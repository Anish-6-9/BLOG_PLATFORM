from django.db import models
from django.contrib.auth. models import User
import uuid

# Create your models here.


def generate_uuid():
    return uuid.uuid4().hex


class registration(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    reference_id = models.CharField(
        max_length=32, unique=True, primary_key=True, default=generate_uuid)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'Register'
