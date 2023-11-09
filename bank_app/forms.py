from django import forms
from .models import District, Branch

from django import forms
from .models import ApplicationForm

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = ApplicationForm
        fields = ['name', 'dob', 'age', 'gender', 'phone_number', 'mail_id', 'address', 'district', 'branch', 'account_type', 'materials_provided']

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        # You can add additional form customization here if needed

        # For example, you can customize the labels, widgets, and other form attributes:
        self.fields['dob'].widget = forms.TextInput(attrs={'type': 'date'})

    # You can also add custom validation logic here if needed
