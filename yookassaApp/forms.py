from django import forms
from yookassaApp.models import Transaction


class TransationCreateForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('value',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'