# Generated by Django 4.2.9 on 2024-01-27 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0008_post_hashtags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='hashtags',
        ),
    ]
