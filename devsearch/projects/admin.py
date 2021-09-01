from django.contrib import admin
from .models import Project, Review, Tag
# Register your models here to make them available in Admin page.
admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)