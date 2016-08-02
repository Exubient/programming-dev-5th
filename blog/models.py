from .validators import max, min, lnglat_validator, min_length_validator
from django.db import models
from django.utils import timezone

class Post(models.Model):
      title = models.CharField(max_length=100, verbose_name='제목', validators=[min_length_validator(4)])
      title2 = models.CharField(max_length=100, verbose_name='제목')
      content = models.TextField(help_text='Markdown 문법을 써주세요.')
      lnglat = models.CharField( max_length=50, validators =[lnglat_validator], help_text='경도, 위도 포맷으로 입력')
      created_at = models.DateTimeField(default=timezone.now)
      test_field = models.IntegerField(default=10)
      tag_set=models.ManyToManyField('Tag', blank=True)
      # Create your models here.

class Comment(models.Model):
      post =models.ForeignKey(Post)
      message= models.TextField()
      author= models.CharField(max_length=20)

class Tag(models.Model):
      name = models.CharField(max_length=20)

      def __str__(self):
            return self.name
