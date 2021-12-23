from django import forms
from django.core.mail.message import EmailMessage

class ContactForm(forms.Form):
    name = forms.CharField(label="Name", widget=forms.TextInput(), max_length=30)
    email = forms.EmailField(label="Email", widget=forms.TextInput(), max_length=30)
    subject = forms.CharField(label="Subject", widget=forms.TextInput(), max_length=50)
    message = forms.CharField(label="Message", widget=forms.Textarea())
    
    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        content = f'Name: {name}\nE-mail: {email}\nSubject: {subject}\nMessage: {message}'

        mail = EmailMessage(
            subject='Email send by system Django2',
            body=content,
            from_email='joaosoutto@hotmail.com',
            to=['joaosoutto92@gmail.com'],
            headers={'Reply-To': email},
        )

        mail.send()