from django.shortcuts import render
from .models import Project, Category
# Create your views here.d
def home(request):
    return render(request, "home.html")

def projects(request):
    projects = Project.objects.all()
    categories = Category.objects.all()
    return render(request, "projects.html", {"projects" : projects, "categories" : categories})