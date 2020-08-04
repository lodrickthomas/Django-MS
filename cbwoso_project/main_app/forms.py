from .models import Employee
from django import forms


class EmployeeForm(forms.ModelForm):
    class Meta:
        model= Employee
        fields= ['first_name', 'last_name', 'registration_number', 'phone_number', 'position']
        #this shows how the fields will appear on crispy form
        labels = {
            'first_name':'First Name',
            'first_last': 'Last Name',
            'registration_number':'Registration Number',
            'phone_number': 'Phone Number',
            'position': 'Your Position'
        }
        #display "select" instead of "-----"
        def __init__(self, *args, **kwargs):
            super(EmployeeForm, self).__init__(*args, **kwargs)
            self.fields['position'].empty_label = "Select"
            self.fields['phone_number'].required = False

