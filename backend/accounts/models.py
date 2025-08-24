from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    is_owner = models.BooleanField(default=False)  # parking owner
    is_customer = models.BooleanField(default=True)
