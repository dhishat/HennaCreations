from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class GalleryView(TemplateView):
    template_name = "gallery_home.html"