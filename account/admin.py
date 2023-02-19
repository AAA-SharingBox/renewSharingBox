from django.contrib import admin

from .models import MyUser
# Register your models here.


class MyUserAdmin(admin.ModelAdmin):
    # 管理画面の表示項目
    exclude = ("password", "groups", "user_permissions")
    fields = ( "last_login", "email", "username", "nickname", "icon", "introduction", "is_active", "is_staff", "is_superuser")

admin.site.register(MyUser, MyUserAdmin)