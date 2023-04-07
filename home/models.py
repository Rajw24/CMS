from django.db import models
from django.conf import settings
import os

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return os.path.join(settings.MEDIA_ROOT, f'user_{instance.user}', filename)

class Enquiries(models.Model):
    email = models.EmailField(max_length=255)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Certificates(models.Model):
    user = models.IntegerField()
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to=user_directory_path)

    def __str__(self):
        return self.title