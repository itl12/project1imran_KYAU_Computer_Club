from django.contrib import admin
from .models import Student_Model, Certificate_Photo, Thumbnail_photo

# Register your models here.
admin.site.register(Student_Model)
admin.site.register(Certificate_Photo)
admin.site.register(Thumbnail_photo)