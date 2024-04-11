#this is for /full-auth-api/.env.local

DJANGO_SECRET_KEY = 'django-insecure-&r&ugrq9j5v%k64m5cc5(d85+pa1(9\*i5glwacb5hvc!dr&2!k'

#setup for dev debug
DEBUG="True"

# DJANGO_ALLOWED_HOST = '127.0.0.1,localhost'

#email settings for aws ses service
AWS_SES_FROM_EMAIL = ''

AWS_SES_ACCESS_KEY_ID = ''
AWS_SES_SECRET_ACCESS_KEY = ''
AWS_SES_REGION_NAME = ''

#email template context
DOMAIN = '127.0.0.1:3000'
SITE_NAME = 'FULL AUTH'

#email settings for google stmp
EMAIL_HOST_USER = 'sender.team.sender@gmail.com'
EMAIL_HOST_PASSWORD = 'ilcmiqpzjjzzeflk'

# CORS_ALLOWED_ORIGINS = ','

AUTH_COOKIE_SECURE = 'False'

GOOGLE_OAUTH_KEY = '17576906475-ivkn2m0a1sfrh11h2umbdb70h8nvne60.apps.googleusercontent.com'
GOOGLE_OAUTH_SECRET = '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'

REDIRECT_URIS = 'http://localhost:3000/auth/google,http://127.0.0.1:3000/auth/google'
