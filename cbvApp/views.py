from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView
from .models import Course
from .forms import CourseForm


class CourseListView(ListView):
    model = Course
    template_name = 'cbvApp/index.html'
    context_object_name = 'course_list'


class CourseCreateView(CreateView):
    model = Course
    template_name = 'cbvApp/create.html'
    form_class = CourseForm
    success_url = '/'


class CourseDetailView(DetailView):
    model = Course
    template_name = 'cbvApp/detail.html'
    context_object_name = 'course'
    
    
class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'cbvApp/delete.html'
    success_url = '/'