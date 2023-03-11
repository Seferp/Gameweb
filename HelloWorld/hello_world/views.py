from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView

from . import models
from . import forms
from .models import Game, GameCategory, Category, Publisher
from .forms import PublisherForm, CategoryForm
# Create your views here.

def hello(request):
    return render(request, 'hello_world/hello.html')

class PublisherView(CreateView):
    model = models.Publisher
    form_class = forms.PublisherForm
    success_url = ''  #Do uzupełnienia

    def get(self, **kwargs):
