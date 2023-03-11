from logging import getLogger

from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from . import models
from . import forms
from .models import Game, GameCategory, Category, Publisher
from .forms import CreatePublisherForm, CategoryForm
# Create your views here.



def hello(request):
    return render(request, "hello_world/hello.html")

class CreatePublisherView(CreateView):
    model = Publisher
    form_class = forms.CreatePublisherForm
    template_name = "hello_world/create_publisher.html"
    success_url = reverse_lazy(hello)

class PublisherDetail(DetailView):
    model = Publisher
    form_class = forms.CreatePublisherForm
    template_name = "hello_world/publisher_detail.html"

class PublisherUpdate(UpdateView):
    model = Publisher
    template_name = "hello_world/publisher_update.html"
    fields = ['name', 'country']
    success_url = reverse_lazy(hello)

class PublisherDelete(DeleteView):
    model = Publisher
    template_name = "hello_world/publisher_delete.html"
    success_url = reverse_lazy(hello)


class CategoryView(CreateView):
    model = models.Category
    form_class = forms.CategoryForm
    success_url = reverse_lazy('')  #Do uzupełnienia


