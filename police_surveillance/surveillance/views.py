from rest_framework import viewsets
from .models import VideoUpload, AIAnalysis
from .serializers import VideoUploadSerializer, AIAnalysisSerializer

class VideoUploadViewSet(viewsets.ModelViewSet):
    queryset = VideoUpload.objects.all()
    serializer_class = VideoUploadSerializer

class AIAnalysisViewSet(viewsets.ModelViewSet):
    queryset = AIAnalysis.objects.all()
    serializer_class = AIAnalysisSerializer
