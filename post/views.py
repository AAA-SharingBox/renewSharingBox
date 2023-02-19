from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views.generic import (ListView,
                                  CreateView,
                                  DeleteView,
                                  UpdateView)
from .models import Post
from SharingBox.libraries import get_client_ip

# Create your views here.
class PostCreateView(CreateView, LoginRequiredMixin):

    #Companyテーブル連携
    model = Post

    #入力項目定義
    fields = ("url", "description")

    #テンプレートファイル指定
    template_name = "post/create_post.html"

    #記録処理
    def form_valid(self, form):
        post = form.save(commit=False)
        post.created_by = self.request.user
        post.ip_address = get_client_ip(self.request)
        form.save(commit=True)
        return redirect("signup")

