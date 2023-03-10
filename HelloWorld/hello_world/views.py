from logging import getLogger

from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from . import models
from . import forms
from .models import Game, GameCategory, Category, Publisher
from .forms import PublisherForm, CategoryForm
# Create your views here.

LOGGER = getLogger()

def hello(request):
    return render(request, "hello_world/hello.html")


class GameTopListView(ListView):
    model = Game
    template_name = "hello_world/top_games.html"
    ordering = ("-rating")
    context_object_name = "top_games"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:10]
        return data

class GamesListView(ListView):
    model = Game
    template_name = "hello_world/all_games.html"
    ordering = ["title"]
    context_object_name = "games"


class CreateGameView(CreateView):
    model = Game
    form_class = forms.CreateGameForm
    template_name = 'hello_world/create_game.html'
    success_url = reverse_lazy("all-games")

class GameDetailView(DeleteView):
    model = Game
    form_class = forms.CreateGameForm
    template_name = "hello_world/game_detail.html"

class GameUpdateVIew(UpdateView):
    model = Game
    template_name = 'hello_world/game_update.html'
    fields = ["title", "publisher", "release_date"]
    success_url = reverse_lazy("all-games")

class GameDeleteView(DeleteView):
    model = Game
    template_name = "hello_world/game_delete.html"
    success_url = reverse_lazy("all-games")



class PublisherListView(ListView):
    model = Publisher
    template_name = "hello_world/all_publisher.html"
    ordering = ["name"]
    context_object_name = "publishers"

class CreatePublisherView(CreateView):
    model = Publisher
    form_class = forms.CreatePublisherForm
    template_name = "hello_world/create_publisher.html"
    success_url = reverse_lazy("all-publisher")

class PublisherDetail(DetailView):
    model = Publisher
    form_class = forms.CreatePublisherForm
    template_name = "hello_world/publisher_detail.html"

class PublisherUpdate(UpdateView):
    model = Publisher
    template_name = "hello_world/publisher_update.html"
    fields = ['name', 'country']
    success_url = reverse_lazy("all-publisher")

class PublisherDelete(DeleteView):
    model = Publisher
    template_name = "hello_world/publisher_delete.html"
    success_url = reverse_lazy("all-publisher")
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