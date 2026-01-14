from rest_framework import serializers

from apps.course.models import Course

from .models import ClassLectureFile, VideoLecture

class VideoLectureSerializer(serializers.ModelSerializer):
    course_info = serializers.SerializerMethodField()
    class Meta:
        model = VideoLecture
        fields =  ['id', 'title', 'video_url', 'course_info']

    def get_course_info(self, obj):
        return [{"id": course.id , "name": course.name} for course in obj.course.all()]
    
class RawVideoLectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoLecture
        fields = '__all__'










## ---------------------- ClassLectureFile Serializer ---------------------- ##



class ClassLectureFileSerializer(serializers.ModelSerializer):
    course_info = serializers.SerializerMethodField()
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), many=True)

    class Meta:
        model = ClassLectureFile
        fields = ['id', 'title', 'file', 'course', 'course_info']

    def get_course_info(self, obj):
        return [{"id": course.id, "name": course.name} for course in obj.course.all()]




class RawClassLectureFileSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), many=True)
    
    class Meta:
        model = ClassLectureFile
        fields = '__all__'
