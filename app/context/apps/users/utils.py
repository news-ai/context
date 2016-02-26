from .models import Company, UserProfile


def check_company_auth(strategy, details, user=None, *args, **kwargs):
    print user
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