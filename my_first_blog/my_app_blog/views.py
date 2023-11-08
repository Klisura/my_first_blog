from django.shortcuts import render
from . models import Post
from django.views.generic import ListView
from django.views import View
from django.views.generic.base import TemplateView
from . import models
# Create your views here.
def home(request):
    return render(request, 'my_app_blog/base.html')

#def about(request):
   # return render(request, 'my_app_blog/about.html')

class PostList(ListView):
    model = Post

class AboutView(View):
    def get (self,request):
        return render(request, 'my_app_blog/about.html')

#class AboutView(TemplateView):
   # template_name = 'my_app_blog/about.html'

