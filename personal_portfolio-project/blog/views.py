from django.shortcuts import render
from django.http import HttpResponse
from .models import ProjectBlogFlo

# Create your views here.
def all_blogs(request):
    # projects = ProjectBlogFlo.objects.all()
    projects = ProjectBlogFlo.objects.order_by('date')
    return render(request, 'blog/all_blogs.html',{'projects':projects})


