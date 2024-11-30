from django.test import TestCase

from OpportuNest.accounts.forms import CompanyCreationForm


class TestCompanyRegistrationForm(TestCase):

    def setUp(self):
        self.valid_data = {
            'email': 'somecompany@gmail.com',
            'company_name': 'Test',
            'password1': '12admin34',
            'password2': '12admin34',
        }

    def test__form_is_valid_expected_true(self):
        form = CompanyCreationForm(self.valid_data)
        self.assertTrue(form.is_valid())

    def test__form_is_valid_expected_false__password_missing(self):
        self.valid_data['password1'] = ''

        form = CompanyCreationForm(self.valid_data)

        self.assertFalse(form.is_valid())

    def test__form_is_valid_expected_false__email_missing(self):
        self.valid_data['email'] = ''

        form = CompanyCreationForm(self.valid_data)

        self.assertFalse(form.is_valid())