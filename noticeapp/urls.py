from django.urls import path 
from . import views 

app_name = 'noticeapp'


urlpatterns = [
    path('', views.All_notice.as_view(), name='all_notice'),
    path('notice/<slug:slug>/', views.NoticeView.as_view(), name='notice'),
    path('class-routine/', views.RoutineView.as_view(), name='class-routine'),
    path('course-content/', views.Course_content.as_view(), name='course_content'),
]