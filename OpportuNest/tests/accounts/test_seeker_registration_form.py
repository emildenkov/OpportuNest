from django.test import TestCase

from OpportuNest.accounts.forms import SeekerCreationForm


class TestSeekerRegistrationForm(TestCase):

    def setUp(self):
        self.valid_data = {
            'email': 'someemail@gmqail.com',
            'first_name': 'John',
            'last_name': 'Doe',
            'password1': '12admin34',
            'password2': '12admin34',
        }

    def test__form_is_valid_expect_true(self):
        form = SeekerCreationForm(self.valid_data)

        self.assertTrue(form.is_valid())

    def test__form_is_valid_expect_false_password_missing(self):
        self.valid_data['password1'] = ''
        form = SeekerCreationForm(self.valid_data)

        self.assertFalse(form.is_valid())

    def test_form_is_valid_expect_false_email_missing(self):
        self.valid_data['email'] = ''

        form = SeekerCreationForm(self.valid_data)

        self.assertFalse(form.is_valid())