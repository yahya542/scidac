# capsule/admin.py

from django.contrib import admin
from .models.capsule_models import StudySession

admin.site.register(StudySession)
