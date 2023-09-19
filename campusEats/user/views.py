# user/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from django.http import HttpResponse
from django.template import loader

def user_login(request):
    # if request.method == 'POST':
    #     form = AuthenticationForm(request, request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data.get('username')
    #         password = form.cleaned_data.get('password')
    #         user = authenticate(username=username, password=password)
    #         if user:
    #             login(request, user)
    #             messages.success(request, 'You have been successfully logged in.')
    #             return redirect('dashboard')  # Redirect to the dashboard or any other desired page
    #         else:
    #             messages.error(request, 'Invalid username or password.')
    # else:
    #     form = AuthenticationForm()
    # return render(request, 'templates/user/login.html', {'form': form})
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

