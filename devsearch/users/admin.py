from django.contrib import admin
from django.db import models

# Register your models here.
from .models import Profile, Skill
admin.site.register(Profile)
admin.site.register(Skill)