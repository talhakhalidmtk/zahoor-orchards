from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.contrib.auth import login,authenticate,logout

from .models import User, UserManager

class UserLoginForm(forms.Form):
    cnic=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'CNIC','class':'form-control','pattern':"[0-9]{5}-[0-9]{7}-[0-9]{1}"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'PASSWORD','class':'form-control'}))
    fields = ['cnic', 'password']

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    cnic = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'CNIC','class':'form-control','pattern':"[0-9]{5}-[0-9]{7}-[0-9]{1}"}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    

    class Meta:
        model = User
        fields = ('name', 'guardian','contact')
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field != "password1" and field!= "password2":
                self.fields[field].widget.attrs.update({'class': 'form-control'})
                self.fields[field].widget.attrs.update({'id': field})
                self.fields[field].widget.attrs['placeholder'] = field.upper() + "..." 
            elif field == "password1":
                self.fields[field].widget.attrs.update({'class': 'form-control'})
                self.fields[field].widget.attrs.update({'id': field})
                self.fields[field].widget.attrs['placeholder'] = "PASSWORD..." 
            elif field == "password2":
                self.fields[field].widget.attrs.update({'class': 'form-control'})
                self.fields[field].widget.attrs.update({'id': field})
                self.fields[field].widget.attrs['placeholder'] = "CONFIRM PASSWORD..." 

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.name = self.cleaned_data["name"]
        user.guardian = self.cleaned_data["guardian"]
        user.cnic = self.cleaned_data["cnic"]
        user.contact = self.cleaned_data["contact"]
        user.set_password(self.cleaned_data["password1"])
        if commit:
            print("success")
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('name', 'guardian','password','cnic','contact')
