from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, DeleteView, UpdateView)
from pprint import pprint

from .forms import *
from .filters import PostsFilter
from .models import Post


class PostsList(ListView):
    model = Post
    ordering = '-date_of_creation'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 7
    paginate_orphans = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pprint(context)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        pprint(queryset)
        return queryset


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pprint(context)
        return context


class PostsSearch(ListView):
    model = Post
    ordering = '-date_of_creation'
    template_name = 'posts_search.html'
    context_object_name = 'posts'
    paginate_by = 7
    paginate_orphans = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        pprint(context)
        return context


class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    model = Post
    form_class = PostCreateForm
    template_name = 'post_create_edit.html'
    success_url = reverse_lazy('posts_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'NWS'
        return super().form_valid(form)


class ArticlesCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    model = Post
    form_class = PostCreateForm
    template_name = 'post_create_edit.html'
    success_url = reverse_lazy('posts_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'ART'
        return super().form_valid(form)


class PostEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    model = Post
    form_class = PostCreateForm
    template_name = 'post_create_edit.html'
    success_url = reverse_lazy('posts_list')


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts_list')
