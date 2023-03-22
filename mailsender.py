import smtplib as sm
from email.message import EmailMessage
import tkinter as tk
from tkinter import messagebox
import os
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
RECIEVER_MAIL = os.environ["RECIEVER_MAIL"]

print(EMAIL)
print(PASSWORD)
print(RECIEVER_MAIL)

def mail_send():
    
    msg=EmailMessage()
    msg["from"]=EMAIL
    msg["to"]=RECIEVER_MAIL
    msg["subject"]="this is the sample program with attacment"
    msg.set_content("mail with attachment!!!")
    fp=open("logged.txt","rb")
    data=fp.read()
    msg.add_attachment(data,maintype="text",subtype="octet-stream",filename="log.txt")
    mail=sm.SMTP('smtp.gmail.com',587)
    mail.starttls()
    mail.login(EMAIL,PASSWORD)
    # body="helooo"
    try:
        mail.sendmail(EMAIL,RECIEVER_MAIL,msg.as_string())
        print("msg sent")
        messagebox.showinfo(title="Success", message="Operation completed successfully.")
    except:
        print("error occured")
        messagebox.showinfo(title="Failed", message="Operation Faled.")
    mail.quit()
    return


