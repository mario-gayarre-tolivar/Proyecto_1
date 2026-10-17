from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field, HTML
from . import models

class DestinationForm(forms.ModelForm):
    class Meta:
        model = models.Destination
        fields = ['name', 'description']
        labels = {
            'name': 'Destination Name',
            'description': 'Description',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter destination details...'}),
            'name': forms.TextInput(attrs={'placeholder': 'e.g. Mars, Europa, Titan'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        action_text = 'Update Destination' if self.instance and self.instance.pk else 'Create Destination'
        self.helper.layout = Layout(
            Field('name'),
            Field('description'),
            Submit('submit', action_text, css_class='btn btn-primary mr-2'),
            HTML('<a href=\"{% url ''destinations'' %}\" class=\"btn btn-secondary\">Cancel</a>'),
        )


class InfoRequestForm(forms.ModelForm):
    class Meta:
        model = models.InfoRequest
        fields = ['name', 'email', 'cruise', 'notes']
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'cruise': 'Interested Cruise',
            'notes': 'Questions or Notes',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'name@example.com'}),
            'notes': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell us what details or questions you have...'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-3'),
                Column('email', css_class='form-group col-md-6 mb-3'),
            ),
            Field('cruise', css_class='mb-3'),
            Field('notes', css_class='mb-3'),
            Submit('submit', 'Send Request', css_class='btn btn-primary mr-2'),
            HTML('<a href=\"{% url ''index'' %}\" class=\"btn btn-secondary\">Cancel</a>'),
        )
