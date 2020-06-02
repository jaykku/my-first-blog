from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)                        # 글자수가 제한된 텍스트
    text = models.TextField()                                       # 글자수 제한 없음
    created_date = models.DateTimeField(default=timezone.now)       # 날짜와 시간
    published_date = models.DateTimeField(blank=True, null=True)    # 날짜와 시간

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title