# send email with gmail smtp
# Required: Turn Allow less secure apps to ON => https://myaccount.google.com/lesssecureapps?pli=1

import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "your@gmail.com"  # Enter your address
receiver_email = "receiver@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ")
message = """\
Subject: Hi guy,

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)