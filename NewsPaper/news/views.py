from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime


class PostsList(ListView):
    model = Post
    ordering = '-date_of_creation'
    template_name = 'posts.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
