from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name="hello"),
    path("create-category", views.CreateCategoryView.as_view(), name="create-category"),
    path("all-categories", views.CategoryListView.as_view(), name="all-categories"),
path("category-update/<int:pk>", views.CategoryUpdate.as_view(), name="category-update"),
path("category-delete/<int:pk>", views.CategoryDelete.as_view(), name="category-delete"),
]