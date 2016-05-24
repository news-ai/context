# -*- coding: utf-8 -*-
# Third-party app imports
import sendgrid

# Imports from app
from .models import Company, UserProfile
from context.settings.secrets import SENDGRID_API_KEY

# Initializing SendGrid: created in order to send emails with SendGrid
# templates
sg = sendgrid.SendGridClient(SENDGRID_API_KEY)


def check_company_auth(strategy, details, user=None, *args, **kwargs):
    try:
        user_profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        user_profile = None

    # Find or create company domain
    split_email = details['email'].split('@')
    company_name = split_email[1].split('.')[0]
    company_profile, created = Company.objects.get_or_create(
        name=company_name,
        email_extension=split_email[1],
    )

    if not user_profile and details['email']:
        user_profile, created = UserProfile.objects.get_or_create(
            user=user,
            company=company_profile,
        )
    else:
        user_profile.company = company_profile
        user_profile.save()


def send_welcome_email(strategy, details, user=None, is_new=False, *args, **kwargs):
    print is_new
    if is_new:
        full_name = ' '.join((details['first_name'], details['last_name']))
        email = details['email']

        message = sendgrid.Mail()
        message.set_from('NewsAI <hello@newsai.org>')
        message.set_subject('Welcome to NewsAI!')
        message.set_text('Welcome to NewsAI!')

        if full_name and email:
            message.add_to(full_name + ' <' + email + '>')
            message.add_substitution('-fullname-', full_name)
            message.add_filter('templates', 'template_id',
                               '39e92d35-09a0-43a5-9629-03fcefecdc2b')
            status, msg = sg.send(message)
