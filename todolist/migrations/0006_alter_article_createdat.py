# Generated by Django 4.0.4 on 2022-04-28 18:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_alter_article_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 28, 21, 58, 13, 331496)),
        ),
    ]
