from django.contrib.auth.models import User
from django.db import models


class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device_type = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device_type} owned by {self.user.username}"


class VideoUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='videos/')
    gps_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    gps_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Video by {self.user.username} on {self.created_at}"


class AIAnalysis(models.Model):
    # Use a string reference 'VideoUpload' to avoid circular dependency
    video = models.ForeignKey('VideoUpload', on_delete=models.CASCADE)
    analysis_result = models.TextField()  # Field for storing AI analysis results
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analysis for {self.video}"
