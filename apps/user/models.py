from django.db import models



class UserProfile(models.Model):
    user_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user_name
    

class BulkUserUpload(models.Model):
    file = models.FileField(upload_to='bulk_uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bulk upload at {self.uploaded_at}"
