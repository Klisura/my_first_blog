from django.db import models
from django.contrib.auth.models import User
# Create your models here.


STATUS = ((0, "Draft"),(1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=255, null=False, blank="False")
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post")


    def __str__(self):
        return self.title + ' | ' + str(self.author)

class Meta:
    ordering = ['- created']


class Topic(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    slug = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=70,blank=True)

    def __str__(self):
        return self.name
