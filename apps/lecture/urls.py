from django.urls import path 
from .views import ClassLectureFileView, RawClassLectureFileView, VideoLectureView, RawVideoLectureView 

urlpatterns = [
    path('video-lectures/<int:pk>/', VideoLectureView.as_view(), name='video-lecture-list'),
    path('video-lectures/', RawVideoLectureView.as_view(), name='video-lecture-create'),
    path('class-lecture/<int:pk>/', ClassLectureFileView.as_view(), name='class-lecture-file-list'),
    path('class-lecture/', RawClassLectureFileView.as_view(), name='class-lecture-file-create'),
]
