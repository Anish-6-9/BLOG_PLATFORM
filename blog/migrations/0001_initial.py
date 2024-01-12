# Generated by Django 4.2.7 on 2024-01-11 15:36

import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Register',
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('reference_id', models.CharField(default=blog.models.generate_uuid, max_length=32, primary_key=True, serialize=False, unique=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('title', models.CharField(max_length=200)),
                ('post', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=100)),
                ('created_by', models.ForeignKey(db_column='created_by', on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(db_column='updated_by', null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'post',
            },
        ),
    ]
