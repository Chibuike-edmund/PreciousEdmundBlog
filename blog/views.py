from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        "about": "Precious Edmund",
        "title": "Blog Post 1",
        "Content": "First Post Content",
        "Date_Posted": "September 29, 2023 "
    },
]

def home(request):
    return render(request, "blog/home.html")

def about(request):
    return render(request, "blog/about.html")