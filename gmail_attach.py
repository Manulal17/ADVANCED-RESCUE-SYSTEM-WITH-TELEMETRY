import smtplib
from email.mime.multipart import MIMEMultipart#from email.MIMEMultipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 
fromaddr = "ezine.pravysoft@gmail.com"
toaddr = "info.pravysoft@gmail.com"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "PravySoft Calicut"
 
body = "Hi, Be carefull. An unknown activity was found!.Please see attached picture"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "praveen.txt"
attachment = open("C:\\Users\\Praveen\\Desktop\\python\\praveen.txt", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "1!myambalaprav")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()