from django.contrib import admin
from blog.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
      list_display=['id', 'title', 'content']

class ComAdmin(admin.ModelAdmin):
      list_display=['post', 'message', 'author']



admin.site.register(Post, PostAdmin)
admin.site.register(Comment, ComAdmin)


# Register your models here.
