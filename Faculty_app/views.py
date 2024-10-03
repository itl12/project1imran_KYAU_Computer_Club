from django.shortcuts import render
from django.views.generic import DetailView, ListView


from .models import Faculty_profile, Faculty_staff, Instructor_developer_moderator

# Create your views here.


class Faculty_profileView(DetailView):
    model = Faculty_profile
    context_object_name = 'profile'
    template_name = 'faculty_profile.html'


class Faculty_members(ListView):
    model = Faculty_profile
    context_object_name = 'members'
    template_name = 'faculty_mambers.html'


class Faculty_staffView(ListView):
    model = Faculty_staff
    context_object_name = 'members'
    template_name = 'faculty_staff.html'
    

class Instructor_developer_moderatorView(ListView):
    model = Instructor_developer_moderator
    context_object_name = 'members'
    template_name = 'instructor_developer_moderator.html'