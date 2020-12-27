from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('Hello there friend!')
    return render(request,'generator/home.html',{'password':'asdf2341'})
    # return 'Hello there friend!'

def eggs(request):
    return HttpResponse('<h1>Eggs are so tasty</h1>')

def barbie(request):
    return HttpResponse('i"m your baby girl')
