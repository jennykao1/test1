import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

maillist = ["jennykao@outlook.com","kaoshr@gmail.com"]

for rec in maillist:

    msg = MIMEMultipart()
    msg["From"] =  "kaoshr@gmail.com"
    msg["To"] = "rec"
    msg["Subject"] = Header("Test email", "utf-8").encode()
    msg_content = MIMEText("Hello 👋，這是自動寄出的測試信件，祝你今天順利！","plain", "utf-8")
    msg.attach(msg_content)

    ssl_context = ssl.create_default_context()

    """
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl_context)
    server.login("kaoshr@gmail.com","psdp hhjt gstx gewx")
    server.sendmail("kaoshr@gmail.com","kaoshr@gmail.com",msg.as_string())
    server.close()"
    """
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl_context) as server:
        server.login("kaoshr@gmail.com","psdp hhjt gstx gewx")
        server.sendmail("kaoshr@gmail.com",rec,msg.as_string())

    print("success send mail")