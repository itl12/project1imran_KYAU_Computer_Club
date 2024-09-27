from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from .models import Notice, RoutineModel
# Create your views here.

class All_notice(ListView):
    model = Notice
    template_name = 'all_notice.html'
    context_object_name = 'notices'
    paginate_by = 7
    


class NoticeView(DetailView):
    model = Notice 
    context_object_name = 'notice'
    template_name = 'notice.html'



class RoutineView(TemplateView):
    template_name = 'routine.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['routine'] =  RoutineModel.objects.all().first()
        return context 
        
    


    