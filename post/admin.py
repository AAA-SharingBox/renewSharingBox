from django.contrib import admin

from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    # 管理画面の表示項目
    #readonly_fields = ( "created_at", "created_by", "ip_address", "url", "description" )
    #管理画面では投稿日が新しいものから表示する
    ordering = ("-created_at", "created_by")

admin.site.register(Post, PostAdmin)