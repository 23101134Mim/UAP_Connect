from django.db import models

# Create your models here.
from django.db import models

class NoticeCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Notice(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(NoticeCategory, on_delete=models.CASCADE)
    description = models.TextField()
    file = models.FileField(upload_to='notices/', blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title