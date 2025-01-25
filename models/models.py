from django.db import models


class Course(models.Model):
    """
    Model representing a course.
    """
    course_id = models.AutoField(primary_key=True)  # Auto-incrementing ID
    course_name = models.CharField(max_length=255, unique=True)  # Unique course name

    def __str__(self):
        return self.course_name  # Display course name in admin panel or queries


class Topic(models.Model):
    """
    Model representing a topic linked to a specific course.
    """
    topic_id = models.AutoField(primary_key=True)  # Auto-incrementing ID
    topic_name = models.CharField(max_length=255)  # Name of the topic
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="topics")  # Link to Course model

    def __str__(self):
        return f"{self.topic_name} (Course: {self.course.course_name})"


class Session(models.Model):
    session_id = models.AutoField(primary_key=True)  # Auto-incrementing session ID
    session_name = models.CharField(max_length=255, unique=True)  # Name of the session
    topic = models.ForeignKey(Topic, related_name="sessions", on_delete=models.CASCADE)  # Linking to Topic
    outcomes = models.TextField()  # Outcomes of the session
    reading_material = models.TextField()  # Reading material in markdown format

    def __str__(self):
        return self.session_name  # Display session name in admin panel or queries
