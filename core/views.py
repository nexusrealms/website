from os import environ
from core.forms import ContactForm
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages

def index(request):

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            sender = environ.get('AWS_SES_DEFAULT_SENDER')
            recipient = environ.get('AWS_SES_DEFAULT_RECIPIENT')
            html_message = render_to_string(
                'home/mail/contact.html',
                {
                    'firstname': firstname,
                    'lastname': lastname,
                    'email': email,
                    'message': message,
                }
            )
            plain_message = strip_tags(html_message)
            send_mail(
                subject,
                plain_message,
                sender,
                [recipient],
                html_message=html_message,
            )

            messages.success(request, 'Your message has been delivered!')
            return redirect('/')

    return render(request, 'home/index.html', {'form': form})

def announcements(request):
    '''Binds URL and returns announcements'''
    return render(request, 'home/announcements.html')

def policies(request):
    '''Binds URL and returns policies'''
    return render(request, 'home/policies.html')

def terms_conditions(request):
    '''Binds URL and returns terms and conditions'''
    return render(request, 'home/terms-conditions.html')
