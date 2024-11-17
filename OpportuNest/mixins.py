class ReadOnlyMixin:

    def make_read_only(self):
        for field_name, field in self.fields.items():
            if field_name in self.fields:
                self.fields[field_name].widget.attrs['readonly'] = 'readonly'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_read_only()