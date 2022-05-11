# from smtplib import SMTP
# from ..config import Config

# sender = Config.MAIL_USERNAME
# password = Config.MAIL_PASSWORD
# domain = Config.EMAIL_SERVER

# def send_message(username,email):
#     receiver = email
#     message = f'Welcome to Pitch perfect. We make Your pitches perfect.'
#     subject = 'Welcome'
#     with SMTP(domain) as conn:
#         conn.starttls()
#         conn.login(user=email, password=password)
#         conn.sendmail(
#             from_addr=email,
#             to_addrs=receiver,
#             msg=f"Subject:{subject}\n\n{message}"
#         )
