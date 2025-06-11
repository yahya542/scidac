from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


class StudySession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    topic= models.CharField(max_length=200, default = "topik harus diisi")
    duration_minutes = models.IntegerField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.topic}"

class StudyCapsule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    topic = models.CharField(max_length=255, default="topik harus diisi")
    question = models.TextField(default="Pertanyaan akan dihasilkan oleh AI")
    correct_answer =   models.TextField(blank=True, null=True)
    user_answer = models.CharField(max_length=255, blank=True, null=True)
    is_correct = models.BooleanField(default=False)
    unlock_next_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)  

   