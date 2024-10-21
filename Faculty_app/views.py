from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView


from .models import Faculty_profile, Faculty_staff, Instructor_developer_moderator, About_CSE

# Create your views here.


class About_CSE_View(TemplateView):
    template_name = 'about_cse.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj'] = About_CSE.objects.first()
        context['head_sir'] = Faculty_profile.objects.first()
        return context



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
    template_name = 'admin_moderators.html'


class DeveloperView(TemplateView):
    template_name = 'developers.html'
