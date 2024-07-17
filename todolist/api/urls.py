from django.urls import path

from .views import TodoList, TodoDetail

urlpatterns = [
    path('api/v1/todos/', TodoList.as_view(), name='todo_list'),
    path('api/v1/todos/<int:pk>/', TodoDetail.as_view(), name='todo_detail'),
]
