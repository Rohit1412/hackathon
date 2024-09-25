from rest_framework.routers import DefaultRouter
from .views import VideoUploadViewSet, AIAnalysisViewSet
from django.urls import path
from .views import VideoUploadView

router = DefaultRouter()
router.register(r'videos', VideoUploadViewSet)
router.register(r'analysis', AIAnalysisViewSet)

urlpatterns = router.urls


urlpatterns = [
    path('videos/', VideoUploadView.as_view(), name='video-upload'),  # Add this route for video uploads
]
