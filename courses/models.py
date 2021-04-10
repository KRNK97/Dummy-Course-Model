from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    desc = models.CharField(max_length=120)
    length = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return f"title - {self.title} | lessons - {self.lessons.count()} | topics - {self.topics.count()}"


class Topic(models.Model):
    name = models.CharField(max_length=25)
    # content = models.TextField()
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="topics")

    def __str__(self):
        return f"id{- self.id} | title - {self.name} | course - {self.course.title} | lessons - {self.lessons.count()}"


class Lesson(models.Model):
    name = models.CharField(max_length=25)
    content = models.TextField()
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="lessons")
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, related_name="lessons")

    def __str__(self):
        return f"id{- self.id} | title - {self.name} | course - {self.course.title} | topic - {self.topic.name}"
