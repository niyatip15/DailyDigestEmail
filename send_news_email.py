import smtplib,ssl,os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "niyupathak1503@gmail.com"
    app_password = os.getenv("PASSWORD")
    receiver = "niyupathak1503@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, app_password)
        server.sendmail(username, receiver, message)