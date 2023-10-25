from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'my_app_blog/base.html')

def about(request):
    return render(request, 'my_app_blog/about.html')