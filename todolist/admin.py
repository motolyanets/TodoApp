from django.contrib import admin
from .models import Article, Executors


admin.site.register(Article)
admin.site.register(Executors)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'createdAt')


class ExecutorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')