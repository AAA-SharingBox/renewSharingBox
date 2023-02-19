from django.db import models
from django.conf import settings
import uuid
# Create your models here.
class Folder(models.Model):

    #プライマリーキーはどのモデルでもuuidを使用する
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    #フォルダ名
    name = models.CharField(verbose_name="フォルダ名", max_length=100, blank=False, null=False)

    #どんなリンク集なのかの説明
    description = models.TextField('コメント', max_length=300, blank=True)

    #作成者
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作成者', on_delete=models.CASCADE, blank=False, null=False)
    
    #作成日
    created_at = models.DateTimeField('作成日', auto_now_add=True)

    #最終更新日
    updated_at = models.DateTimeField('最終更新日', auto_now=True)

    def __str__(self):
        return self.name