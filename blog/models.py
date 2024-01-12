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

    class Meta:
        db_table = 'Register'


class BaseModel(models.Model):
    reference_id = models.CharField(
        max_length=32, unique=True, primary_key=True, default=generate_uuid)
    is_delete = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User, db_column="created_by", on_delete=models.PROTECT, related_name="+")
    created_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(
        User, db_column="updated_by", on_delete=models.PROTECT, null=True)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True


class BlogPost(BaseModel):
    title = models.CharField(max_length=200)
    post = models.CharField(max_length=200)
    username = models.CharField(max_length=100)

    class Meta:
        db_table = 'post'
