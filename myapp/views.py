from django.shortcuts import render
import requests

# Create your views here.

def indexpage(request):
    url = requests.get("https://dummyjson.com/recipes")
    tags = requests.get("https://dummyjson.com/recipes/tags").json()
    response = url.json()
    data = response['recipes']
    print(data)

    context ={

        "data":data,
        "tags":tags

    }

    return render(request,"index.html",context)

def databytages(request,tag):
    response = requests.get(f"https://dummyjson.com/recipes/tag/{tag}").json()
    tags = requests.get("https://dummyjson.com/recipes/tags").json()

    data = response["recipes"]

    context = {
        "data": data,
        "tags":tags
    }

    return render(request,"index.html",context)



def mealtype(request,meal):
    response = requests.get(f"https://dummyjson.com/recipes/meal-type/{meal}").json()
    tags = requests.get("https://dummyjson.com/recipes/tags").json()

    data = response["recipes"]

    context = {
        "data": data,
        "tags":tags
    }

    return render(request,"index.html",context)

def search(request):

    userquery = request.POST.get("query")
    response = requests.get(f"https://dummyjson.com/recipes/search?q={userquery}").json()

    tags = requests.get("https://dummyjson.com/recipes/tags").json()

    data = response["recipes"]

    context = {
        "data": data,
        "tags": tags
    }

    return render(request,"index.html",context)

import requests
from django.shortcuts import render

def singlerecipe(request, id):
    # Get the current recipe
    current_recipe = requests.get(f"https://dummyjson.com/recipes/{id}").json()

    # Get all recipes
    all_recipes = requests.get("https://dummyjson.com/recipes").json()["recipes"]

    # Filter recommended recipes by cuisine, excluding the current one
    recommended = [
        recipe for recipe in all_recipes
        if recipe["cuisine"].lower() == current_recipe["cuisine"].lower() and recipe["id"] != current_recipe["id"]
    ][:3]  # Limit to 3 recommended recipes

    context = {
        "data": current_recipe,
        "recommended": recommended
    }

    return render(request, "receipes.html", context)


