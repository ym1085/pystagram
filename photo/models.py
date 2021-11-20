from django.contrib.auth.models import User
from django.db import models

# Model - DB
class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='timeline_photo/%Y/%m/%d') # 자동으로 년/월/일 을 생성하여 이미지 추가
    created = models.DateTimeField(auto_now_add=True) # 시간까지 저장
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "text : " + self.text

    class Meta:
        # order = ['-created']
        ordering = ['-created']



