from logging import getLogger

from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView

from . import models
from . import forms
from .models import Game, GameCategory, Category, Publisher
from .forms import PublisherForm, CategoryForm
# Create your views here.

LOGGER = getLogger()

def hello(request):
    return render(request, 'hello_world/hello.html')

class PublisherView(CreateView):
    model = models.Publisher
    form_class = forms.PublisherForm
    success_url = reverse_lazy('')  #Do uzupełnienia


class CategoryView(CreateView):
    model = models.Category
    form_class = forms.CategoryForm
    success_url = reverse_lazy('')  #Do uzupełnienia

