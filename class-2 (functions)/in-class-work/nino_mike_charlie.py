### Customer emails

#Given a sequence containing dictionaries with customers with the following form:

    customer = {
        'name': 'Jonh Doe',
        'age 45,
        'email': 'john@yahoo.com'
    }

# a. Write a function that extract just the emails from the sequence. It should return other sequence with the emails. Try returning a list and a tuple.

# b. Modifiy that function to accept an optional parameter `domain` which would just return emails from a given domain (for example _yahoo.com_)

# c. Modify that function to accept both a whitelist and a blacklist of domains.

# * Use List Comprehensions for all three examples.

# Charlie's Attempt:

# a. Write a function that extract just the emails from the sequence. It should return other sequence with the emails. Try returning a list and a tuple.

def extract_emails(customers):
    
    emails = [person['email'] for person in customers]
    return emails

# b. Modifiy that function to accept an optional parameter `domain` which would just return emails from a given domain (for example _yahoo.com_)

def extract_emails2(customers, domain= None):
    emails = [person['email'] for person in customers if (domain in person['email'])]
    return emails 

# Alternatively, don't know if this would work but it would allow multiple domain searches
def domain_check(domains_wanted, email):
    answer = False
    for domain in domains_wanted:
        if domain in email:
            answer = True
    return answer
    
def v2extract_emails2(customers, *args):
    domains_wanted = [domain for domain in args]
    emails = [person['email'] for person in customers if domain_check(domains_wanted, person['email'])]
    return emails

# c. Modify that function to accept both a whitelist and a blacklist of domains.

def email_exists(email):
    return len(email) > 0:

def extract_emails3(customers):
    emails = [person['email'] for person in customers if email_exists(person['email'])]
    return emails