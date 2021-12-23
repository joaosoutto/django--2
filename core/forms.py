from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Name", widget=forms.TextInput(), max_length=30)
    email = forms.EmailField(label="Email", widget=forms.TextInput(), max_length=30)
    subject = forms.CharField(label="Subject", widget=forms.TextInput(), max_length=50)
    message = forms.CharField(label="Message", widget=forms.Textarea())