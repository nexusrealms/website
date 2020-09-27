from django import forms

class ContactForm(forms.Form):
    firstname = forms.CharField(
        label=('First Name'),
        required=True,
        error_messages={'required': 'Please enter your first name.'}
    )
    lastname = forms.CharField(
        label=('Last Name'),
        required=True,
        error_messages={'required': 'Please enter your last name.'}
    )
    email = forms.EmailField(
        label=('Email Address'),
        required=True,
        error_messages={'required': 'Please enter a valid email address.'}
    )
    subject = forms.CharField(
        label=('Subject'),
        required=True,
        error_messages={'required': 'Please enter a subject line.'}
    )
    message = forms.CharField(
        label=('Message'),
        min_length=4,
        widget=forms.Textarea,
        required=True,
        error_messages={'min_length': 'Your message is too short.'}
    )
