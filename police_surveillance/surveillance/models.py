from django.contrib.auth.models import User
from django.db import models

class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device_type = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class VideoUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='videos/')
    gps_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    gps_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class AIAnalysis(models.Model):
    video = models.ForeignKey(VideoUpload, on_delete=models.CASCADE)
    analysis_result = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
