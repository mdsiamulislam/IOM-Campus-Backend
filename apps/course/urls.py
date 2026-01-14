from django.urls import path 
from .views import CourseView , CourseBaseOnStudent

urlpatterns = [
    path('courses/', CourseView.as_view(), name='course-list'),
    path('courses/<int:student_id>/', CourseBaseOnStudent.as_view(), name='course-by-student'),
]
