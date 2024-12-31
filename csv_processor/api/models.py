from django.db import models

class UploadedFile(models.Model):
    file_name = models.CharField(max_length=255)  # Unique filename
    original_name = models.CharField(max_length=255)  # User-provided name
    upload_date = models.DateTimeField(auto_now_add=True)
    file_path = models.CharField(max_length=255)

    def __str__(self):
        return self.file_name