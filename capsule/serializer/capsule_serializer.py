from rest_framework import serializers
from capsule.models.capsule_models import StudyCapsule

class StudyCapsuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyCapsule
        fields = '__all__'
        read_only_fields = ['id', 'question', 'correct_answer', 'created_at', 'user_answer', 'is_correct', 'unlock_next_at', 'user']


class CapsuleAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyCapsule
        fields = ['user_answer', 'is_correct', 'unlock_next_at']
        read_only_fields = ['is_correct', 'unlock_next_at']
