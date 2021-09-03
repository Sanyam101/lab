from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import Project
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # view all fields in the form 
        #fields = '__all__'

        # view only selected fields 
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags']
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

        # or you can update each field one by one 
        #self.fields['title'].widget.attrs.update({'class':'input', 'placeholder':'add title'})
        #self.fields['description'].widget.attrs.update({'class':'input', 'placeholder':'add description'})