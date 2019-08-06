from django.shortcuts import render

from .models import Post
from django.views.generic import ListView, DetailView
from django.http import HttpResponse

class PostsListView(ListView): # представление в виде списка
    model = Post                   # модель для представления


class PostDetailView(DetailView): # детализированное представление модели
    model = Post

def go(request):
    return HttpResponse("<h2>Главная</h2>")