from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Blog
# Create your views here.
class BlogView (ListView):
    model = Blog
    template_name = "blog.html"

class BlogDetail (DetailView):
    model = Blog
    template_name = "blog_detail.html"

class BlogCreate (CreateView):
    model = Blog
    template_name = "blog_create.html"
    fields = ['title', 'author', 'body']

class BlogEdit (UpdateView):
    model = Blog
    template_name = "blog_edit.html"
    fields = ["title", "body"]

class BlogDelete (DeleteView):
    model = Blog
    template_name = "blog_delete.html"
    success_url = reverse_lazy('home')

