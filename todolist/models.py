import datetime

from django.db import models

# Create your models here.
'''
content
'''

class Article(models.Model):
    content = models.TextField(blank=False)
    createdAt = models.DateTimeField(default=datetime.datetime.now())
    executor = models.ForeignKey('Executors', on_delete=models.PROTECT)

    def __str__(self):
        return self.content


class Executors(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name