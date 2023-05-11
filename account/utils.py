from django.core.mail import send_mail
from decouple import config


def send_activation_code(email: str, code: str):
 message = ""
 html = f"""
<h1>для активации нажмите на кнопку</h1>
<a href="{config('LINK')}api/v1/account/activate/{code}">
<button>Activate</button>
</a>
"""
 send_mail(
  subject="Активация аккаунта",
  message=message,
  from_email="a@gmail.com",
  recipient_list=[email],
  html_message=html
 )

