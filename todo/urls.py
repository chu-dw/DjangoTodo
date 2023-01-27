from django import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
]