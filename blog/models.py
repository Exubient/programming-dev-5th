from .validators import max, min, lnglat_validator
from django.db import models
from django.utils import timezone
from pic import thumbnail
from django.db.models.signals import pre_save
import os
from uuid import uuid4
from django.core.files import File

def myupload(instance, filename):
      pass


def random_name_upload_to(instance, filename):
      extension = os.path.splitext(filename)[-1].lower()
      name = uuid4().hex
      path = name[:3] + '/' + name[3:6] + '/' + name[6:]  +  extension
      return os.path.join(path)

class Post(models.Model):
      title = models.CharField(max_length=100, verbose_name='제목',)
      content = models.TextField(help_text='Markdown 문법을 써주세요.')
      lnglat = models.CharField( max_length=50, validators =[lnglat_validator], help_text='경도, 위도 포맷으로 입력')
      photo = models.ImageField(upload_to=random_name_upload_to)
      created_at = models.DateTimeField(default=timezone.now)
      test_field = models.IntegerField(default=10)
      tag_set=models.ManyToManyField('Tag', blank=True)

      def __str__(self):
            return self.title

      # Create your models here.

class Comment(models.Model):
      post =models.ForeignKey(Post)
      message= models.TextField()
      author= models.CharField(max_length=20)
      jjal = models.ImageField(blank=True)

      def __str__(self):
            return self.message


def pre_on_post_save(sender, **kwargs):
      post = kwargs['instance']
      if post.photo:
            max_width = 300
            if post.photo.width > max_width or post.photo.height > max_width:
                  processed_file = thumbnail(post.photo.file, max_width, max_width)
                  post.photo.save(post.photo.name, File(processed_file))

pre_save.connect(pre_on_post_save, sender=Post)

class Comment1(models.Model):
      post =models.ForeignKey(Post)
      message= models.TextField()
      author= models.CharField(max_length=20)

      def __str__(self):
            return self.message



class Tag(models.Model):
      name = models.CharField(max_length=20)

      def __str__(self):
            return self.name
