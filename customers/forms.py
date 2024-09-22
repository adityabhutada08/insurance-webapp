from django import forms
from .models import Customer, FamilyMember

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name','last_name' ,'email', 'phone', 'address', 'city', 'state', 'postal_code']

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Your Email'
        self.fields['phone'].widget.attrs['placeholder'] = 'Enter Your Mobile Number'
        self.fields['address'].widget.attrs['placeholder'] = 'Enter Your Adddess'
        self.fields['city'].widget.attrs['placeholder'] = 'Enter Your City'
        self.fields['state'].widget.attrs['placeholder'] = 'Enter Your State'
        self.fields['postal_code'].widget.attrs['placeholder'] = 'Enter Your Postal Code'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            
class FamilyMemberForm(forms.ModelForm):
    class Meta:
        model = FamilyMember
        fields = ['first_name','last_name' ,'email', 'phone', 'relationship']

    def __init__(self, *args, **kwargs):
        super(FamilyMemberForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Your Email'
        self.fields['phone'].widget.attrs['placeholder'] = 'Enter Your Mobile Number'
        self.fields['relationship'].widget.attrs['placeholder'] = 'Enter Your Relationship with Family Member'
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    