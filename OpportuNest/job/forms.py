from django import forms

from OpportuNest.job.models import Job
from OpportuNest.mixins import ReadOnlyMixin


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
            'location': {
                'required': 'Location is required',
            }
        }


class EditJobForm(AddJobForm):
    pass


class DeleteJobForm(ReadOnlyMixin, forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['posted_by', 'date_posted']


class SearchJobForm(forms.Form):
    query = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search for a job',
            }
        ),
        label='',
        required=False,
        max_length=15
    )