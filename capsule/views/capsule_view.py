from django.shortcuts import render
from rest_framework import generics, permissions
from capsule.models.capsule_models import StudyCapsule
from capsule.serializer.capsule_serializer import StudyCapsuleSerializer, CapsuleAnswerSerializer
from ..utils.ai import ai_response, check_answer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import get_object_or_404
from myapp.models import Profile


def capsule(request):
    return render(request, 'capsule.html')


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

            profile, created = Profile.objects.get_or_create(user=request.user)
            profile.points += 10
            profile.save()

        capsule.save()

        profile = Profile.objects.get(user=request.user)

        return Response({
            "question": capsule.question,
            "your_answer": user_answer,
            "correct": is_correct,
            "feedback": feedback,
            "current_points": profile.points
        }, status=200)
