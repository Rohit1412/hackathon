from rest_framework.routers import DefaultRouter
from .views import VideoUploadViewSet, AIAnalysisViewSet

router = DefaultRouter()
router.register(r'videos', VideoUploadViewSet)
router.register(r'analysis', AIAnalysisViewSet)

urlpatterns = router.urls
