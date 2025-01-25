from django.urls import path
from .views import TopicListCreateAPIView, TopicDetailAPIView

urlpatterns = [
    # CRUD for Topics
    path('topics/', TopicListCreateAPIView.as_view(), name='topic-list-create'),
    path('topics/<int:topic_id>/', TopicDetailAPIView.as_view(), name='topic-detail'),
]
