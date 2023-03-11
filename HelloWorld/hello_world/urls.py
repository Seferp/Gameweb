from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello),
    path("create-publisher", views.CreatePublisherView.as_view(), name="create-publisher"),
    path("<int:pk>/", views.PublisherDetail.as_view(), name="publisher-detail"),
    path("<int:pk>/update", views.PublisherUpdate.as_view(), name="publisher-update"),
    path("<int:pk>/delete", views.PublisherDelete.as_view(), name="publisher-delete"),
]
