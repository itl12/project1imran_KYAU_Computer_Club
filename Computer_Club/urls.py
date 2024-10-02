
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.contrib.staticfiles.urls import static
from django.conf import settings
from django.contrib.auth import views as auth_views



from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root' : settings.STATIC_ROOT }),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root' : settings.MEDIA_ROOT }),
    path('', views.Home.as_view(), name='home'),
    path('contact-us/', views.Contact_view.as_view(), name='contact_us'),
    path('notices/', include('noticeapp.urls')),
    path('gallery/', include('galleryapp.urls')),
    path('students/', include('students.urls')),



    path('login/', views.Custom_loginview.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

] 

