from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse as r
from django.contrib import auth
from .forms import UserCreationForm, AuthenticationForm, LinkForm
from .models import User

import json

def home(request):
    """
    home - app home
    """
    return render(request, 'index.html')

def login(request,
          login_form=AuthenticationForm,
          template='register/login.html'):
    """
    login - login the user on app
    """
    if request.method == "POST":

        data = request.POST
        form = login_form(data or None)

        if form.is_valid():

            auth.login(request, form.get_user())

            return HttpResponseRedirect(r('core:home'))

        return render(request, template, { 'form' : form })

    return render(request, template, { 'form' : login_form() })

def logout(request):
    """
    logout - logout user from app
    """
    auth.logout(request)

    return HttpResponseRedirect(r('core:home'))

def signup(request,
           signup_form=UserCreationForm,
           template='register/signup.html'):
    """
    signup - sign up an user on web app
    """
    if request.method == "POST":

        data = request.POST
        form = signup_form(data or None)

        if form.is_valid():

            User.objects.create_user(name=data.get('name'), email=data.get('email'), password=data.get('password'))

            user = auth.authenticate(email=data.get('email'), password=data.get('password'))

            if user:
                auth.login(request, user)

            return HttpResponseRedirect(r('core:home'))

        return render(request, template, { 'form' : form })
    return render(request, template, { 'form' : signup_form() })


def shortenit(request,
              link_form=LinkForm):
    """
    shortenit - an ajax view to shorten an url
    """
    if request.is_ajax():

        form = link_form(request.POST)

        if form.is_valid():
            link = form.save()
            link.user = request.user if request.user.is_authenticated() else None
            link.save()
            return HttpResponse({ 'url' : link.get_shortened_url() }, content_type='application/json')
        return HttpResponse(json.dumps(form.errors), content_type='application/json')

def redirect(request, id):
    """
    redirect -
    """
    return HttpResponseRedirect(r('core:home'))