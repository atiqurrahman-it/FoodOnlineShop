
from __future__ import print_function

from cgi import print_directory

from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, message
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


def send_varification_email(request,user,mail_subject,email_template):
    current_site = get_current_site(request)

    message = render_to_string(email_template,{
        'user': user, # user meens current user 
        'domain': current_site.domain,

        'uid':urlsafe_base64_encode(force_bytes(user.id)), # or 'uid': user.id, 

        'token': default_token_generator.make_token(user), # token.py inport account_activation_token
    })
    # print("to email ")
    to_email =user.email # or if view file  request.POST['email']
    # print(to_email)

    from_email=settings.DEFAULT_FROM_EMAIL
    mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
    mail.content_subtype = "html"
    mail.send()

    print('sucessfyully emailsend ')
 
    # return HttpResponse("thanks for registertion send code your email ")



