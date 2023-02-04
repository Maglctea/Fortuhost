from django import forms
from support.models import Feedback

# class BugReportForm(forms.Form):
#     subject = forms.CharField(label='Название', max_length=50, required=False, strip=True)
#     content = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), strip=True)
#     file = forms.FileField(label='Файл', widget=forms.FileInput, required=False)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields:
#             self.fields[field].widget.attrs['class'] = 'form-control'



class BugReportForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'