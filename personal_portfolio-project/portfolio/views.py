from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import ProjectFlo

# Create your views here.
def home(request):
    projects = ProjectFlo.objects.all()
    return render(request,'portfolio/home.html',{'projects':projects}) #kok bisa otomatis ambil dr folder templates ya??
