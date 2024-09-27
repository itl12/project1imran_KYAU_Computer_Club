import uuid
from django.db import models 
from django.utils.text import slugify

class Carousel(models.Model):
    image = models.ImageField(upload_to='carousel', default=None)

    class Meta():
        ordering = ['image']

    
class Activity_Gallery(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField(blank=True, null=True)
    date = models.DateField()
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta():
        verbose_name_plural = 'Activity Gallery'
        ordering = ['-id']

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(str(uuid.uuid4()))
        return super().save(**kwargs)

    def __str__(self):
        return f'{self.title[:30]} | {self.date}'



class GalleryImage(models.Model):
    gallery = models.ForeignKey(Activity_Gallery, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery_images/')

    class Meta():
        ordering = ['gallery']

    def __str__(self):
        return  f"Image for {self.gallery.title}" 