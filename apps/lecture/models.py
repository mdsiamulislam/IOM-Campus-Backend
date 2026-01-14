from django.db import models
from ..course.models import Course


# Video Lecture Model

class VideoLecture(models.Model):
    title = models.CharField(max_length=150)
    video_url = models.CharField(max_length=255)
    course = models.ManyToManyField(Course, blank=True)
    upload_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title
    

class ClassLectureFile(models.Model):
    title = models.CharField(max_length=150)
    file = models.FileField(upload_to='lecture_files/')
    course = models.ManyToManyField(Course, blank=True)
    upload_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title
