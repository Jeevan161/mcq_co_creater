from rest_framework import serializers
from models.models import Topic

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['topic_id', 'topic_name', 'course']
