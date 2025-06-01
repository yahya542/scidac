import os
from django.shortcuts import render
from rest_framework import generics, permissions
from study.models.capsule_models import StudyCapsule
from study.serializer.capsule_serializer import StudyCapsuleSerializer

def capsule(request):
    return render(request, 'capsule/capsule.html')

class ListCreateView(generics.ListCreateAPIView):
    serializer_class = StudyCapsuleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return StudyCapsule.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudyCapsuleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return StudyCapsule.objects.filter(user=self.request.user)

   