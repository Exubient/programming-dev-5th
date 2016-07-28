import re
from django.db import models

# Create your models here.

class user(models.Model):
      name = models.CharField(max_length=50)
      town = models.CharField(max_length=10)
      age = models.IntegerField(default=8)
      location = models.CharField(max_length=10)

      def __str__(self):
            return self.name


class location(models.Model):
      name=models.CharField(max_length=100)
      lnglat=models.CharField(max_length=40)
      created_at=models.DateTimeField(auto_now_add=True)
      updated_at=models.DateTimeField(auto_now=True)

      def __str__(self):
            return self.name


class pokemon(models.Model):
      name = models.CharField(max_length=10)
      attack = models.CharField(max_length=10)
      defense = models.CharField(max_length=10)
      ptype = models.CharField(max_length=10)

      def __str__(self):
            return self.name

class capture(models.Model):
      user = models.ForeignKey(user, null =True, blank = True)
      pokemon = models.ForeignKey(pokemon, null =True, blank = True)
      location = models.ForeignKey(location, null=True, blank=True)


      def __str__(self):
            return "{} has captured {} at {}".format(self.user, self.pokemon, self.location)


# post.commet_set.all()
# =
# comment.objects.filter(post=post)






