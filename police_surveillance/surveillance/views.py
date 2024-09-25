from rest_framework import viewsets
from .models import VideoUpload, AIAnalysis
from .serializers import VideoUploadSerializer, AIAnalysisSerializer
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class VideoUploadViewSet(viewsets.ModelViewSet):
    queryset = VideoUpload.objects.all()
    serializer_class = VideoUploadSerializer

class AIAnalysisViewSet(viewsets.ModelViewSet):
    queryset = AIAnalysis.objects.all()
    serializer_class = AIAnalysisSerializer


class VideoUploadView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated with JWT
    parser_classes = [MultiPartParser, FormParser]  # Support file uploads

    def post(self, request, *args, **kwargs):
        data = {
            'user': request.user.id,
            'video_file': request.FILES.get('video_file'),
            'gps_latitude': request.data.get('gps_latitude'),
            'gps_longitude': request.data.get('gps_longitude'),
        }
        serializer = VideoUploadSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
