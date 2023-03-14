from django.urls import path
from . import views

urlpatterns = [

    path("", views.hello, name="hello"),
    path("create-publisher", views.CreatePublisherView.as_view(), name="create-publisher"),
    path("publisher-detail/<int:pk>", views.PublisherDetail.as_view(), name="publisher-detail"),
    path("publisher-update/<int:pk>", views.PublisherUpdate.as_view(), name="publisher-update"),
    path("publisher-delete/<int:pk>", views.PublisherDelete.as_view(), name="publisher-delete"),
    path("all-publisher", views.PublisherListView.as_view(), name="all-publisher"),

    path("create-game", views.CreateGameView.as_view(), name="create-game"),
    path("game-detail/<int:pk>", views.GameDetailView.as_view(), name="game-detail"),
    path("game-update/<int:pk>", views.GameUpdateVIew.as_view(), name="game-update"),
    path("game-delete/<int:pk>", views.GameDeleteView.as_view(), name="game-delete"),
    path("all-games", views.GamesListView.as_view(), name="all-games"),
    path("top-games", views.GameTopListView.as_view(), name="top-games"),
    
    path("create-category", views.CreateCategoryView.as_view(), name="create-category"),
    path("all-categories", views.CategoryListView.as_view(), name="all-categories"),
    path("category-update/<int:pk>", views.CategoryUpdate.as_view(), name="category-update"),
    path("category-delete/<int:pk>", views.CategoryDelete.as_view(), name="category-delete"),
]