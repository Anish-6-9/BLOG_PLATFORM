from django.contrib import admin

from . models import registration, BlogPost

# Register your models here.

admin.site.register(registration)
admin.site.register(BlogPost)
