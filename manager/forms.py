from django import forms
from .models import PasswordEntry

class AddEntryForm(forms.ModelForm):
    class Meta:
        model = PasswordEntry
        fields = ['website', 'username', 'encrypted_password'] 

    def clean_password(self):
        # Optional password validation logic here (e.g., minimum length)
        password = self.cleaned_data['encrypted_password']
        # ... (validation code)
        return password
