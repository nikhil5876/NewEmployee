from django import forms
from .models import EmployeeDB

class DateInput(forms.DateInput):
    input_type = 'date'

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = EmployeeDB
        fields = ['eName', 'eLastName', 'eMobNo', 'eEmail', 'eAddress', 'eGroup', 'eExtraInfo', 'eDateOfRenewable']
        widgets = {
            'eDateOfRenewable': DateInput(),
        }
        labels = {
            'eName':'Name ', 
            'eLastName': 'Last Name ',
            'eMobNo': 'Mobile No. ', 
            'eEmail': 'Email ', 
            'eAddress': 'Address ', 
            'eGroup': 'Group ', 
            'eExtraInfo': 'Extra Information ', 
            'eDateOfRenewable': 'Date of Renewable ',
            
        }

    def __init__(self, *arg,**kwargs):
        super(EmployeeForm, self).__init__(*arg,**kwargs)
        self.fields['eLastName'].required  = False
        self.fields['eExtraInfo'].required  = False
        self.fields['eDateOfRenewable'].required  = False
