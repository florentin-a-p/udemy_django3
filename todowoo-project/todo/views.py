from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from .models import ProjectTodoWooFlo

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
        # # create new user
        # if request.POST['password1'] == request.POST['password2']:
        #     try: 
        #         user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
        #         user.save()
        #         login(request, user)
        #         return redirect('currenttodos')

        #     except IntegrityError:
        #         return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
        # else:
        #     #tell the user the passwords didn't match
        #     # print("hello")
        #     return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})



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
    todos = ProjectTodoWooFlo.objects.all()
    return render(request, 'todo/currenttodos.html',{'todos':todos})









# def detail_view(request, product_id):
#     product = Product.objects.get(pk=product_id)
#     comment_form = CommentForm(request.POST, instance=product)
#     if comment_form.is_valid():
#         comment_form.save()
#         comment_form = CommentForm()
#     context = {'product': product, 'comment_form': comment_form}
#     return render(request, 'my_rev/detail_view.html', context)


# def detail_view(request, product_id):
#     product = Product.objects.get(pk=product_id)
#     if product:
#         comment_form = CommentForm(request.POST or None, instance=product)
#         if comment_form.is_valid():
#             comment_form.save()
#             comment_form = CommentForm()
#     context = {'product': product, 'comment_form': comment_form}
#     return render(request, 'my_rev/detail_view.html', context)










# <body>
# <h1>{{ product.title }}</h1>
# <p>
# <p><strong>PRODUCT DESCRIPTION</strong></p>
#     {{ product.description }}
# <p><strong>Price: </strong>Rs.{{ product.price }}</p>
# <ul>
# {% for comment in product.comment_set.all %}
#     <li>{{ comment.comment|capfirst }}</li>

# {% endfor %}
#         </ul>
# <p><a href="/comment/"><strong>ADD COMMENT</strong></a></p>





# <body>
# <h1>{{ product.title }}</h1>
# <p>
# <p><strong>PRODUCT DESCRIPTION</strong></p>
#     {{ product.description }}
# <p><strong>Price: </strong>Rs.{{ product.price }}</p>
# <ul>
#    {% for comment in product.comment_set.all %}
#     <li>{{ comment.comment|capfirst }}</li>

# {% endfor %}
#         </ul>

# <form method="POST"> {% csrf_token %}
#     {{ comment_form.as_p }}
#     <input type="submit" value="Save"/>
# </form>
