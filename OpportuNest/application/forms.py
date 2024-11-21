from django import forms

from OpportuNest.application.models import Application
from OpportuNest.mixins import ReadOnlyMixin


class BaseApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        exclude = ['job', 'applicant', 'date_applied']


class CreateApplicationForm(BaseApplicationForm):
    pass
