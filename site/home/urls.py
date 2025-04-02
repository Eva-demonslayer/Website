from django.urls import path

from . import views

urlpatterns = [
    path("", views.Index, name="Index"),
    path("images/", views.Image_view, name="Image"),  # URL for the Image view
]