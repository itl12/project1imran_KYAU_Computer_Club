from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Student_Model(models.Model):
    photo = models.ImageField(upload_to='students_profile_pic', blank=True, null=True)
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    batch = models.IntegerField(blank=True, null=True)
    std_id = models.CharField(max_length=16)
    description = models.TextField(blank=True, null=True)
    cv = models.FileField(upload_to='students_cv/', blank=True, null=True)
    skills = models.CharField(max_length=1000, blank=True, null=True)
    slug = models.SlugField(unique=True)

    class Meta():
        ordering = ['-batch', 'std_id']
        verbose_name= 'Student Info'

    def __str__(self):
        return f'{self.batch}th batch | {self.name} | id: {self.std_id}'


class Certificate_Photo(models.Model):
    profile = models.ForeignKey(Student_Model, related_name='certificates', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='students_certificates', blank=True, null=True)
    upload_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.profile.batch}th batch | {self.profile.std_id} | {self.profile.name}'
    
    class Meta():
        verbose_name_plural = 'Student Certificates'
        ordering = ['profile__batch', 'profile__std_id', '-upload_date']


class Thumbnail_photo(models.Model):
    profile = models.OneToOneField(Student_Model, related_name='thumbnail', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='thumbnails', blank=True, null=True)
    
    def __str__(self):
        return f'{self.profile.user.username}'
    
    class Meta():
        ordering = ['-pk']
