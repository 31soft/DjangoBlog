from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post # наша модель из blog/models.py

admin.site.register(Post)