from django.shortcuts import render
from django.views.generic import ListView
from .models import BlogModel

class IndexView(ListView):
    model = BlogModel
    template_name = 'pages/index.html'
    context_object_name = 'blogs'