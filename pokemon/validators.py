from django.forms import ValidationError
from django.utils.deconstruct import deconstructible
import re
import csv
import requests
import xmltodict
from django.conf import settings


CSV_PATH = '/Users/hyunjoongkim/Downloads/post.txt'
reader= csv.reader(open(CSV_PATH, 'rt', encoding='cp949'), delimiter="|")

columns=next(reader)

ls =[]

for row in enumerate(reader):
      data = dict(zip(columns, row))
      ls.append(str(data['우편번호']))


@deconstructible
class post(object):
      def __init__(self):
            pass

      def __call__(self, value):
            if value not in ls:
                  raise ValidationError('우편번호가 틀립니다!')


@deconstructible
class post_api(object):
      '우편번호 체계안내 : http://www.koreapost.go.kr/kpost/sub/subpage.jsp?contId=010101040100'
      def __init__(self, check= False):
            self.check=check

      def __call__(self, zip_code):
            if not re.match(r'^\d{5}$', zip_code):
                  raise ValidationError('5자리 입력하시오')
            if self.check:
                  self.check_func(zip_code)

      def check_func(self, zip_code):
            '우체국 open api : http://biz.epost.go.kr/customCenter/custom/custom_10.jsp'
            params = {
            'regkey': settings.EPOST_API_KEY,
            'target': 'postNew',
            'query': zip_code,
         }

#https://www.youtube.com/results?search_query=drake

            xml = requests.get('http://biz.epost.go.kr/KpostPortal/openapi', params=params).text
            response = xmltodict.parse(xml)
            try:
                  error = response['error']
                  print('########',response['error'])
            except KeyError:
                  pass
            else:
                  raise ValidationError('[{error_code}] {message}'.format(**error))

@deconstructible
class max(object):
      def __init__(self, max_length):
            self.max_length=max_length

      def __call__(self, value):
            if len(value) > self.max_length:
                  raise ValidationError('{}글자이하!'.format(self.max_length))

@deconstructible
class min(object):
      def __init__(self, min_length):
            self.min_length=min_length

      def __call__(self, value):
            if len(value) < self.min_length:
                  raise ValidationError('{}글자이상!'.format(self.min_length))

@deconstructible
class phone_number_validator(object):
      def __init__(self):
            pass

      def __call__(self, value):
            if not re.match(r'^01[06789][1-9]\d{6,7}$', value):
                  raise ValidationError('휴대폰 번호를 입력해주세요.')
