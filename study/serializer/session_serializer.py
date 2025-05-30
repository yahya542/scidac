from rest_framework import serializers
from study.models import StudySession


class StudySessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudySession
        fields = ['id', 'user', 'subject', 'topic', 'duration_minutes', 'completed', 'created_at']
        read_only_fields = ['id', 'created_at']