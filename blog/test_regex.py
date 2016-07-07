import re

def validate_number(number):
      if re.match(r'^01[016789][1-9]\d{6,7}$', number):
            return True
      return False


print(validate_number('01075114389'))
print(validate_number('01075389'))
print(validate_number('010751a389'))