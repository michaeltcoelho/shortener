#encoding:utf-8
from django.shortcuts import render
from django.conf import settings
from django.http import (HttpResponseRedirect, HttpResponse, Http404)
from django.db.models import F
from django.core.urlresolvers import reverse as r
from django.contrib import auth

from .forms import UserCreationForm, AuthenticationForm, LinkForm
from .models import User, Link, UserLink

from .converter import base62

import json


def home(request):
    """
    home - app home
    """
    if request.user.is_authenticated():
        user_links = UserLink.objects.filter(user=request.user) \
                                .select_related() \
                                .order_by('-visits')
    else:
        user_links = None

    context = {
        'user_links' : user_links,
        'base_url' : settings.BASE_URL
    }

    return render(request, 'index.html', context)


def login(request,
          login_form=AuthenticationForm,
          template='register/login.html'):
    """
    login - login the user
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
    signup - enrolls a new user
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
    shorten - an ajax view to shorten an url
    """
    if request.is_ajax():
        form = link_form(request.GET)
        user = request.user if request.user.is_authenticated() else None
        context = {}

        if form.is_valid():

            link, created = Link.objects.get_or_create(url=form.cleaned_data.get('url'))

            if user:
                user_link, ul_created = UserLink.objects.get_or_create(user=user, link=link)
                context.update({
                    'visits' : user_link.visits,
                    'created' : ul_created
                })

            context.update({
                'url'  : link.url,
                'submitted' : link.submitted.strftime('%d/%m/%Y %H:%m'),
                'shortened_url' : link.get_shortened_url()
            })

            return HttpResponse(json.dumps(context), content_type='application/json')

        return HttpResponse(json.dumps({ 'error' : form.errors }), content_type='application/json')


def redirect(request, uid):
    """
    redirect - redirect the user permanently to the original link
    """
    uid = base62.to_decimal(uid)

    try:
        link = Link.objects.get(id=uid)

        if request.user.is_authenticated():
            user_link = UserLink.objects.get(user=request.user, link=link)
            user_link.visits = F('visits') + 1
            user_link.save()

    except Link.DoesNotExist:
        raise Http404()

    return HttpResponseRedirect(link.url)


def error404(request):
    """
    error404 - show 404 custom error page
    """
    return render(request, '404.html')