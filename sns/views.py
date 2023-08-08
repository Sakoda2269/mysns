from django.shortcuts import render
from .models import Post
from django.views import generic


class IndexView(generic.ListView):
    model = Post


class DetailView(generic.DetailView):
    model = Post
