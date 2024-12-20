from django.urls import path 
from . import views 

app_name = 'Faculty_app'

urlpatterns = [
    path('about-cse/', views.About_CSE_View.as_view(), name='about_cse'),
    path('faculty_members/', views.Faculty_members.as_view(), name='faculty_members'),
    path('faculty_profile/<int:pk>/', views.Faculty_profileView.as_view(), name='faculty_profile'),
    path('faculty_staffs/', views.Faculty_staffView.as_view(), name='faculty_staffs'),
    path('moderators/', views.Instructor_developer_moderatorView.as_view(), name='moderators'),
    path('developers/', views.DeveloperView.as_view(), name='developers'),
]

