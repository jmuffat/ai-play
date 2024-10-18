import os
from pathlib import Path
import duckdb

from cmn_mail import MboxReader
from cmn_maildb import initdb,save_message

def run():
    Path("output").mkdir(exist_ok=True)

    db = duckdb.connect("output/test-maildb.db")
    initdb(db)

    mboxPath = os.path.expanduser("~/Downloads/Takeout/all-mails.mbox")

    i = 0
    with MboxReader(mboxPath) as mbox:
        for message in mbox:
            if i%100 == 0: print('-=-=-=- Parsing email {0} -=-=-=-'.format(i))
            save_message(db,message)

            i=i+1
            # if i>=100: break 

    db.close()

    print("done.")
