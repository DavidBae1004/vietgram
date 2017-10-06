from django.shortcuts import render
# it makes the HTML file in here
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import models
from images import models as image_models

# 1) Create the views
# 2) Create the urls with the views
# 3) Test with admin user and anon user

# 1) Render the template with render function (line one)
# 2) Create a folder named 'static' and another named 'templates'
# 3) Add STATIC_DIRS to settings.py (look on github)
# 4) Modifie TEMPLATE DIRS on settings.py (look on github)
# 5) Add template tags to your html (look on github)

# 1) Create 'partials' folder inside of 'templates' folder
# 2) Move <nav> and <footer> to nav.html and footer.html (dont forget to load static)
# 3) Create base.html and include nav and footer and create title block and content block
# 4) Create feed.html and then extend from 'base.html' and put the <main id="feed"> inside of the content block


def index(request):
    if request.user.is_authenticated:
        images = image_models.Image.objects.all() 
        context = {
            'images' : images
        }
        return render(request, 'feed.html', context)
    else:
        response = HttpResponseRedirect(reverse('login'))
    return response



def login(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        response = HttpResponseRedirect(reverse('index'))
    return response


def explore(request):
    if request.user.is_authenticated:
        users =  models.User.objects.exclude(id=request.user.id)
        context = {
            'users': users
        }
        return render(request, 'explore.html', context)
    else:
        response = HttpResponseRedirect(reverse('login'))
    return response


def profile(request, username_from_url):
    if request.user.is_authenticated:
        profile_user = models.User.objects.get(username=username_from_url)
        context = {
            'profile_user': profile_user
        }
        return render(request, 'profile.html', context)
    else:
        response = HttpResponseRedirect(reverse('login'))
    return response