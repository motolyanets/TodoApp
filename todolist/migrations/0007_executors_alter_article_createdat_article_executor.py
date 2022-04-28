# Generated by Django 4.0.4 on 2022-04-28 19:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0006_alter_article_createdat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Executors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 28, 22, 27, 57, 627447)),
        ),
        migrations.AddField(
            model_name='article',
            name='executor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='todolist.executors'),
        ),
    ]
