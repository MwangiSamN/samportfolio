from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Portfolio

# Create your views here.

def index(request):

    home = Home.objects.all()

    about = About.objects.all()
    profiles =Profile.objects.filter(about=about)

    categories = Category.objects.all()

    portfolios = Portfolio.objects.all()

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios,
    }



    return render(request, 'index.html', context)