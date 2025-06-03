from django.shortcuts import render
from rest_framework import generics, permissions
from study.models.capsule_models import StudyCapsule
from study.serializer.capsule_serializer import StudyCapsuleSerializer, CapsuleAnswerSerializer
from ..utils.ai import ai_response, check_answer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from datetime import timedelta




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
            question, answer = ai_response(topic)
            serializer.save(
                user=self.request.user,
                topic=topic,
                question=question,
                correct_answer=answer
            )
        else:
            serializer.save(user=self.request.user)


# Endpoint: Detail, Update, Delete
class DetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudyCapsuleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return StudyCapsule.objects.filter(user=self.request.user)


# Endpoint: Check Answer
class CapsuleAnswerAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CapsuleAnswerSerializer

    def post(self, request, pk):
        try:
            capsule = StudyCapsule.objects.get(id=pk, user=request.user)
        except StudyCapsule.DoesNotExist:
            return Response({"error": "Capsule not found"}, status=404)

        user_answer = request.data.get("user_answer")
        if not user_answer:
            return Response({"error": "user_answer is required"}, status=400)

        # Cek ke AI
        is_correct, feedback = check_answer(user_answer, capsule.correct_answer, capsule.question)


        capsule.user_answer = user_answer
        capsule.is_correct = is_correct
        if is_correct:
            capsule.unlock_next_at = timezone.now() + timedelta(days=1)
        capsule.save()

        return Response({
            "question": capsule.question,
            "your_answer": user_answer,
            "correct": is_correct,
            "feedback": feedback
        }, status=200)