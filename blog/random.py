import os
from uuid import uuid4
from django.utils import timezone

def random_name_upload_to(instance, filename):
    name = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower()
    return os.path.join(name[:3], name[3:6], name[6:] + extension)
