from django import forms 
from django.core.validators import FileExtensionValidator
import base64
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

from .models import Student_Model, Certificate_Photo, Thumbnail_photo



# Custom widget for handling multiple file uploads
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        if isinstance(data, (list, tuple)):
            return [super(MultipleFileField, self).clean(d) for d in data]
        return [super().clean(data)]




class Update_student_profile(forms.ModelForm):

    class Meta:
        model = Student_Model
        exclude = ['user', 'slug'] 

    images = MultipleFileField(required=False, label='Upload all your Certificate photos')  # Use custom MultipleFileField # extra added
    cv_clear = forms.BooleanField(required=False, label='Clear CV', help_text="Check this to remove the existing CV")  # extra added


    description = forms.CharField(required=False, label='About yourself', widget=forms.Textarea())
    cv = forms.FileField(required=False, label='Your CV (curiculam vita)', validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
                          widget=forms.FileInput(attrs={'accept': 'application/pdf'}))
    
    skills = forms.CharField(required=False, label='Seperate your skill tags using comma , ', widget=forms.Textarea(attrs={'rows':5, 'placeholder': 'fontend, backend, javascript, html, css, tailwind, bootstrap, graphics design, video editor, node-js, singer, photographer, hacking, volunteer, etc.'}))


    def save(self, commit=True):
        instance = super().save(commit=False)

        


        # Handle clearing CV file if necessary
        if self.cleaned_data.get('cv_clear') and instance.cv:
            instance.cv.delete()

        if commit:
            instance.save()

            # process Profile picture
            profile_pic = self.data.get('cropped_image', '')  # can't use cleaned_data.get() cz this field is not in form class rather extra added in 'template file'
            if profile_pic:
                format, imgstr = profile_pic.split(';base64,')
                ext = format.split('/')[-1]
                image_data = ContentFile(base64.b64decode(imgstr), name=f'profile_pic.{ext}')
                instance.photo = image_data
                instance.save()  # save again to update changes

                ti = Thumbnail_photo.objects.filter(profile=instance)
                if ti.exists():
                    thumbnail = ti.first()

                    img = Image.open(image_data)
                    img = img.resize((50, 50), Image.LANCZOS)  
                    buffer = BytesIO()
                    img.save(buffer, format=ext.upper())
                    compressed_image_data = ContentFile(buffer.getvalue(), name=f'thumbnail_compressed.{ext}')

                    thumbnail.image = compressed_image_data 
                    thumbnail.save()
            else:
                profile_pic = self.data.get('uncropped_but_compressed', '')
                if profile_pic:
                    format, imgstr = profile_pic.split(';base64,')
                    ext = format.split('/')[-1]
                    image_data = ContentFile(base64.b64decode(imgstr), name=f'profile_pic.{ext}')
                    instance.photo = image_data
                    instance.save()  # save again to update changes

                    ti = Thumbnail_photo.objects.filter(profile=instance)
                    if ti.exists():
                        thumbnail = ti.first()

                        img = Image.open(image_data)
                        img = img.resize((50, 50), Image.LANCZOS)  
                        buffer = BytesIO()
                        img.save(buffer, format=ext.upper())
                        compressed_image_data = ContentFile(buffer.getvalue(), name=f'thumbnail_compressed.{ext}')

                        thumbnail.image = compressed_image_data 
                        thumbnail.save()
            
            print('certificate images = ', self.files)

            # process Certificate Images
            compressed_images = self.data.getlist('certificate_images[]')   # can't use cleaned_data.get() cz this field is not in form class rather extra added in 'template file'
            for base64_image in compressed_images:
                # Convert the base64 string back to image
                format, imgstr = base64_image.split(';base64,')  # split the format and base64 string
                ext = format.split('/')[-1]  # extract file extension from format
                image_data = ContentFile(base64.b64decode(imgstr), name=f'certificate_image.{ext}')
                
                # Create and save the Certificate_Photo object with the compressed image
                Certificate_Photo.objects.create(profile=instance, image=image_data)


            #process Thubmnail image

        return instance