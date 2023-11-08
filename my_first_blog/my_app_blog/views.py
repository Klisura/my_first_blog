from django.shortcuts import render
from . models import Post
from django.views.generic import ListView
# Create your views here.
def home(request):
    return render(request, 'my_app_blog/base.html')

def about(request):
    return render(request, 'my_app_blog/about.html')

class PostList(ListView):
    model = Post

