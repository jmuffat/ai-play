import email
from email.policy import default
import bs4

def get_html_text(html):
    try:
        return bs4.BeautifulSoup(html, 'lxml').body.get_text(' ', strip=True)
    except AttributeError: # message contents empty
        return None

class GmailMboxMessage():
    def __init__(self, email_data):
        if not isinstance(email_data, email.message.EmailMessage):
            raise TypeError('Variable must be type email.message.EmailMessage, not <{0}>'.format(type(email_data)))

        self.raw = email_data
        self.id = email_data.get("Message-ID")
        self.date = email.utils.parsedate_to_datetime( email_data.get('Date') )
        self.sent_from = email_data.get('From')
        self.sent_to = email_data.get('To')
        self.subject = email_data.get('Subject')
        self.labels = email_data.get('X-Gmail-Labels')

        body = email_data.get_body(preferencelist=('plain', 'html'))
        text = ""
        if body: 
            content_type = body.get_content_type()
            if content_type=="text/plain":
                text = body.get_content()
            elif content_type=="text/html":
                text = get_html_text(body.get_content())
            else:
                text = body.get_content()
        
        self.text = text




class MboxReader:
    def __init__(self, filename):
        self.handle = open(filename, 'rb')
        assert self.handle.readline().startswith(b'From ')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.handle.close()

    def __iter__(self):
        return iter(self.__next__())

    def __next__(self):
        lines = []
        while True:
            line = self.handle.readline()
            if line == b'' or line.startswith(b'From '):
                yield email.message_from_bytes(b''.join(lines), policy=default)
                if line == b'':
                    break
                lines = []
                continue
            lines.append(line)