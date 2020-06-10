from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
#from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):
    if(request.method == "POST"):
        form = UserRegisterForm(request.POST)
        if(form.is_valid()):
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request,f"Account created. Pleaase Login !")
            return redirect("login")
    else:
        form = UserRegisterForm()
    context = {"title":"Registration","form":form}
    return render(request,"users/register.html",context)

#messages
#message.debug
#message.info
#message.sucess
#message.warning
#message.error


#def logInUser(request):
#    username = request.POST["username"]
#    password = request.POST["password"]
#    user = authenticate(request,username=username,password=password)
#    if user is not None:
#        login(request,user)
#        messages.sucess(request,f"You are now logged In")
#        redirect("blog-home")
#    else:
#        messages.error(request,f"PLease try agian")
#        context = {}





#def logoutUser(request):
#    logout(request)
#    return render(request,"blog/home.html",{"title":"Blog Home"})




