from django.urls import path
from .views import GalleryView

urlpatterns = [
    path("home", GalleryView.as_view(), name="home"),
]