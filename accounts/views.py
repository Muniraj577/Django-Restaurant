from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.http import HttpResponseRedirect


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, 'accounts/register.html', {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, 'accounts/register.html', {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, 'accounts/register.html', {
                    'form': form,
                    'error_message': 'Password do not match.'
                })
            else:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone = form.cleaned_data['phone']
                user.save()
                auth.login(request, user)
                return redirect('frontend:index')
    else:
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('frontend:index')
        else:
            form = LoginForm(request.POST)
            if form.cleaned_data['username'] != user.username:
                messages.error(request, 'Username do not match.')
                return redirect('accounts:login')
            elif form.cleaned_data['password'] != user.password:
                messages.error(request, 'Password do not match')
                return redirect('accounts:login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('accounts:login')
