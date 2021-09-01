from django.db.models import fields
from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # view all fields in the form 
        #fields = '__all__'

        # view only selected fields 
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags']