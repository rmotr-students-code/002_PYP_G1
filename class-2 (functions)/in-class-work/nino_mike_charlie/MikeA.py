### Customer emails

#Given a sequence containing dictionaries with customers with the following form:

    customer = {
        'name': 'Jonh Doe',
        'age 45,
        'email': 'john@yahoo.com'
    }

#a. Write a function that extract just the emails from the sequence. It should return other sequence with the emails. Try returning a list and a tuple.

extract_emails = {key:value for key,value in customer.items() if key == 'email'}

#b. Modifiy that function to accept an optional parameter `domain` which would just return emails from a given domain (for example _yahoo.com_)

#c. Modify that function to accept both a whitelist and a blacklist of domains.

#* Use List Comprehensions for all three examples.