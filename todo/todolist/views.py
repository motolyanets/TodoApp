from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article


def home(request):
    posts = Article.objects.all()
    return render(request, 'todolist/home.html', {'posts': posts})


def create(request):
    if request.method == 'POST':
        todo = Article()
        todo.content = request.POST.get('todo')
        todo.save()
    return HttpResponseRedirect("/")


def edit(request, id):
    todo = Article.objects.get(id=id)

    if request.method == 'POST':
        todo.content = request.POST.get('todo')
        todo.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, 'todolist/edit.html', {'todo': todo})


def delete(request, id):
    todo = Article.objects.get(id=id)
    todo.delete()
    return HttpResponseRedirect("/")
