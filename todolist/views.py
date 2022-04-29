from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Article, Executors


def home(request):
    posts = Article.objects.order_by('createdAt')
    executors = Executors.objects.order_by('name')
    return render(request, 'todolist/home.html', {'posts': posts, 'executors': executors})


def create(request):
    if request.method == 'POST':
        Article.objects.create(content=request.POST.get('todo'), executor_id=request.POST.get('executor'))
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


def executor(request, executor_id):
    posts = Article.objects.filter(executor_id=executor_id).order_by('createdAt')
    return render(request, 'todolist/executor.html', {'posts': posts})
