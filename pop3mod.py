from base64 import decode
import email
from email.header import decode_header
import getpass, poplib

Mail = poplib.POP3('pop3.seznam.cz')
# Mail.user(getpass.getuser())
# Mail.pass_(getpass.getpass())
Mail.user("p717@post.cz")
Mail.pass_(".Kocicka1")
numMailessages = len(Mail.list()[1])
print(f"počet zpráv: {numMailessages}")

cmd=1
if cmd==1:
    for i in range(numMailessages):
        n=0
        # vypíše jednotlivé řádky 
        for msg in Mail.retr(i+1)[1]:  # rozdelí zprávu na řádky
            n=n+1
            print(n,": ",msg)

elif cmd==2:
    for i in range(numMailessages):
        # rozlož zprávu
        for msg in Mail.retr(i+1)[1]:  # rozdelí zprávu na řádky
            
            if "Subject" in  msg:
                print(msg)
        # eml=email.message_from_bytes(msg)
        # email.message_from_string
        # decode
        #subject, encoding =decode_header(eml["Subject"])[0]
        #print(subject)
        
