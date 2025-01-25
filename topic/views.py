from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from models.models import Topic, Course
from .serializers import TopicSerializer


class TopicListCreateAPIView(APIView):
    """
    Handles GET (list all topics) and POST (create a topic).

    Endpoints:
    - GET /api/topics/:
        Input: None
        Output: List of all topics with their details.
    - POST /api/topics/:
        Input: JSON body with 'topic_name' and 'course' (course_id).
        Output: Created topic details.

    Example Input (POST):
    {
        "topic_name": "Introduction to Python",
        "course": 1
    }

    Example Output (GET/POST):
    [
        {
            "topic_id": 1,
            "topic_name": "Introduction to Python",
            "course": 1
        }
    ]
    """

    def get(self, request):
        try:
            topics = Topic.objects.all()
            serializer = TopicSerializer(topics, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"An error occurred while retrieving topics: {str(e)}"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = TopicSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": f"An error occurred while creating the topic: {str(e)}"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TopicDetailAPIView(APIView):
    """
    Handles GET, PUT, and DELETE operations for a specific topic by ID.

    Endpoints:
    - GET /api/topics/<int:topic_id>/:
        Input: topic_id (path parameter)
        Output: Details of the specified topic.

    - PUT /api/topics/<int:topic_id>/:
        Input: topic_id (path parameter), JSON body with updated details.
        Output: Updated topic details.

    - DELETE /api/topics/<int:topic_id>/:
        Input: topic_id (path parameter)
        Output: Success or error message.

    Example Input (PUT):
    {
        "topic_name": "Updated Topic Name",
        "course": 1
    }

    Example Output (GET/PUT):
    {
        "topic_id": 1,
        "topic_name": "Updated Topic Name",
        "course": 1
    }

    Example Output (DELETE):
    {
        "message": "Topic deleted successfully"
    }
    """

    def get(self, request, topic_id):
        try:
            topic = Topic.objects.get(pk=topic_id)
            serializer = TopicSerializer(topic)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Topic.DoesNotExist:
            return Response({"error": "Topic not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": f"An error occurred while retrieving the topic: {str(e)}"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, topic_id):
        try:
            topic = Topic.objects.get(pk=topic_id)
            serializer = TopicSerializer(topic, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Topic.DoesNotExist:
            return Response({"error": "Topic not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": f"An error occurred while updating the topic: {str(e)}"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, topic_id):
        try:
            topic = Topic.objects.get(pk=topic_id)
            topic.delete()
            return Response({"message": "Topic deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Topic.DoesNotExist:
            return Response({"error": "Topic not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": f"An error occurred while deleting the topic: {str(e)}"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
