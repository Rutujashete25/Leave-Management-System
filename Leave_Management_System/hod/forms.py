from django import forms
from accounts.models import CustomUser

class StaffRegistartionForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name','username','email','contact_number']
       