import re
from .validators import max, phone_number_validator, post, post_api
from django.db import models

# Create your models here.
"""
class PhoneNumberField(models.CharField):
      def __init__(self, *args, **kwargs):
            kwargs.setdault('max_length', 20)
            kwargs.setdault('validators', [])
            kwargs['validators'].append(phone_number_validator)
            super().__init__(*args, **kwargs)

            우체국 key = 5315606e3fe0e7fe31470021512564
"""

class user(models.Model):
      name = models.CharField(max_length=50, validators=[max(5)])
      town = models.CharField(max_length=10)
      age = models.IntegerField(default=8)
      location = models.CharField(max_length=10)
      phone = models.CharField(max_length=10, validators=[phone_number_validator()])
      post_number1 = models.CharField(max_length=10, validators=[post()])
      post_number2 = models.CharField(max_length=10, validators=[post_api(True)])

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






