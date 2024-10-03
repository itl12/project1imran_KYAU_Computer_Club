from django.shortcuts import render
from django.views.generic import DetailView


from .models import Faculty_profile

# Create your views here.


class Faculty_profile(DetailView):
    model = Faculty_profile
    context_object_name = 'profile'
    template_name = 'faculty_profile.html'
