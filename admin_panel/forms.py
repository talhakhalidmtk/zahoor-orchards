from admin_panel.models import Client, Property, File, Agent
from django.core.validators import RegexValidator
from django import forms

status =(
    ("Active", "Active"),
)

category =(
    ("General", "General"),
    ("Boulevard", "Boulevard"),
    ("Corner", "Corner"),
    ("Facing Park", "Facing Park"),
    ("Corner Boulevard", "Corner Boulevard"),
    ("Corner Facing Park", "Corner Facing Park"),
)

property_status =(
    ("In Progress", "In Progress"),
    ("Dispute", "Dispute"),
    ("Completed", "Completed"),
)

file_status =(
    ("Active", "Active"),
    ("Pending", "Pending"),
    ("Dispute", "Dispute"),
    ("Canceled", "Canceled"),
)

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ('name', 'guardian', 'contact', 'cnic', 'image')
    def __init__(self, *args, **kwargs):
        super(AgentForm, self).__init__(*args, **kwargs)
        self.fields['contact'].widget.attrs.update({'pattern':"[0-9]{4}-[0-9]{7}"})
        self.fields['cnic'].widget.attrs.update({'pattern':"[0-9]{5}-[0-9]{7}-[0-9]{1}"})
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'id': field})
            self.fields[field].widget.attrs['placeholder'] = field.capitalize() + "..." 


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
        fields = ('plot','name', 'size', 'block', 'amount', 'category', 'status')
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
        fields = ('file','new_file', 'agent','client','property', 'status')
    def __init__(self, *args, **kwargs):
        super(FileForm, self).__init__(*args, **kwargs)
        self.fields['client'].empty_label = 'Client...'
        self.fields['property'].empty_label = 'Plot...'
        self.fields['agent'].empty_label = 'Agent...'
        self.fields['status'] = forms.ChoiceField(label="Status...", choices=file_status)
        for field in self.fields:
            if field == "file":
                self.fields[field].widget.attrs.update({'class': 'form-control'})
                self.fields[field].widget.attrs['placeholder'] = "FILE NUMBER" + "..."
                self.fields[field].widget.attrs.update({'id': field})
            elif field == "new_file":
                self.fields[field].widget.attrs.update({'class': 'form-control'})
                self.fields[field].widget.attrs['placeholder'] = "NEW FILE NUMBER" + "..."
                self.fields[field].widget.attrs.update({'id': field})
            else:
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
        self.fields['property'].empty_label = 'Plot...'
        self.fields['payment_details'] = forms.CharField()
        self.fields['amount'] = forms.CharField()
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs['placeholder'] = field.capitalize() + "..."
            self.fields[field].widget.attrs.update({'id': field})


    
