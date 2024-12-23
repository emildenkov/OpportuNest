from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from OpportuNest.accounts.choices import UserChoices
from OpportuNest.accounts.models import Company, Seeker
from OpportuNest.skill.models import Skill

UserModel = get_user_model()


class AppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email', )


class CompanyCreationForm(UserCreationForm):
    company_name = forms.CharField(max_length=100)

    class Meta:
        model = UserModel
        fields = ('email','company_name', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=commit)

        company_name = self.cleaned_data['company_name']

        company = Company.objects.create(
            user=user,
            company_name=company_name,
        )

        if commit:
            company.save()

        return user


class SeekerCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = UserModel
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')


    def save(self, commit=True):
        user = super().save(commit=commit)

        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']

        seeker = Seeker.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
        )

        if commit:
            seeker.save()

        return user


class AccountTypeSelectionForm(forms.Form):
    account_type = forms.ChoiceField(
        choices=UserChoices,
        widget=forms.RadioSelect,
        label='Select Account Type',
    )


class CompanyEditForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('company_name', 'description', 'logo')


class SeekerEditForm(forms.ModelForm):

    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all().order_by('name'),
        widget=forms.SelectMultiple(attrs={'class': 'select2'}),
        required=False,
    )

    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        required=False,
    )

    class Meta:
        model = Seeker
        fields = ['first_name', 'last_name', 'profile_picture', 'date_of_birth', 'skills']
