
#send_email("hello", 3, "universe", 1987)

def send_email_1(**kwargs):
    title = kwargs['title']
    copies = kwargs['copies']
    template = kwargs['template']
    year = kwargs['year']

def send_email_2(title=None, copies=None, template=None, year=None):
    pass

#send_email(title="hello", copies=3, template="universe", year=1987)