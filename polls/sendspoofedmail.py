# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import smtplib

# fromaddr = "weiyuxinexponential@gmail.com"
# toaddr = "weiyuxin100@gmail.com"
# msg = MIMEMultipart()
# msg['From'] = fromaddr
# msg['To'] = toaddr
# msg['Subject'] = "Python email Subject"
# body = "Python test mail body"
# msg.attach(MIMEText(body, 'plain'))
# print(str(msg) + " message assigned")

# server = smtplib.SMTP('mail.smtp2go.com', 25)
# print("server entered")
# server.ehlo()
# print("ehlo complete")
# server.starttls()
# print("starttls complete")
# server.ehlo()
# print("ehlo 2 complete")
# server.login("weiyuxinexponential@gmail.com", "mcONLINE123")
# print("server login success")
# text = msg.as_string()
# print("text set as: " + str(text))
# print("text end")
# server.sendmail(fromaddr, toaddr, text)
# print("email sent!")



# from smtp2go.core import Smtp2goClient
# SMTP2GO_API_KEY="api-D887B4D6FDDB11E897EDF23C91C88F4E"
# smtp2go_client = Smtp2goClient(api_key=SMTP2GO_API_KEY)
# client = Smtp2goClient()
# payload = {
#     'sender': 'dave@example.com',
#     'recipients': ['matt@example.com'], 
#     'subject': 'Trying out Smtp2go!', 
#     'text': 'Test Message', 
#     'html': '<html><body><h1>Test HTML message</h1></body><html>', 
#     'custom_headers': {'Your-Custom-Headers': 'Custom Values'}
#     }
# response = client.send(**payload)
# response.success


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = 'weiyuxinexponential@gmail.com'
password = 'mcONLINE123'
msg = MIMEMultipart('mixed')

sender = 'sender@example.com'
recipient = 'weiyuxin100@gmail.com'

msg['Subject'] = 'Your Subject'
msg['From'] = sender
msg['To'] = recipient

text_message = MIMEText('It is a text message.', 'plain')
html_message = MIMEText('It is a html message.', 'html')
msg.attach(text_message)
msg.attach(html_message)

mailServer = smtplib.SMTP('mail.smtp2go.com', 2525) # 8025, 587 and 25 can also be used. 
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login(username, password)
mailServer.sendmail(sender, recipient, msg.as_string())
mailServer.close()