from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import UserProfile
from .serializer import UserProfileSerializer
from apps.user import serializer

class UserProfileView(APIView):
    def get(self, request):
        profiles = UserProfile.objects.all()
        serializer = UserProfileSerializer(profiles, many=True)
        if not serializer.data:
            return Response({"message": "No user profiles found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request):
        pk = request.data.get('id')
        try:
            profile = UserProfile.objects.get(pk=pk)
            serializer = UserProfileSerializer(profile, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except UserProfile.DoesNotExist:
            return Response({"message": "User profile not found."}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request):
        pk = request.data.get('id')
        try:
            profile = UserProfile.objects.get(pk=pk)
        except UserProfile.DoesNotExist:
            return Response({"message": "User profile not found."}, status=status.HTTP_404_NOT_FOUND)
        
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data={"message": "User profile deleted successfully."})
    


class SupportiveAuthView(APIView):
    def get(self, request):
        return Response({"message": "Supportive authentication endpoint is operational."}, status=status.HTTP_200_OK)
    
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        profile = UserProfile.objects.filter(email=email, password=password).first()
        if profile:
            serializer = UserProfileSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "Invalid email or password."}, status=status.HTTP_401_UNAUTHORIZED)
