from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from models.models import Session
from .serializers import SessionSerializer  # Assuming you have a serializer for Session
from AI.Prompts.learning_outcomes import create_learning_outcomes_prompt
from AI.genrate_response import OpenAIClient


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from models.models import Course, Topic


class GenerateLearningOutcomesAPIView(APIView):
    """
    Endpoint to generate learning outcomes based on course ID, topic ID, session name, and reading material.

    Example Input (POST):
    {
        "course_id": 1,
        "topic_id": 1,
        "session_name": "Introduction to Django",
        "reading_material": "## Django Overview\nDjango is a web framework."
    }

    Example Output:
    {
        "learning_outcomes": "By the end of this session, the learner will be able to..."
    }
    """

    def post(self, request):
        course_id = request.data.get("course_id")
        topic_id = request.data.get("topic_id")
        session_name = request.data.get("session_name")
        reading_material = request.data.get("reading_material")

        # Check if all required fields are provided
        if not all([course_id, topic_id, session_name, reading_material]):
            return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve course and topic using IDs
        course = get_object_or_404(Course, course_id=course_id)
        topic = get_object_or_404(Topic, topic_id=topic_id)

        # Generate prompt using course name, topic name, session name, and reading material
        prompt = create_learning_outcomes_prompt(
            course_name=course.course_name,
            topic_name=topic.topic_name,
            session_name=session_name,
            reading_material=reading_material
        )

        # Generate learning outcomes by calling the OpenAI client
        openai_client = OpenAIClient()
        learning_outcomes = openai_client.generate_response(prompt)

        return Response({"learning_outcomes": learning_outcomes}, status=status.HTTP_200_OK)



class SessionListCreateAPIView(APIView):
    """
    Handles GET (list all sessions) and POST (create a session).

    Endpoints:
    - GET /api/sessions/
        Input: None
        Output: List of all sessions with their details.
    - POST /api/sessions/
        Input: JSON body with 'session_name', 'topic', 'outcomes', and 'reading_material'.
        Output: Created session details.

    Example Input (POST):
    {
        "session_name": "Introduction to Django",
        "topic": 1,
        "outcomes": "Learn the basics of Django.",
        "reading_material": "## Django Overview\nDjango is a web framework."
    }

    Example Output (GET/POST):
    [
        {
            "session_id": 1,
            "session_name": "Introduction to Django",
            "topic": 1,
            "outcomes": "Learn the basics of Django.",
            "reading_material": "## Django Overview\nDjango is a web framework."
        }
    ]
    """

    def get(self, request):
        sessions = Session.objects.all()
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SessionDetailAPIView(APIView):
    """
    Handles GET, PUT, and DELETE operations for a specific session by ID.

    Endpoints:
    - GET /api/sessions/<int:session_id>/
        Input: session_id (path parameter)
        Output: Details of the specified session.

    - PUT /api/sessions/<int:session_id>/
        Input: session_id (path parameter), JSON body with updated details.
        Output: Updated session details.

    - DELETE /api/sessions/<int:session_id>/
        Input: session_id (path parameter)
        Output: Success or error message.

    Example Input (PUT):
    {
        "session_name": "Updated Session Name",
        "topic": 1,
        "outcomes": "Updated outcomes.",
        "reading_material": "## Updated Material"
    }

    Example Output (GET/PUT):
    {
        "session_id": 1,
        "session_name": "Updated Session Name",
        "topic": 1,
        "outcomes": "Updated outcomes.",
        "reading_material": "## Updated Material"
    }

    Example Output (DELETE):
    {
        "message": "Session deleted successfully"
    }
    """

    def get(self, request, session_id):
        try:
            session = Session.objects.get(pk=session_id)
            serializer = SessionSerializer(session)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Session.DoesNotExist:
            return Response({"error": "Session not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, session_id):
        try:
            session = Session.objects.get(pk=session_id)
            serializer = SessionSerializer(session, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Session.DoesNotExist:
            return Response({"error": "Session not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, session_id):
        try:
            session = Session.objects.get(pk=session_id)
            session.delete()
            return Response({"message": "Session deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Session.DoesNotExist:
            return Response({"error": "Session not found"}, status=status.HTTP_404_NOT_FOUND)
