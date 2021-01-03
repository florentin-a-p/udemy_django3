from django.shortcuts import render
from django.http import HttpResponse
from .models import ProjectBlogFlo

# Create your views here.
def all_blogs(request):
    projects = ProjectBlogFlo.objects.all()
    return render(request, 'blog/all_blogs.html',{'projects':projects})


