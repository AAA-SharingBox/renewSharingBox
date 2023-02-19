# Generated by Django 4.1.3 on 2022-11-17 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folder', '0002_folder_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='最終更新日'),
        ),
        migrations.AlterField(
            model_name='folder',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='作成日'),
        ),
    ]