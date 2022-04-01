import smtplib

sender = "senderGmail.com"
receiver = "reciever@gmail.com"
password = "password1234"
subject = "Python email text"
body = "I wrote an email! :D"

# header
message = f"""" From: {sender}
To: {receiver}
Subject: {subject}
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("Logged in ...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("unable to sign in")
