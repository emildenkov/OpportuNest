from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class PDFValidator:

    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value: str):
        if not value:
            self.__message = 'Unsupported file type! Make sure your file is .pdf'
        else:
            self.__message = value


    def __call__(self, value):
        if not value.name.endswith('.pdf'):
            raise ValidationError(self.__message)
