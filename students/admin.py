from django.contrib import admin
from .models import Student_Model, Certificate_Photo, Thumbnail_photo
from .forms import Update_student_profile

# Register your models here.
class Student_admin(admin.ModelAdmin):
    form = Update_student_profile

admin.site.register(Student_Model, Student_admin)
admin.site.register(Certificate_Photo)
admin.site.register(Thumbnail_photo)