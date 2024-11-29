from django import forms
from OpportuNest.review.models import Review


class ReviewBaseForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'


class CreateReviewForm(ReviewBaseForm):
    class Meta:
        model = Review
        exclude = ['reviewer', 'date_posted']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rating'].help_text = 'Rate us from 1 to 5 based on your experience.'
        self.fields['rating'].widget = forms.Select(
            choices=[
                ('', 'Select a rating'),
                (1, '1 - Poor'),
                (2, '2 - Fair'),
                (3, '3 - Good'),
                (4, '4 - Very Good'),
                (5, '5 - Excellent'),
            ],
            attrs={'class': 'form-select'}
        )

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if not rating or rating == '':
            raise forms.ValidationError('Please select a valid rating.')
        return rating

