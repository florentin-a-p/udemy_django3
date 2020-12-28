from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    # return HttpResponse('Hello there friend!')
    # return render(request,'generator/home.html',{'password':'asdf2341'})
    # return render(request,'templates/generator/home.html')
    return render(request,'generator/home.html')
    # return 'Hello there friend!'

# def password(request):
    
#     chara_characters = list('abcdefghijklmnopqrstuvwyz')
#     chara_uppercase = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#     chara_numbers = list('1234567890')
#     chara_special_symbols = list('!@#$%^&*()_+~?><:"|')

#     # bagian if else if else buat randomized characters

#     # length = 10
#     length = int(request.GET.get('length',10))
#     bool_uppercase = bool(request.GET.get('uppercase'))
#     bool_numbers = bool(request.GET.get('numbers'))
#     bool_special_symbols = bool(request.GET.get('special_symbols'))
#     # uppercase = request.GET.get('uppercase')
#     # length = home.value
#     thepassword = ''

#     if bool_uppercase is True:
#         chara_characters=chara_characters+chara_uppercase
#     if bool_special_symbols is True:
#         chara_characters=chara_characters+chara_special_symbols
#     if bool_numbers is True:
#         chara_characters=chara_characters+chara_numbers

#     for x in range(length):
#             thepassword += random.choice(chara_characters)    
#     return render(request,'generator/password_woyyy.html',{'password':thepassword})


def password(request):
    characters = list('abcdefghijklmnopqrstuvwyz')
 
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special_symbols'):
        characters.extend(list('!@#$%^&*()_+~?><:"|'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length',10))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)    
    return render(request,'generator/password_woyyy.html',{'password':thepassword})


def eggs(request):
    return HttpResponse('<h1>Eggs are so tasty</h1>')

def barbie(request):
    return HttpResponse('i"m your baby girl')
