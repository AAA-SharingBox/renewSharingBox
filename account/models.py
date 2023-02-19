from django.db import models

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.validators import MinLengthValidator
import uuid
# Create your models here.

class MyUserManager(BaseUserManager):

    def create_user(self, username, email, nickname, password):

        if not username:
            raise ValueError("Users must have an username")
        if not email:
            raise ValueError("Users must have an email address")
        if not nickname:
            raise ValueError("Users must have a nickname")
        
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            nickname = nickname
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, nickname, password):
        user = self.create_user(
            username = username,
            email = self.normalize_email(email),
            nickname = nickname,
            password = password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser, PermissionsMixin):

    #プライマリーキーはどのモデルでもuuidを使用する
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    #ユーザーID
    username = models.CharField(
        verbose_name="ユーザーID", 
        max_length=40, unique=True, 
        blank=False, 
        null=False, 
        validators=[ASCIIUsernameValidator(), MinLengthValidator(5, )]
    )
    #メールアドレス
    email = models.EmailField(verbose_name="email", max_length=100, unique=True)
    #ユーザーの表示名
    nickname = models.CharField(verbose_name="ユーザー名", max_length=100, blank=False, null=False)
    #プロフィール文
    introduction = models.TextField(verbose_name="プロフィール文", max_length=1000, blank=True, null=False)
    #アイコン画像
    icon = models.ImageField(verbose_name="アイコン", upload_to="user_icon/", blank=True, null=False, default="user_icon/default.png")
    #登録日時
    date_joined = models.DateTimeField(verbose_name="登録日", auto_now_add=True)
    #アクティブ状態
    is_active = models.BooleanField(default=True)
    
    #管理者権限
    is_staff = models.BooleanField(default=False)
    #superuser権限
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "nickname"]

    def __str__(self):
        return self.username
