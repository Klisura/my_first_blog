from django.urls import path
from . import views


urlpatterns = [
    path('', views.base, name='base'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('home/', views.home, name='home'),
    path('posts/', views.ListView.as_view(), name='post_list'),
    path('topic/', views.TopicView.as_view(), name='topic'),
    path('form/', views.form_example, name='form'),
]
