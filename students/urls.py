from django.urls import path 
from . import views 

app_name = 'studentsapp'

urlpatterns = [
    path('ajax/skill-suggestions/', views.SkillSuggestionView.as_view(), name='skill-suggestions'),
    path('search_skills/', views.Search_skills.as_view(), name='search_skills'),
    path('all-students/', views.All_Students.as_view(), name='all_students'),
    path('profile/<slug:slug>/', views.Student_Profile.as_view(), name='student-profile'),
    path('update-profile/', views.Update_profile.as_view(), name='update_profile'),
    path('change-password/', views.Password_ChangeView.as_view(), name='change_password'),
    path('modify-certificates/', views.Delete_certificates.as_view(), name='modify_certificates')
]

