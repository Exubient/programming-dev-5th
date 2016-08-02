from django.forms import ValidationError
import re

class max(object):
      def __init__(self, max_length):
            self.max_length=max_length

      def __call__(self, value):
            if len(value) > max_length:
                  raise ValidationError('{}글자이하!'.format(max_length))

class min(object):
      def __init__(self, min_length):
            self.min_length=min_length

      def __call__(self, value):
            if len(value) < min_length:
                  raise ValidationError('{}글자이상!'.format(min_length))

def lnglat_validator(lnglat):
      if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$', lnglat):
            raise forms.ValidationError('Invalid lnglat Type')


def min_length_validator(min_length):
      def wrap(value):
            if len(value) < min_length:
                  raise ValidationError('{}글자이상!'.format(min_length))
      return wrap