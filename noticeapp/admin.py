from django.contrib import admin
from .models import Notice, RoutineModel, Notice_images
from .forms import NoticeForm, RoutineForm

# Register your models here.

class NoticeAdmin(admin.ModelAdmin):
    form = NoticeForm
    
class RoutineAdmin(admin.ModelAdmin):
    form = RoutineForm

admin.site.register(Notice, NoticeAdmin)
admin.site.register(RoutineModel, RoutineAdmin)
admin.site.register(Notice_images)