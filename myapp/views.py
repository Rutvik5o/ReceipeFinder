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

