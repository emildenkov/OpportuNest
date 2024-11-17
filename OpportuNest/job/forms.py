from django import forms

from OpportuNest.job.models import Job


class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['posted_by', 'date_posted']

        error_messages = {
            'title': {
                'required': 'Title is required',
            },
            'description': {
                'required': 'Description is required',
            },
            'requirements' : {
                'required': 'Requirements are required',
            },
            'company': {
                'required': 'Company name is required',
            },
            'location': {
                'required': 'Location is required',
            }
        }

