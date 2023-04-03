from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
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