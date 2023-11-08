

from django.views import View

from django.shortcuts import render
# Create your views here.
#def home(request):


def base(request):
    return render(request, 'my_app_blog/base.html')


class AboutView(View):
    def get (self,request):
        return render(request, 'my_app_blog/about.html')



def home(request):
    return render(request, 'my_app_blog/home.html', {'message': 'Hello world!'})

class ListView(View):
    def get (self,request):
        return render(request, 'my_app_blog/post_list.html')