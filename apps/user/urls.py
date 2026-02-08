from django.urls import path 
from .views import UserProfileView, SupportiveAuthView , BulkUserView

urlpatterns = [
    path('profiles/', UserProfileView.as_view(), name='user-profiles'),
    path('supportive-auth/', SupportiveAuthView.as_view(), name='supportive-auth'),
    path('bulk-user/', BulkUserView.as_view(), name='bulk-user'),
]
