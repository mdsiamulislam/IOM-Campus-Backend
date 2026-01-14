from django.db import models
from ..user.models import UserProfile


class Course(models.Model):
    name = models.CharField(max_length=200)
    sort_name = models.CharField(max_length=50)
    description = models.TextField()

    students = models.ManyToManyField(UserProfile, related_name='enrolled_courses', blank=True)

    is_active = models.BooleanField(default=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)  

    def __str__(self):
        return self.name
