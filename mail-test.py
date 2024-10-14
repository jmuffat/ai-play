# import shutil
from pathlib import Path
from mail import MboxReader, GmailMboxMessage

# shutil.rmtree("output")
Path("output").mkdir(exist_ok=True)

f = open("output/test2.txt", "w")

mboxPath = '/Users/jeromemuffat-meridol/Downloads/Takeout/all-mails.mbox' # "~/Downloads/Takeout/all-mails.mbox"

i = 0
with MboxReader(mboxPath) as mbox:
    for message in mbox:
        email = GmailMboxMessage(message)
        print('-=-=-=- Parsing email {0} -=-=-=-'.format(i))

        print('-=-=-=- Parsing email {0} -=-=-=-'.format(i), file=f)
        print(email.subject, file=f)
        print(email.labels, file=f)
        print(email.text, file=f)
        print("", file=f)

        i=i+1
        if i>=10: break 


f.close()
print("done.")
