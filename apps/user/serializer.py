from rest_framework import serializers

from .models import UserProfile , BulkUserUpload


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class BulkUserUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulkUserUpload
        fields = '__all__'