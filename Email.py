#Sending video and location as an attachment via email

#importing libraries
import smtplib
from email.mime.base import MIMEBase
from email.message import EmailMessage
from email import encoders
from os.path import basename

#define sender and recipient email addresses
sender = "sender@example.com" #senders email id
password = 'password'   #sender email password
#multiple recipient mail address
recipient = ["recipient_1@example.com","recipient_2@example.com","recipient_3@example.com"]

#create a message object and sets its headers
message = EmailMessage()
message['From'] = sender
message['To'] = recipient
message['Subject'] = 'CODE BLUE [ EMERGENCY (SOS) ]'
message.set_content('Its an Emergency. Please respond fast!!. I am attaching you the gps location and an video file')

#.....Attaching video and location file.....

# 1] Attaching Video file

with open('Video_Output.mp4','rb') as attachment:

    video_part = MIMEBase('application','octet-stream')
    video_part.set_payload(attachment.read())
    video_name = attachment.name

    #encode the video file
    encoders.encode_base64(video_part)
    video_part.add_header('content-Disposition','attachment',filename = 'Video_Output.mp4')
    
message.add_attachment(video_part, maintype='video', filename= video_name)

# 2] Attaching Location file

with open('GPS_Location.txt','r') as f:
    file_data = f.read()
    file_name = f.name

message.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=file_name)

#sending email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender,password)
    smtp.send_message(message)