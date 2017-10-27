# for gmail or google apps
EMAIL_USE_TLS= True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'djangotests123@gmail.com'
EMAIL_HOST_PASSWORD = 'Cmtests123'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
