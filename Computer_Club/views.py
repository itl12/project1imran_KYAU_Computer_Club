from django.shortcuts import render 
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView

from galleryapp.models import Carousel, Activity_Gallery
from noticeapp.models import Notice
from students.models import Student_Model
from .forms import Create_user_and_profile_form


class Custom_loginview(LoginView):
    template_name = 'registration/login.html'
    def get_success_url(self) -> str:
        try:
            profile = self.request.user.profile
            return reverse_lazy('studentsapp:student-profile', kwargs={'slug': profile.slug })
        except Student_Model.DoesNotExist:
            return '/'

class SignUpView(CreateView):
    form_class = Create_user_and_profile_form
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    

class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        carousel = Carousel.objects.all()
        context['carousel'] = carousel

        notices = Notice.objects.all()[0:6]
        context['notices'] = notices 

        activities = Activity_Gallery.objects.all()[0:6]
        context['activities'] = activities
        return context
    


class Contact_view(TemplateView):
    template_name = 'contact-us.html'