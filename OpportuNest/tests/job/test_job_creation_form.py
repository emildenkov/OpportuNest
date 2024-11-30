from django.test import TestCase

from OpportuNest.job.forms import AddJobForm


class TestJobCreationForm(TestCase):
    def setUp(self):
        self.valid_data = {
            'title': 'Some title',
            'description': 'Some description',
            'requirements': 'Some requirements',
            'location': 'Some location',
        }

    def test__form_valid__expect_true(self):
        form = AddJobForm(self.valid_data)
        self.assertTrue(form.is_valid())

    def test__form_invalid__expect_false__title_missing(self):
        self.valid_data['title'] = ''
        form = AddJobForm(self.valid_data)

        self.assertFalse(form.is_valid())

    def test__form_invalid__expect_false__description_missing(self):
        self.valid_data['description'] = ''
        form = AddJobForm(self.valid_data)

        self.assertFalse(form.is_valid())

    def test__form_invalid__expect_false__requirements_missing(self):
        self.valid_data['requirements'] = ''
        form = AddJobForm(self.valid_data)

        self.assertFalse(form.is_valid())

    def test__form_invalid__expect_false__location_missing(self):
        self.valid_data['location'] = ''
        form = AddJobForm(self.valid_data)

        self.assertFalse(form.is_valid())