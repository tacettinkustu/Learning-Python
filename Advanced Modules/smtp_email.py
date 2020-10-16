import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

message = MIMEMultipart()

message["From"] = "tcttnkst@gmail.com"

message["To"] = "ttkustu@gmail.com"

message["Subject"] = "Sending smtp email"


content = """

I am sending you an email.

Tacettin Kustu


"""


message_content = MIMEText(content,"plain")

message.attach(message_content)

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)

    mail.ehlo()

    mail.starttls()

    mail.login("tcttnkst@gmail.com","**********#emailpassword************")

    mail.sendmail(message["From"],message["To"],message.as_string())

    print("Sending email is successful....")

    mail.close()

except:
    sys.stderr.write("An error occured!")
    sys.stderr.flush()
