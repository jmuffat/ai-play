import os
import re
import email
import traceback

def parseDate(email_data):
    s = email_data.get('Date')
    if s==None: return None

    try:
        return email.utils.parsedate_to_datetime(s)
    except:
        print("bad date={0}".format(s))
        return None

def initdb(db):

    schema_path = os.path.join( os.path.dirname(__file__), "schema")

    def run_step(filename):
        with open(os.path.join(schema_path,filename)) as f: sql = f.read()
        return db.execute(sql)

    steps = [f for f in os.listdir(schema_path) if os.path.isfile(os.path.join(schema_path, f))]
    steps.sort()

    step1 = steps.pop(0)
    ver = ( run_step(step1).fetchall() )[0][0]

    print("DB schema update (cur:{0}):".format(ver))
    for step in steps:
        x = re.findall("^(\\d+)-(.*)\\..*$", step)[0]
        i = int(x[0])
        if (ver<i):
            print("  step {0}: {1}".format(i,x[1]))
            db.execute("BEGIN TRANSACTION")
            run_step(step)
            db.execute("UPDATE ver SET ver_value=$new_ver WHERE ver_id='db'", {"new_ver": i})
            db.execute("COMMIT")
    
    print("DB schema up to date")

def save_message(db, email_data):
    id = email_data.get("Message-ID")

    exists = db.execute("SELECT msg_id FROM message WHERE msg_id=$id",{"id":id}).fetchall()
    if len(exists)>0: return

    # ---
    subject = "(not found)" # default value, in case exception gets raised
    try:
        subject = email_data.get('Subject')
        timestamp = parseDate(email_data)
        labels = email_data.get('X-Gmail-Labels') or ""

        addresses = []
        def push_address(x,rel):
            dec = re.findall("^(.*?)\\s*<(.+)>$",x)
            if (len(dec)):
                addresses.append({"id":id,"rel":rel,"address":dec[0][1],"alias":dec[0][0]})
            else:               
                addresses.append({"id":id,"rel":rel,"address":x,"alias":None})

        for x in email_data.get_all("From",[]):    push_address(x,"from")
        for x in email_data.get_all("To",[]):      push_address(x,"to")
        for x in email_data.get_all("Cc",[]):      push_address(x,"cc")

    except Exception as e:
        print('.oO(')
        print('    (!) Error parsing "{0}", id={1}'.format(subject,id))
        traceback.print_exc()
        print()
        print(')Oo.')
        return
    
    # ---
    db.execute("BEGIN TRANSACTION")

    db.execute(
        """
            INSERT INTO message(msg_id,msg_date,msg_subject)
            VALUES($id,$date,$subject)
        """, 
        {"id":id,"date":timestamp,"subject":subject}
    )

    db.executemany(
        """
            INSERT INTO message_label(mlb_message,mlb_label)
            VALUES ($id,$label)
        """, 
        [{"id":id,"label":label} for label in labels.split(',')]
    )
    
    db.executemany("""
        INSERT OR IGNORE INTO message_address(mad_message,mad_rel,mad_address,mad_alias)
        VALUES ($id,$rel,$address,$alias)
    """, addresses)

    db.execute("COMMIT")

