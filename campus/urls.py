from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lecture/', include('apps.lecture.urls')),
    path('batch/', include('apps.batch.urls')),
    path('course/', include('apps.course.urls')),
    path('user/', include('apps.user.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
