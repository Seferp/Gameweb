from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello),
    path("create-publisher", views.CreatePublisherView.as_view(), name="create-publisher"),
]
