from django import forms
from .models import Activity_Gallery, GalleryImage

######## MyCustomForm %%%%%

class MyCustomForm(forms.ModelForm):
    class Meta:
        model = Activity_Gallery
        exclude = ['slug']

    def save(self, commit=True):
        gallery = super().save(commit=False)
        gallery.save()

        images = self.files.getlist('image')
        print('image ', images)
        for image in images:
            GalleryImage.objects.create(gallery=gallery, image=image)
        return gallery