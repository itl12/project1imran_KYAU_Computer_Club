from django import forms 
from django.utils.text import slugify
import uuid
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

from students.models import Student_Model, Thumbnail_photo

class Create_user_and_profile_form(UserCreationForm):
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.save()
        if commit is True:
            obj = Student_Model.objects.create(user=instance)
            if not obj.slug:
                obj.slug = slugify(str(uuid.uuid4()))
            obj.save()
            Thumbnail_photo.objects.create(profile=obj)
        return instance

