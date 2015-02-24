customers = [
    {"id":111,
    "name":"John Baker",
    "email":"JohnB@hotmail.com"},
    {"id":333,
    "name":"Jim Jones",
    "email":"Jimmy@gmail.com"},
    {"id":444,
    "name":"Stan Yoda",
    "email":"yoda@yahoo.com",
    "email":"yoda1@yahoo.com"}
]

# b. Modifiy that function to accept an optional parameter `domain` which would just return emails
# from a given domain (defaults to _yahoo.com_)
# b.1: Find a way to include an optional paramter.
# b.2: Filter the list.

def get_email(x):
    return x['email']


def customer_emails(customers, domain=None):
    #my_list = [get_email(x) for x in customers if should_be_included(get_email(x), domain)]

    my_list = []
    for customer in customers:
        cust_email = get_email(customer)
        if should_be_included(cust_email, domain):
            my_list.append(cust_email)
    return my_list

def should_be_included(email, domain):
    if is_string_included(email, domain):
        return True


def is_string_included(email, domain):
    return domain in email # Should return True or False
    # Alternatively can accept a list of domains
    # return any([(domain in email) for domain in domains])

x = 'A' in 'ABC'
y = 'Z' in 'ABC'
print(x)
print(y)

[^@]+@[^@]+\.[^@]+ 