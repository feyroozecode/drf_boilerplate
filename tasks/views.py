from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from  rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class IsOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)     
    
class TaskViewSet(viewsets.ModelViewSet):
   serialzer_class = TaskSerializer
   permission_classes = [IsAuthenticated, IsOwnerPermission]
   filter_backends = [DjangoFilterBackend, SearchFilter]
   filterset_fields = ['completed', 'due_date']
   search_fields = ['title', 'description']
   
   # Ensure users can only access their own tasks
   def get_queryset(self):
       return Task.objects.filter(user=self.request.user)
   
   def perform_create(self, serializer):
       serializer.save(user=self.request.user)