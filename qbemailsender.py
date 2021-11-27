import datetime
import smtplib
from email.message import EmailMessage

senderEmail = "pingryquizbowl@gmail.com"
senderPassword = "S1mplep@ss"

receiversList = [] # fill this array with any email addresses you want to add to your email list (remember to make them strings tho)

todaysDate = datetime.datetime.now()

fo = open("finalemail.html", "r")
emailText = fo.read()
fo.close()

message = EmailMessage()
message["Subject"] = "Pingry Quizbowl Question of the Day for " + str(todaysDate.month) + "/" + str(todaysDate.day) + "/" + str(todaysDate.year)
message["From"] = senderEmail
message["To"] = receiversList
message.set_content(emailText, subtype = "html")

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(senderEmail, senderPassword)
    smtp.send_message(message)
