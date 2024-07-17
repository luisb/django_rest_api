from rest_framework import generics
from .permissions import IsOwnerOnly
from .serializers import TodoSerializer
from todo.models import Todo

class TodoList(generics.ListCreateAPIView):
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
