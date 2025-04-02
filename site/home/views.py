from django.http import HttpResponse
from django.shortcuts import render
from .models import Image

def Index(request):
    return HttpResponse("Welcome to the homepage!")

def Image_view(request):
    images = Image.objects.all()
    return render(request, 'home.html', {'images': images}) # Django automatically looks for templates in the templates directory (either globally or within the app).