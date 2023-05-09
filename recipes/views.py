from django.shortcuts import render
from django.http import HttpResponse
from recipes.models import Recipe

# Create your views here.
def home(request):
   recipes = Recipe.objects.all().order_by('-id')
   return render(request, 'recipes/pages/home.html', context={'recipes':recipes})
