from django.db import models

# Create your models here.
'''
content
'''

class Article(models.Model):
    content = models.TextField(blank=False)

    def __str__(self):
        return self.content