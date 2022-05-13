from admin_panel.models import Client, Property, File
from django import forms

school_name =(
    ("Active", "Active"),
)

category =(
    ("Corner", "Corner"),
)

property_status =(
    ("In Progress", "In Progress"),
)

file_status =(
    ("Active", "Active"),
    ("Pending", "Pending"),
    ("Dispute", "Dispute"),
    ("Canceled", "Canceled"),
)

class ClientForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name...'}))
    guardian = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Guardian\'s Name ...'}))
    contact = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','id':'contact', 'placeholder':'Contact Number...', 'pattern':"[0-9]{4}-[0-9]{7}"}))
    cnic = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','id':'cnic' ,'placeholder':'CNIC...', 'pattern':"[0-9]{5}-[0-9]{7}-[0-9]{1}"}))
    status = forms.ChoiceField(choices = school_name, label="", initial='', widget=forms.Select(attrs={"class":'form-control', 'placeholder':'Status...'}), required=True)

class PropertyForm(forms.Form):
    plot = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Plot Number...'}))
    size = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Size...'}))
    block = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Block...'}))
    amount = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Amount...'}))
    category = forms.ChoiceField(choices = category, label="", initial='', widget=forms.Select(attrs={"class":'form-control', 'placeholder':'Category...'}), required=True)
    status = forms.ChoiceField(choices = property_status, label="", initial='', widget=forms.Select(attrs={"class":'form-control', 'placeholder':'Status...'}), required=True)

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file', 'agent','client','property', 'status')
    def __init__(self, *args, **kwargs):
        super(FileForm, self).__init__(*args, **kwargs)
        self.fields['client'].empty_label = 'Client...'
        self.fields['property'].empty_label = 'Plot - Size - Block - Category...'
        self.fields['status'] = forms.ChoiceField(label="Status...", choices=file_status)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs['placeholder'] = field.capitalize() + "..."


    
