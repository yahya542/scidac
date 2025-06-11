from rest_framework import generics, permissions
from capsule.models.capsule_models import StudySession
from capsule.serializer.session_serializer import StudySessionSerializer


class StudySessionListCreateView(generics.ListCreateAPIView): #bawaan drf
    serializer_class = StudySessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Hanya menampilkan sesi belajar milik user yang sedang login
        return StudySession.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        # Saat create, otomatis assign user yg login
        serializer.save(user=self.request.user)

class StudySessionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudySessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Hanya menampilkan sesi belajar milik user yang sedang login
        return StudySession.objects.filter(user=self.request.user)
    
    def perform_update(self, serializer):
        # Saat update, tetap assign user yg login
        serializer.save(user=self.request.user)