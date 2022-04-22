from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article


def home(request):
    posts = Article.objects.all()
    return render(request, 'todolist/home.html', {'posts': posts})


def create(request):
    if request.method == 'POST':
        Article.objects.create(content=request.POST.get('todo'))
    return HttpResponseRedirect("/")


def edit(request, id):
    todo = Article.objects.filter(id=id)

    if request.method == 'POST' and todo.exists():
        todo.update(content=request.POST.get('todo'))
        return HttpResponseRedirect("/")
    else:
        return render(request, 'todolist/edit.html', {'todo': todo.first()})


def delete(request, id):
    Article.objects.filter(id=id).first().delete()
    return HttpResponseRedirect("/")
