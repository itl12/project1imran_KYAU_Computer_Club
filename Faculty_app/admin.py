from django.contrib import admin
from .models import Faculty_profile, Research_and_publication, Academic_info, Experience
from . forms import Faculty_profile_form


class Faculty_profile_admin(admin.ModelAdmin):
    form = Faculty_profile_form



admin.site.register(Faculty_profile, Faculty_profile_admin)

admin.site.register(Research_and_publication)
admin.site.register(Academic_info)
admin.site.register(Experience)