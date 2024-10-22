from django import forms
from django.core.validators import FileExtensionValidator
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from .models import Notice, RoutineModel, Notice_images


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



class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        exclude = ['slug']
        # fields = '__all__'
        widgets = {
            'body': forms.Textarea(attrs={'rows': 25, 'cols': 150}),  # Set initial rows and columns for the body field
        }


    # Define the pdf field with the FileExtensionValidator for PDF files
    pdf = forms.FileField(
        required=False,  # Make it optional if needed
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],  # Validate PDF files only
        widget=forms.ClearableFileInput(attrs={'accept': 'application/pdf'})  # Accept PDF in file input
    )

    image = MultipleFileField(required=False)

    def save(self, commit=True):
        instance = super().save(commit=False)
        
        instance.save()
        images = self.files.getlist('image')
        for img in images:
            image = Image.open(img)
            max_width = 600
            if image.width > max_width:
                new_height = int((max_width / image.width) * image.height)
                image = image.resize((max_width, new_height), Image.Resampling.LANCZOS)
            buffer = BytesIO()
            image.save(buffer, format='JPEG', quality=100)
            buffer.seek(0)
            compressed_image = ContentFile(buffer.read(), name=img.name)
            Notice_images.objects.create(notice=instance, image=compressed_image)

        return instance


class RoutineForm(forms.ModelForm):
    class Meta:
        model = RoutineModel 
        fields = ['routine_pdf', 'routine_photo']
        
    routine_pdf = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
                          widget=forms.FileInput(attrs={'accept': 'application/pdf'}))