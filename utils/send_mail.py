import smtplib, ssl
import os



def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "be.app.mailer@gmail.com"
    password = os.getenv("MAILER_PASSWORD")
    receiver = "be.app.mailer@gmail.com"

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


