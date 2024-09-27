from django.urls import path 
from . import views 


app_name = 'galleryapp'

urlpatterns = [
    path('list-activity/', views.List_activity.as_view(), name='list_activity'),
    path('<slug:slug>/', views.ActivityGallary.as_view(), name='activity-gallery'),
    path('cla/', views.RoutineView.as_view(), name='cla'),
]