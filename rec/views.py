from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', {'form': UserCreationForm()})
    else:
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                user = User.objects.create_user(username=request.POST.get(
                    'username'), passwoer=request.POST.get('password2'))
            except IntegrityError:
                error = 'This username is already taken. Try another one.'
                return render(request, 'register.html', {'form':UserCreationForm(), 'error': error})
            else:
                user.save()
                # login user
                return redirect('home')
        else:
            error = 'Password did not match. Try again.'
            return render(request, 'register.html', {'form': UserCreationForm, 'error': error})

def home(request):
    return render(request, 'home.html')


