from admin_panel.models import Client, Property, File
from django import forms

status =(
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

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'guardian', 'contact', 'cnic', 'status')
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['status'] = forms.ChoiceField(label="Status...", choices=status)
        self.fields['contact'].widget.attrs.update({'pattern':"[0-9]{4}-[0-9]{7}"})
        self.fields['cnic'].widget.attrs.update({'pattern':"[0-9]{5}-[0-9]{7}-[0-9]{1}"})
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'id': field})
            self.fields[field].widget.attrs['placeholder'] = field.capitalize() + "..." 

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('plot', 'size', 'block', 'amount', 'category', 'status')
    def __init__(self, *args, **kwargs):
        super(PropertyForm, self).__init__(*args, **kwargs)
        self.fields['category'] = forms.ChoiceField(label="Category...", choices=category)
        self.fields['status'] = forms.ChoiceField(label="Status...", choices=property_status)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'id': field})
            self.fields[field].widget.attrs['placeholder'] = field.capitalize() + "..."

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
            self.fields[field].widget.attrs.update({'id': field})

class PaymentForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file', 'client','property')
    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields['client'].empty_label = 'Client...'
        self.fields['property'].empty_label = 'Plot - Size - Block - Category...'
        self.fields['payment_details'] = forms.CharField()
        self.fields['amount'] = forms.CharField()
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs['placeholder'] = field.capitalize() + "..."
            self.fields[field].widget.attrs.update({'id': field})


    
