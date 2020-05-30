from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
posts = [

        {
            "author": "Swapnil",
            "title" : "Post 1",
            "content" : "First Post Yay!!!",
            "date_posted": "May 29th 2020"
        },

        
        {
            "author": "Acharya",
            "title" : "Post 2",
            "content" : "Second Post Yay!!!",
            "date_posted": "May 30th 2020"
        }
    ]



def index(request):
    return render(request,"blog/index.html")



def home(request):
    context = {
            "posts": posts
        }
    return render(request,"blog/home.html",context)


