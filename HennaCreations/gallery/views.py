from django.shortcuts import render
from django.http import HttpResponse


def GalleryView(request):
    return HttpResponse("Hello, World!")