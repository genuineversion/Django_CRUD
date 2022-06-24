from audioop import reverse
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post
# Create your views here.

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

class PostCreateView(CreateView):
    model=Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostUpdateView(UpdateView):
    model=Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostListView(ListView):
    model=Post

class PostDetailView(DetailView):
    model=Post

class PostDeleteView(DeleteView):
    model=Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")


