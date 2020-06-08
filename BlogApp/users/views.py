from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.
def register(request):
    if(request.method == "POST"):
        form = UserRegisterForm(request.POST)

        if(form.is_valid()):
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request,f"Account created for {username}!")
            return redirect("blog-home")

    form = UserRegisterForm()
    context = {"title":"Registration","form":form}
    return render(request,"users/register.html",context)





#messages
#message.debug
#message.info
#message.sucess
#message.warning
#message.error