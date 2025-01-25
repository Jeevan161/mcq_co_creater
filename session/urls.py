from django.urls import path
from .views import SessionListCreateAPIView, SessionDetailAPIView, GenerateLearningOutcomesAPIView

urlpatterns = [
    path('sessions/', SessionListCreateAPIView.as_view(), name='session-list-create'),
    path('sessions/<int:session_id>/', SessionDetailAPIView.as_view(), name='session-detail'),
    path('generate-learning-outcomes/', GenerateLearningOutcomesAPIView.as_view(), name='generate-learning-outcomes'),
]
