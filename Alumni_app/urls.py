from django.urls import path 
from . import views

app_name = 'Alumni_app'


urlpatterns = [
    path('', views.HomeView.as_view(), name='home')
]