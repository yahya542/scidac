
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class StudySession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    topic = models.CharField(max_length=200)
    duration_minutes = models.IntegerField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.topic}"

class StudyCapsule(models.Model):
   class Capsule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=255)
    question = models.TextField()
    correct_answer = models.CharField(max_length=255)
    user_answer = models.CharField(max_length=255, blank=True, null=True)
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def check_answer(self):
        return self.user_answer and self.user_answer.strip().lower() == self.correct_answer.strip().lower()
    def save(self, *args, **kwargs):
        # Set waktu unlock capsule berikutnya jika jawabannya benar
        if self.user_answer:
            self.is_correct = self.check_answer()
            if self.is_correct:
                self.unlock_next_at = timezone.now() + timedelta(days=1)
        super().save(*args, **kwargs)