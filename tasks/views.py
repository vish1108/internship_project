from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


#List & Create task
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    


    def get_queryset(self):
        return Task.objects.filter(user = self.request.user)
    

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    

# Retrieve, Update, Delete task
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]



    def get_queryset(self):
        return Task.objects.filter(user = self.request.user)
    

class RecentCompletedTasksView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.completed_last_week(request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    

    

    
