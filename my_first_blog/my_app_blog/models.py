from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.TextField()

    def __str__(self):
        return self.name

STATUS = ((0, "Draft"),(1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=255, null=False, blank="False")
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post")
    topics = models.ManyToManyField(Topic, blank=True)
    slug = models.SlugField(max_length=255, null=False, blank=False, unique=True, default='')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def save(self, *args, **keyargs):
        self.slug = slugify(self.title)
        super().save(*args, **keyargs)
class Meta:
    ordering = ['- created']





class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=70,blank=True)
    approved = models.BooleanField(default=False)
    def __str__(self):
        return self.name
