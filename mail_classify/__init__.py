import os
import shutil
import re
import textwrap

from pathlib import Path
from transformers import pipeline

from cmn_mail import MboxReader, GmailMboxMessage


def run():
    Path("output").mkdir(exist_ok=True)
    shutil.rmtree("output/mcls",ignore_errors=True)
    Path("output/mcls").mkdir()

    mboxPath = os.path.expanduser("~/Downloads/Takeout/all-mails.mbox")

    summarizer = pipeline("summarization", device="mps")

    i = 0
    with MboxReader(mboxPath) as mbox:
        for message in mbox:
            email = GmailMboxMessage(message)
            
            id = re.findall("<?(.*)?>",email.id)[0]
            print('-=-=-=- Parsing email {0} -=-=-=-'.format(id))

            summary = summarizer(email.text)
            summaryText = textwrap.wrap(summary[0].get("summary_text"))

            f = open("output/mcls/{0}.txt".format(id), "w")
            print(email.date, file=f)
            print(email.sent_from, file=f)
            print(email.sent_to, file=f)
            print(email.subject, file=f)
            print(email.labels, file=f)
            print("-=-=-=-=-=-=-=-=-=-=-", file=f)
            for s in summaryText: print(s, file=f)
            print("-=-=-=-=-=-=-=-=-=-=-", file=f)
            print(email.text, file=f)
            print("-=-=-=-=-=-=-=-=-=-=-", file=f)
            # print(message, file=f)
            f.close()

            i=i+1
            if i>=100: break 
