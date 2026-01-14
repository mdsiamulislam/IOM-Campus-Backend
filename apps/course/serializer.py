from rest_framework import serializers

from apps.user.models import UserProfile
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    # Read student names instead of IDs
    students = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'name', 'sort_name', 'description', 'is_active', 'start_date', 'end_date', 'students']

    def get_students(self, obj):
        return [{"id": student.id, "name": student.name} for student in obj.students.all()]

