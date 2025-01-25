from rest_framework import serializers
from models.models import Session

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['session_id', 'session_name', 'topic', 'outcomes', 'reading_material']
