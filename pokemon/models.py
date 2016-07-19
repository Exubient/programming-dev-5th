import re
from django.db import models
from django.utils import timezone



# Create your models here.


class user(models.Model):
      name = models.CharField(max_length=50)
      town = models.CharField(max_length=10)
      age = models.IntegerField(default=8, max_length=3)
      location = models.CharField(max_length=10)


      def __str__(self):
            return self.name


class pokemon(models.Model):
      user = models.ForeignKey(user, null =True, blank = True)

      name = models.CharField(max_length=10)
      attack = models.CharField(max_length=10)
      defense = models.CharField(max_length=10)
      ptype = models.CharField(max_length=10)

      def __str__(self):
            return self.name

