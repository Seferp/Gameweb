from logging import getLogger

from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from . import models
from . import forms
from .models import Game, GameCategory, Category, Publisher
from .forms import PublisherForm, CategoryForm
# Create your views here.

LOGGER = getLogger()

def hello(request):
    return render(request, 'hello_world/hello.html')



class CategoryListView(ListView):
    model = Category
    template_name = "hello_world/all_categories.html"
    ordering = ["type"]
    context_object_name = "categories"

class CreateCategoryView(CreateView):
    model = Category
    form_class = forms.CreateCategoryForm
    template_name = "hello_world/create_categories.html"
    success_url = reverse_lazy("all-categories")

class CategoryUpdate(UpdateView):
    model = Category
    template_name = "hello_world/category_update.html"
    fields = ['type']
    success_url = reverse_lazy("all-categories")

class CategoryDelete(DeleteView):
    model = Category
    template_name = "hello_world/category_delete.html"
    success_url = reverse_lazy("all-categories")