from django.shortcuts import render

from django.views.generic.list import ListView
from records.models import Post


class PostListView(ListView):

    model = Post

