from django.urls import path
from .views import CourseListCreateAPIView, CourseDetailAPIView

urlpatterns = [
    path('courses/', CourseListCreateAPIView.as_view(), name='course-list-create'),  # List and create courses
    path('courses/<int:course_id>/', CourseDetailAPIView.as_view(), name='course-detail'),  # Retrieve, update, or delete
]
