#encoding:utf-8
from django.shortcuts import render
from django.conf import settings
from django.http import (HttpResponseRedirect, HttpResponse,
                         Http404, HttpResponsePermanentRedirect)
from django.core.urlresolvers import reverse as r
from django.contrib import auth

from .forms import UserCreationForm, AuthenticationForm, LinkForm
from .models import User, Link

from .converter import base62

import json

def home(request):
    """
    home - app home
    """
    if request.user.is_authenticated():
        links = Link.objects.filter(user=request.user)
    else:
        links = None

    context = {
        'links' : links,
        'base_url' : settings.BASE_URL
    }

    return render(request, 'index.html', context)

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

            User.objects.create_user(name=data.get('name'),
                                     email=data.get('email'),
                                     password=data.get('password'))

            user = auth.authenticate(email=data.get('email'), password=data.get('password'))

            if user:
                auth.login(request, user)

            return HttpResponseRedirect(r('core:home'))

        return render(request, template, { 'form' : form })
    return render(request, template, { 'form' : signup_form() })


def shorten(request,
          link_form=LinkForm):
    """
    short - an ajax view to shorten an url
    """
    if request.is_ajax():

        data = request.GET
        form = link_form(data)

        user = request.user if request.user.is_authenticated() else None
        created = False

        if form.is_valid():

            try:

                link = Link.objects.get(url=form.cleaned_data.get('url'))

                if user is not None and link.user is not user:
                    link.user.add(user)
                    link.save()

            except Link.DoesNotExist:

                link, created = Link.objects.create(url=form.cleaned_data.get('url')), True

                if user:
                    link.user.add(user)
                    link.save()

            link_json = link.to_json()

            link_json['created'] = created

            return HttpResponse(
                json.dumps(link_json),
                content_type='application/json'
            )

        return HttpResponse(
            json.dumps({ 'error' : form.errors }),
            content_type='application/json'
        )

def redirect(request, id):
    """
    redirect - redirect the user permanently to the original link
    """
    id = base62.to_decimal(id)

    try:
        link = Link.objects.get(id=id)
    except Link.DoesNotExist:
        raise Http404()

    link.visits += 1
    link.save()

    return HttpResponsePermanentRedirect(link.url)

def error404(request):
    """
    error404 - show 404 custom error page
    """
    pass