from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, 
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)

# Create your views here.



def home(request):
    context = {
            "title": "Home",
            "posts": Post.objects.all()
        }
    return render(request,"blog/home.html",context)



class PostListView(ListView):
    model = Post
    #by defaul the postlistview looks for template in format <app>/<model>_<viewtype>.html
    #for example: blog/post_list.html

    #override the default template for this listview
    template_name = "blog/home.html"
    context_object_name = "posts" #from the context passed in home function
    ordering = ["-date_posted"] #the - in "-date_posted" reverses the list


class PostDetailView(DetailView):
    model = Post
    #by defaul the postlistview looks for template in format <app>/<model>_<viewtype>.html
    #for example: blog/post_list.html



class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ["title","content"]
    #by defaul the postlistview looks for template in format <app>/<model>_<viewtype>.html
    #for example: blog/post_list.html

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ["title","content"]
    #by defaul the postlistview looks for template in format <app>/<model>_<viewtype>.html
    #for example: blog/post_list.html

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if(self.request.user == post.author):
            return True
        return False




class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    #by defaul the postlistview looks for template in format <app>/<model>_<viewtype>.html
    #for example: blog/post_list.html
    
    sucess_url = "/"

    def test_func(self):
        post=self.get_object()
        if(self.request.user == post.author):
            return True
        return False

def about(request):
    return render(request,"blog/about.html")


