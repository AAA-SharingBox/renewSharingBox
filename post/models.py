from django.db import models

from django.conf import settings
import uuid
from django.core.validators import URLValidator #URLのバリデータを設定する関数をインポート
from folder.models import Folder
# Create your models here.

class Post(models.Model):

    #投稿をできるリンクはhttpとhttpsのみ
    UrlValidator = URLValidator(
        schemes = ('http', 'https')
    )

    #プライマリーキーはどのモデルでもuuidを使用する
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    #URLfieldにバリデータを設定するとデフォルトのバリデータへの追加での設定になってしまうので、CharFieldを使用する。
    url = models.CharField('リンク', validators=[UrlValidator], max_length=500, blank=False, null=False)

    #リンクについての説明
    description = models.TextField('説明', max_length=300, blank=True, null=False)

    #投稿者
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='投稿者', on_delete=models.CASCADE, blank=False, null=False)

    #投稿日
    created_at = models.DateTimeField('投稿日', auto_now_add=True)

    #ipアドレス
    ip_address = models.GenericIPAddressField('IPアドレス', protocol='both', blank=False, null=False)

    #所属するフォルダー
    folder = models.ForeignKey(Folder, verbose_name='フォルダ', on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return f"{self.created_by.username} {self.created_at.strftime('%Y/%m/%d %H:%M:%S')}"