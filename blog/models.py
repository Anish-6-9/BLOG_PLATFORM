from django.db import models
from django.contrib.auth. models import User
import uuid

# Create your models here.


def generate_uuid():
    return uuid.uuid4().hex


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


class registration(BaseModel):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'Register'


class BlogPost(BaseModel):
    title = models.CharField(max_length=200)
    post = models.CharField(max_length=200)
    username = models.CharField(max_length=100)

    class Meta:
        db_table = 'post'


class Comments(models.Model):
    comment_id = models.CharField(max_length=32)
    comment_time = models.DateTimeField()
    is_delete = models.BooleanField(default=False)
    comment_by = models.CharField(max_length=100)
    cmt = models.CharField(max_length=1000)

    class Meta:
        db_table = 'Comments'

    def _str_(self):
        return self.comment_by


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # it ensures that a user can like a post only once.
        unique_together = ('user', 'post')
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

    def __str__(self):
        return f'{self.user.username} likes {self.post.title}'


class Share(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')
        verbose_name = 'Share'
        verbose_name_plural = 'Shares'

    def __str__(self):
        return f'{self.user.username} shares {self.post.title}'
