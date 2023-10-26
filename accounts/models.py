from django.db import models
# import uuid
# from shortuuid.django_fields import ShortUUIDField

# Create your models here.
class user_profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.BigIntegerField()