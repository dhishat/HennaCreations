from django.urls import path
from .views import GalleryView

urlpatterns = [
    path("home", GalleryView, name="home"),
]