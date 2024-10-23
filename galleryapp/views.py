from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView 
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Activity_Gallery, Category_Activity_Gallery

# Create your views here.
class RoutineView(TemplateView):
    template_name = 'class.html'


class List_activity(ListView):
    model = Activity_Gallery
    template_name = 'activity_list.html'  # Replace with your actual template
    context_object_name = 'activities'
    paginate_by = 8  # Optional: Adds pagination

    def get_queryset(self):
        queryset = Activity_Gallery.objects.all()
        category_id = self.request.GET.get('category')
        
        if category_id:
            queryset = queryset.filter(category__id=category_id)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category_Activity_Gallery.objects.all()
        context['selected_category'] = self.request.GET.get('category', None)
        return context



class ActivityGallary(DetailView):
    model = Activity_Gallery
    template_name = 'activity_gallery.html'
    context_object_name = 'activity'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        images = self.object.images.all()
        paginator = Paginator(images, 6)  # Initial 6 images per load
        page_number = self.request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            page_number = request.POST.get('page')
            images = self.get_object().images.all()
            paginator = Paginator(images, 6)
            page_obj = paginator.get_page(page_number)
            image_list = []
            for img in page_obj:
                image_list.append(img.image.url)
            return JsonResponse({'image_list' : image_list, 'has_next': page_obj.has_next()})
        return super().post(request, *args, **kwargs)
    

