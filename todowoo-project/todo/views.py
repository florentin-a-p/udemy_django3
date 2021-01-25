from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from .models import ProjectTodoWooFlo
from django.utils import timezone

def home(request):
    return render(request, 'todo/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form':UserCreationForm()})
    else:
        # create new user
        if request.POST['password1'] == request.POST['password2']:
            try: 
                # user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user_name = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                # user.save()
                user_name.save()
                # login(request, user)
                login(request, user_name)
                return redirect('currenttodos')

            except IntegrityError:
                return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
        else:
            #tell the user the passwords didn't match
            # print("hello")
            return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form':AuthenticationForm()})
    else:
        # user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        user_name = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        # if user is None:
        if user_name is None:
            return render(request, 'todo/loginuser.html', {'form':AuthenticationForm(), 'error':'username and password did not match'})
        else:
            # login(request, user)
            login(request, user_name)
            return redirect('currenttodos')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def createtodo(request):
    if request.method == 'GET':
        return render(request, 'todo/createtodo.html', {'form':TodoForm()}) 

    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            # newtodo.creator = request.user_name
            # newtodo.user_name = request.user_name
            newtodo.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/createtodo.html', {'form':TodoForm(), 'error':'bad data passed in. try again'}) 

def currenttodos(request):
    todos = ProjectTodoWooFlo.objects.filter(user=request.user, memo_complete_date__isnull=True)
    return render(request, 'todo/currenttodos.html',{'todos':todos})


def completedtodos(request):
    todos = ProjectTodoWooFlo.objects.filter(user=request.user, memo_complete_date__isnull=False).order_by('-memo_complete_date')
    return render(request, 'todo/completedtodos.html',{'todos':todos})

def createdtodos(request):
    todos = ProjectTodoWooFlo.objects.filter(user=request.user)
    return render(request, 'todo/createdtodos.html',{'todos':todos})


def viewtodo(request, todo_pk):
    todos = ProjectTodoWooFlo.objects.filter(user=request.user).get(pk=todo_pk)
    
    if request.method == 'GET':
        form = TodoForm(instance=todos)
        return render(request, 'todo/viewtodo.html',{'todos':todos,'form':form})
    else: 
        try:
            form = TodoForm(request.POST, instance=todos)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/viewtodo.html',{'todos':todos,'form':form, 'error':'bad info'})
             

def completetodo(request, todo_pk):
    todos = get_object_or_404(ProjectTodoWooFlo, pk=todo_pk, user=request.user)
    # todos = ProjectTodoWooFlo.objects.filter(user=request.user, memo_complete_date__isnull=True).get(pk=todo_pk)
    if request.method == 'POST':
        todos.memo_complete_date = timezone.now()
        todos.save()
        return redirect('currenttodos')

def deletetodo(request, todo_pk):
    todos = get_object_or_404(ProjectTodoWooFlo, pk=todo_pk, user=request.user)
    # todos = ProjectTodoWooFlo.objects.filter(user=request.user, memo_complete_date__isnull=True).get(pk=todo_pk)
    if request.method == 'POST':
        todos.delete()
        return redirect('currenttodos')



