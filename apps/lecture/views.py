from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from .models import ClassLectureFile, VideoLecture
from .serializer import VideoLectureSerializer, ClassLectureFileSerializer, RawVideoLectureSerializer , RawClassLectureFileSerializer



class VideoLectureView(APIView):

    def get(self, request, pk):
        lectures = VideoLecture.objects.filter(course = pk)
        if not lectures.exists():
            return Response({"error": "VideoLecture not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = VideoLectureSerializer(lectures, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def patch(self, request, pk):
        try:
            lecture = VideoLecture.objects.get(pk=pk)
        except VideoLecture.DoesNotExist:
            return Response({"error": "VideoLecture not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = VideoLectureSerializer(lecture, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            lecture = VideoLecture.objects.get(pk=pk)
        except VideoLecture.DoesNotExist:
            return Response({"error": "VideoLecture not found."}, status=status.HTTP_404_NOT_FOUND)
        lecture.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data={"message": "VideoLecture deleted successfully."})
    

class RawVideoLectureView(APIView):

    def get(self, request):
        lectures = VideoLecture.objects.all()
        serializer = RawVideoLectureSerializer(lectures, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RawVideoLectureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    











## ---------------------- ClassLectureFile Views ---------------------- ##
class ClassLectureFileView(APIView):

    def get(self, request, pk):
        files = ClassLectureFile.objects.filter(course = pk)
        if not files.exists():
            return Response({"error": "ClassLectureFile not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ClassLectureFileSerializer(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def patch(self, request, pk):
        try:
            lecture_file = ClassLectureFile.objects.get(pk=pk)
        except ClassLectureFile.DoesNotExist:
            return Response({"error": "ClassLectureFile not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ClassLectureFileSerializer(lecture_file, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data = {"message": "ClassLectureFile updated successfully.", "data": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            lecture_file = ClassLectureFile.objects.get(pk=pk)
        except ClassLectureFile.DoesNotExist:
            return Response({"error": "ClassLectureFile not found."}, status=status.HTTP_404_NOT_FOUND)
        lecture_file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data={"message": "ClassLectureFile deleted successfully."})
    
class RawClassLectureFileView(APIView):
    parser_classes = [MultiPartParser, FormParser]


    def get(self, request):
        files = ClassLectureFile.objects.all()
        serializer = RawClassLectureFileSerializer(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        print(request.data)  # you can see both files and other fields
        serializer = RawClassLectureFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)