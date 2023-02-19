from django.shortcuts import render

from django.views.generic import ListView
from folder.models import Folder

# Create your views here.
class Top(ListView):
    model = Folder
    template_name = "top/top.html"
    paginate_by = 20