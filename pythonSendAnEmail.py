import smtplib

sender = "mitorehadapauri@gmail.com"
receiver = "anushkasinha@gmail.com"
password = "password123"
subject = "python send an email"
body = "I send an email with the help of Python! : D"
# header
message = f"""From:{sender}
To:{receiver}
Subject: {subject}\n
{body}

"""

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
try:
    server.login(sender,password)
    print("Logged in...........")
    server.sendmail(sender,receiver,message)
    print("Email has been sent")
except smtplib.SMTPAuthenticationError:
    print("Unable to sign in!")