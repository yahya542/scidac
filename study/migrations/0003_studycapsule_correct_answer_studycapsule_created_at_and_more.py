# Generated by Django 5.2 on 2025-06-01 09:01

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0002_studycapsule_capsule'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='studycapsule',
            name='correct_answer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='studycapsule',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='studycapsule',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studycapsule',
            name='question',
            field=models.TextField(default='Pertanyaan akan dihasilkan oleh AI'),
        ),
        migrations.AddField(
            model_name='studycapsule',
            name='topic',
            field=models.CharField(default='topik harus diisi', max_length=255),
        ),
        migrations.AddField(
            model_name='studycapsule',
            name='unlock_next_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='studycapsule',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='studycapsule',
            name='user_answer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='studysession',
            name='topic',
            field=models.CharField(default='topik harus diisi', max_length=200),
        ),
        migrations.DeleteModel(
            name='Capsule',
        ),
    ]
