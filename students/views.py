from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView, ListView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.contrib.auth.views import PasswordChangeView
from collections import defaultdict
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse

from .models import Student_Model, Certificate_Photo
from .forms import Update_student_profile

# Create your views here.

class Password_ChangeView(PasswordChangeView):
    template_name = 'change_password.html'
    
    def get_success_url(self):
        slug = self.request.user.profile.slug
        return reverse_lazy('studentsapp:student-profile', kwargs={'slug': slug})

class Search_skills(ListView):
    model = Student_Model
    template_name = 'search_skills.html' 
    context_object_name = 'students'
    paginate_by = 40

    def get_queryset(self):
        key = self.request.GET.get('skill', '')
        if key: 
            return Student_Model.objects.filter(skills__icontains=key)
        return super().get_queryset()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the search query back to the template so it persists across paginated results
        context['search_query'] = self.request.GET.get('skill', '')
        return context

        # new view created for search students 
class SkillSuggestionView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('skill', '').lower()
        if query:
            # Fetch distinct skill sets matching the query
            students = Student_Model.objects.filter(skills__icontains=query).values_list('skills', flat=True).distinct()[:10]

            # Find only the matching substrings
            matched_skills = []
            for skills in students:
                # Split skills into individual words and match with query
                skill_list = [skill.strip() for skill in skills.split(',')]
                for skill in skill_list:
                    if query in skill.lower():
                    # if skill.lower().startswith(query):
                        matched_skills.append(skill)
                    # if len(matched_skills) >= 10:  # Limit to 10 individual skills
                    #     break
            return JsonResponse(matched_skills, safe=False)
        return JsonResponse([], safe=False)




class All_Students(ListView):
    model = Student_Model
    template_name = 'all_students.html'
    context_object_name = 'students_by_batch'
    paginate_by = 40

    def get_queryset(self):
        # Get the search query from the GET request
        std_name = self.request.GET.get('search', '')

        # If search query exists, filter students based on the search query
        if std_name:
            return Student_Model.objects.filter(Q(name__icontains=std_name) | Q(batch__icontains=std_name)).order_by('-batch', 'std_id')
        
        # If no search query, return all students ordered by batch and std_id
        return Student_Model.objects.order_by('-batch', 'std_id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Group students by batch
        grouped_students = defaultdict(list)
        for student in context['students_by_batch']:
            grouped_students[student.batch].append(student)

        # Add grouped students to context
        context['grouped_students'] = dict(grouped_students)

        # Pass the search query to the template
        context['search_query'] = self.request.GET.get('search', '')
        
        return context




class Student_Profile(DetailView):
    model = Student_Model
    context_object_name = 'profile'
    template_name = 'student_profile.html'
    paginate_by = 3  # Number of images per page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get the student's certificates/photos
        images = Certificate_Photo.objects.filter(profile=self.object)

        # Add pagination for the images
        paginator = Paginator(images, self.paginate_by)
        page_number = self.request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj
        context['is_paginated'] = page_obj.has_other_pages()
        
        return context

    def post(self, request, *args, **kwargs):
        """Handles AJAX request for loading more images."""
        profile = self.get_object()
        page = int(request.POST.get('page', 1))

        images = Certificate_Photo.objects.filter(profile=profile)
        paginator = Paginator(images, self.paginate_by)
        page_obj = paginator.get_page(page)

        image_urls = [image.image.url for image in page_obj]
        has_next = page_obj.has_next()

        return JsonResponse({
            'image_list': image_urls,
            'has_next': has_next
        })


class Update_profile(LoginRequiredMixin, UpdateView):
    model = Student_Model
    form_class = Update_student_profile
    template_name = 'update_student_profile.html'

    def get_success_url(self):
        return reverse_lazy('studentsapp:student-profile', kwargs={'slug': self.request.user.profile.slug})

    def get_object(self, queryset=None):
        return get_object_or_404(Student_Model, user=self.request.user)




class  Delete_certificates(View):
    def get(self, request):
        obj = Student_Model.objects.get(user = request.user)
        return render(request, 'delete_certificates.html', {'obj': obj})
    
    def post(self, request):
        # Get selected certificate IDs from the POST request
        selected_certificates = request.POST.getlist('certificates')

        if selected_certificates:
            # Delete the selected certificates
            Certificate_Photo.objects.filter(id__in=selected_certificates).delete()

        return redirect(reverse_lazy('studentsapp:student-profile', kwargs={'slug': request.user.profile.slug }))
