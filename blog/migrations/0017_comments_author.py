# Generated by Django 4.2.16 on 2024-10-26 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_remove_comments_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='author',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
