from logging import getLogger

from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView

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



class CategoryView(CreateView):
    model = models.Category
    form_class = forms.CategoryForm
    success_url = reverse_lazy('')  #Do uzupełnienia


