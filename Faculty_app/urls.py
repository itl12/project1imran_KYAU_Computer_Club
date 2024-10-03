from django.urls import path 
from . import views 

app_name = 'Faculty_apps'

urlpatterns = [
    path('faculty_profile/<int:pk>/', views.Faculty_profile.as_view(), name='faculty_profile'),
]