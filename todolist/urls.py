from django.urls import path
from todolist.views import home, create, edit, delete, executor

urlpatterns = [
    path('', home),
    path('create/', create),
    path('edit/', edit),
    path('edit/<int:id>/', edit),
    path('delete/', delete),
    path('delete/<int:id>/', delete),
    path('executor/<int:executor_id>/', executor),

]
