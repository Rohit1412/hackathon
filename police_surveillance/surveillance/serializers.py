from rest_framework import serializers
from .models import VideoUpload, AIAnalysis, Device
from .models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'video_file', 'gps_latitude', 'gps_longitude', 'uploaded_at', 'user']

class VideoUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoUpload
        fields = ['id', 'user', 'video_file', 'gps_latitude', 'gps_longitude', 'created_at']

class AIAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIAnalysis
        fields = ['id', 'video', 'analysis_result', 'timestamp']

