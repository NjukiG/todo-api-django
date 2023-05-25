from django.urls import path

from .views import ListTodo, DetailTodo, CreateTodoView, DeleteTodo

urlpatterns = [
    path("<int:pk>/", DetailTodo.as_view(), name="todo_detail"),
    path("", ListTodo.as_view(), name="todo_list"),
    path('create/', CreateTodoView.as_view(), name='create-todo'),
    path('delete/<int:pk>/', DeleteTodo.as_view(), name='delete_todo'),


]