from django.views import View
from django.shortcuts import render
from . import forms, models

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

class TopicView(View):
    def get (self,request):
        return render(request, 'my_app_blog/topic.html')


def form_example(request):
    # Create an instance of the form
    form = forms.NameForm()
    # Render the form and pass it into the context
    return render(request, 'my_app_blog/form.html', context={'form': form})

