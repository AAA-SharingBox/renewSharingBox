from django.shortcuts import render

from django.views.generic import ListView
from post.models import Post
from .models import Folder

# Create your views here.

class Folder_detail(ListView):
    model = Post
    template_name = "folder/folder_detail.html"
    paginate_by = 20

    def get_queryset(self):
        folder_id = self.kwargs.get("id")
        return Post.objects.filter( folder__id = folder_id )