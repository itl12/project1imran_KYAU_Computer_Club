from django.db import models
from django.core.files.base import ContentFile
from PIL import Image, ImageOps
from io import BytesIO

# Create your models here.

class Faculty_profile(models.Model):
    photo = models.ImageField(upload_to='faculty_members', blank=True, null=True)
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    short_biography = models.CharField(max_length=1500, blank=True, null=True)
    research_interest = models.CharField(max_length=1500, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    whatsapp = models.CharField(max_length=15, blank=True, null=True)
    linkedin = models.CharField(max_length=50, blank=True, null=True)
    github = models.CharField(max_length=50, blank=True, null=True)
    room_number = models.CharField(max_length=10, blank=True, null=True)
    sorting_priority = models.IntegerField(blank=True, null=True)

    class Meta():
        ordering = ['sorting_priority']
    
    def __str__(self):
        return f"{self.name} | {self.designation}"


    def save(self, *args, **kwargs):
        if self.photo:
            img = Image.open(self.photo)
            
            try:
                img = ImageOps.exif_transpose(img)  # This corrects orientation based on EXIF data
            except (ValueError, TypeError, AttributeError):
                # In case no EXIF data is available, we just continue
                pass

            if img.mode == "P":
                img = img.convert("RGBA")

            max_size = (400, 400)
            img.thumbnail(max_size, Image.Resampling.LANCZOS)

            img_io = BytesIO()
            img.save(img_io, format='PNG')  # Save as PNG (no need for quality setting)

            # Replace the image file with the compressed version
            self.photo = ContentFile(img_io.getvalue(), name=self.photo.name)

        super().save(*args, **kwargs)



class Research_and_publication(models.Model):
    faculty = models.ForeignKey(Faculty_profile, related_name='research_and_publications', on_delete=models.CASCADE)
    research_and_publication = models.TextField()

    class Meta():
        ordering = ['faculty__name']

    def __str__(self):
        return f"{self.faculty.name}"


class Academic_info(models.Model):
    faculty = models.ForeignKey(Faculty_profile, related_name='academic_info', on_delete=models.CASCADE)
    degree = models.CharField(max_length=220)
    institution = models.CharField(max_length=220)
    period = models.CharField(max_length=60, blank=True, null=True)

    class Meta():
        ordering = ['faculty__name', '-pk']

    def __str__(self):
        return f"{self.faculty.name} | {self.degree}"


class Experience(models.Model):
    faculty = models.ForeignKey(Faculty_profile, related_name='experiences', on_delete=models.CASCADE)
    institution_organization = models.CharField(max_length=60)
    position = models.CharField(max_length=220)
    job_role = models.CharField(max_length=220, blank=True, null=True)
    period = models.CharField(max_length=60, blank=True, null=True)

    class Meta():
        ordering = ['faculty__name', '-pk']

    def __str__(self):
        return f"{self.faculty.name} | {self.position} | {self.institution_organization}"
    

class Faculty_staff(models.Model):
    photo = models.ImageField(upload_to='faculty_staff', blank=True, null=True)
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    whatsapp = models.CharField(max_length=15, blank=True, null=True)
    room_number = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.name} | {self.designation}"
    


class Instructor_developer_moderator(models.Model):
    photo = models.ImageField(upload_to='inst_dev_moder', blank=True, null=True)
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    whatsapp = models.CharField(max_length=15, blank=True, null=True)
    facebook = models.CharField(max_length=150, blank=True, null=True)
    linkedin = models.CharField(max_length=50, blank=True, null=True)
    github = models.CharField(max_length=50, blank=True, null=True)
    sorting_priority = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} | {self.designation}"
    
    def save(self, *args, **kwargs):
        if self.photo:
            img = Image.open(self.photo)
            
            try:
                img = ImageOps.exif_transpose(img)  # This corrects orientation based on EXIF data
            except (ValueError, TypeError, AttributeError):
                # In case no EXIF data is available, we just continue
                pass

            if img.mode == "P":
                img = img.convert("RGBA")

            max_size = (400, 400)
            img.thumbnail(max_size, Image.Resampling.LANCZOS)

            img_io = BytesIO()
            img.save(img_io, format='PNG')  # Save as PNG (no need for quality setting)

            # Replace the image file with the compressed version
            self.photo = ContentFile(img_io.getvalue(), name=self.photo.name)

        super().save(*args, **kwargs)