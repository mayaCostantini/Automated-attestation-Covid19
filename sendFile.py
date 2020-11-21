import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email import encoders
import time 


def sendFile() : 
    currentTime = time.localtime()

    mailContent = f'Hello, here is your attestation for the {currentTime.tm_mday}/{currentTime.tm_mon}/{currentTime.tm_year}, {currentTime.tm_hour}h{currentTime.tm_min}.'

    senderAddress = 'your.sender.email@gmail.com'
    senderPassword = 'xxxxxxxxxxx'
    receiverAddress = 'your.receiver.email@gmail.com'

    message = MIMEMultipart()
    message['From'] = senderAddress
    message['To'] = receiverAddress
    message['Subject'] = 'Attestation de déplacement Covid-19'

    message.attach(MIMEText(mailContent, 'plain'))

    with open('./attestations/attestation.pdf', 'rb') as f : 
        attach = MIMEApplication(f.read(),_subtype="pdf")

    attach.add_header('Content-Disposition','attachment',filename=str('./attestations/attestation.pdf'))
    message.attach(attach)

    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.ehlo()
    session.login(senderAddress, senderPassword) #login with mail_id and password
    session.ehlo()
    text = message.as_string()
    session.sendmail(senderAddress, receiverAddress, text)
    session.quit()
    print('Mail Sent')
