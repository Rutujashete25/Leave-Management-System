from django import forms
from accounts.models import Leaves



class LeaveApplyForm(forms.ModelForm):
    leave_from_date = forms.DateField(widget=
                                forms.widgets.DateInput
                                (format='%Y-%m-%d ', 
                                attrs={ 'type':'date'}))

    leave_to_Date = forms.DateField(widget=
                                forms.widgets.DateInput
                                (format='%Y-%m-%d ', 
                                attrs={'type':'date'}))


    class Meta:
        model = Leaves
        fields = ['leave_from_date','leave_to_Date','reason']

     



