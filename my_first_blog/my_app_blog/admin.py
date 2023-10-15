from django.contrib import admin
from . import models


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created','updated',)
    list_filter = ('created',)
    search_fields = ('title',)


class TopicAdmin(admin.ModelAdmin):
    list_display = ('name','slug',)
    search_fields = ('name',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'created', 'updated',)
    list_filter = ('created',)



admin.site.register(models.Post,PostAdmin)
admin.site.register(models.Topic, TopicAdmin)
admin.site.register(models.Comment,CommentAdmin)
