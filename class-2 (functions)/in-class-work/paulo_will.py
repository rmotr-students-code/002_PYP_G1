# ### Customer emails

# Given a sequence containing dictionaries with customers with the following form:

#     customer = {
#         'name': 'Jonh Doe',
#         'age 45,
#         'email': 'john@yahoo.com'
#     }

"""
customers = [
    {'name': 'Jonh', 'age': 45, 'email': 'john@yahoo.com'},
    {'name': 'Doe', 'age': 45, 'email': 'john@yahoo.com'},
    {'name': 'Martin', 'age': 45, 'email': 'john@yahoo.com'},
]
"""

# a. Write a function that extract just the emails from the sequence. It should return other sequence with the emails. Try returning a list and a tuple.

def extract_emails(customers):
    return [itm['email'] for itm in customers]


# b. Modifiy that function to accept an optional parameter `domain` which would just return emails from a given domain (for example _yahoo.com_)

def extract_emails_yahoo(customers, domain):
    return [itm['email'] for itm in customers if domain in itm['email']]
    


# c. Modify that function to accept both a whitelist and a blacklist of domains.

# * Use List Comprehensions for all three examples.