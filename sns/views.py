from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(generic.ListView):
    model = Post


class DetailView(generic.DetailView):
    model = Post


class CreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Post
    fields = ["title", "detail"]


    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super(CreateView, self).form_valid(form)

class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Post
    fields = ["title", "detail"]


class DeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Post
    success_url = reverse_lazy("sns:index")

