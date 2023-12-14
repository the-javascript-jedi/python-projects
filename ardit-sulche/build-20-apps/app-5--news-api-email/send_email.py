import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "thejavascriptjedi77@gmail.com"
    password = "rmjcdimzxfdlesix"

    receiver = "nithinsam77@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
