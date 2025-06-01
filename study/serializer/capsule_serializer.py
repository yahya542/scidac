from rest_framework import serializers
from study.capsule_models import StudyCapsule


class StudyCapsuleSerializer(serializers.ModelSerializer):
     class Meta:
        model = StudyCapsule
        fields = '__all__'
        read_only_fields = ['user', 'is_correct', 'unlock_next_at', 'created_at']