from rest_framework.routers import DefaultRouter
from .views import VideoUploadViewSet, AIAnalysisViewSet
from django.urls import path
from .views import VideoUploadView

# Create a router and register the ViewSets
router = DefaultRouter()
router.register(r'videos', VideoUploadViewSet)
router.register(r'analysis', AIAnalysisViewSet)

# Include the router-generated URLs in urlpatterns
urlpatterns = router.urls

urlpatterns = [
    path('videos/', VideoUploadView.as_view(), name='video-upload'),
]

