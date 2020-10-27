from django.contrib import admin
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_didplay = ("title", "description", "body", "image", "slug")


admin.site.register(Post, PostAdmin)

