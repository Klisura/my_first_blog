from django.contrib import admin
from . import models


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created','updated',)
    list_filter = ('created',)


class TopicAdmin(admin.ModelAdmin):
    list_display = ('name','slug',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'created', 'updated',)
    list_filter = ('created',)


admin.site.register(models.Post,PostAdmin)
admin.site.register(models.Topic, TopicAdmin)
admin.site.register(models.Comment,CommentAdmin)
