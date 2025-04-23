from django.shortcuts import render
import requests

# Create your views here.

def indexpage(request):
    url = requests.get("https://dummyjson.com/recipes")
    response = url.json()
    data = response['recipes']
    print(data)

    context ={

        "data":data

    }

    return render(request,"index.html",context)
