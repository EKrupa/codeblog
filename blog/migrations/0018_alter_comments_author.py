# Generated by Django 4.2.16 on 2024-10-26 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_comments_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='author',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
