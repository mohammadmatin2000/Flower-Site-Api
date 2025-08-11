from django.core.mail import send_mail

send_mail(
    'Test Email',
    'This is a test email.',
    'mohammadmatin13872008@gmail.com',
    ['your_email@example.com'],
    fail_silently=False,
)
