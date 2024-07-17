from rest_framework import generics
from rest_framework.pagination import CursorPagination
from .permissions import IsOwnerOnly
from .serializers import TodoSerializer
from todo.models import Todo

class TodoCursorPagination(CursorPagination):
    ordering = 'id'
    page_size = 2
class TodoList(generics.ListCreateAPIView):
    pagination_class = TodoCursorPagination
    permission_classes = (IsOwnerOnly,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def filter_queryset(self, queryset):
        queryset = queryset.filter(user=self.request.user.id)
        return super().filter_queryset(queryset)

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    # Restrict access only to admin users
    permission_classes = (IsOwnerOnly,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
