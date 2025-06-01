from django.shortcuts import render
from rest_framework import generics, permissions
from study.models.capsule_models import StudyCapsule
from study.serializer.capsule_serializer import StudyCapsuleSerializer
from ..utils.ai import generate_question

# Tampilan HTML (jika ada template)
def capsule(request):
    return render(request, 'capsule/capsule.html')

# Endpoint: List + Create Capsule
class ListCreateView(generics.ListCreateAPIView):
    serializer_class = StudyCapsuleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return StudyCapsule.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        topic = self.request.data.get('topic')
        if topic:
            question, answer = generate_question(topic)
            serializer.save(user=self.request.user, topic=topic, question=question, correct_answer=answer)
        else:
            serializer.save(user=self.request.user)

# Endpoint: Detail, Update, Delete
class DetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudyCapsuleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return StudyCapsule.objects.filter(user=self.request.user)
