from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from models.models import Course
from .serializers import CourseSerializer


class CourseListCreateAPIView(APIView):
    """
    Handles GET (list all courses) and POST (create a course).
    Endpoint: /api/courses/
    """

    def get(self, request):
        """
        Retrieves the list of all courses.

        Endpoint: GET /api/courses/
        Input: None
        Output:
        [
            {
                "course_id": 1,
                "course_name": "Introduction to Python"
            },
            {
                "course_id": 2,
                "course_name": "Advanced Java"
            }
        ]
        """
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Creates a new course.

        Endpoint: POST /api/courses/
        Input:
        {
            "course_name": "New Course Name"
        }
        Output:
        {
            "course_id": 3,
            "course_name": "New Course Name"
        }
        """
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailAPIView(APIView):
    """
    Handles GET (retrieve), PUT (update), and DELETE (delete) for a specific course by ID.
    Endpoint: /api/courses/<course_id>/
    """

    def get(self, request, course_id):
        """
        Retrieves details of a specific course by its ID.

        Endpoint: GET /api/courses/<course_id>/
        Input: None
        Output:
        {
            "course_id": 1,
            "course_name": "Introduction to Python"
        }
        If the course does not exist:
        {
            "error": "Course not found"
        }
        """
        try:
            course = Course.objects.get(pk=course_id)
            serializer = CourseSerializer(course)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Course.DoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, course_id):
        """
        Updates an existing course by its ID.

        Endpoint: PUT /api/courses/<course_id>/
        Input:
        {
            "course_name": "Updated Course Name"
        }
        Output:
        {
            "course_id": 1,
            "course_name": "Updated Course Name"
        }
        If the course does not exist:
        {
            "error": "Course not found"
        }
        If the input is invalid:
        {
            "course_name": ["This field may not be blank."]
        }
        """
        try:
            course = Course.objects.get(pk=course_id)
            serializer = CourseSerializer(course, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Course.DoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, course_id):
        """
        Deletes a course by its ID.

        Endpoint: DELETE /api/courses/<course_id>/
        Input: None
        Output:
        {
            "message": "Course deleted successfully"
        }
        If the course does not exist:
        {
            "error": "Course not found"
        }
        """
        try:
            course = Course.objects.get(pk=course_id)
            course.delete()
            return Response({"message": "Course deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Course.DoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
