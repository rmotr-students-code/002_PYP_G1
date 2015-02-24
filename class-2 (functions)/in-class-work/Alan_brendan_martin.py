'''
### Customer emails

Given a sequence containing dictionaries with customers with the following form:

    customer = {
        'name': 'Jonh Doe',
        'age 45,
        'email': 'john@yahoo.com'
    }

a. Write a function that extract just the emails from the sequence.
It should return other sequence with the emails. Try returning a list and a tuple.

b. Modifiy that function to accept an optional parameter `domain` which would just return emails
from a given domain (for example _yahoo.com_)

c. Modify that function to accept both a whitelist and a blacklist of domains.

d. Move all this fun stuff into an anonymous function

* Use List Comprehensions for all three examples.
'''
#///////////////MARTIN's CODE///////////////////////////////////////////////////
#result = lambda dic, domaine="@" :[x["email"] for x in dic if (domaine in x["email"])]

#[operation for elem in list if condition]

#def customer_email(dic, domaine="@"):
#    return [x["email"] for x in dic if (domaine in x["email"])]

#print customer_email(customer,"hotmail")
#print customer_email(customer,"yahoo")
#print result(customer, "yahoo")
my_people = [
    {"id":111,
    "name":"John Baker",
    "email":"JohnB@hotmail.com"},
    {"id":333,
    "name":"Jim Jones",
    "email":"Jimmy@gmail.com"},
    {"id":444,
    "name":"Stan Yoda",
    "email":"yoda@gmail.com"}
    ]
    

badies = ["yoda@gmail.com", "Jimmy@gmail.com"] # the blacklist

#lambda returns email address if it's not in the blacklist
result = lambda customer_list, blacklist=[]: [items['email'] for items in customer_list if items['email'] not in blacklist]
    
print result(my_people, badies)

#////////////////////////////////////////////////////////////////////////////////////////////

def customer_email(dic):
    mylist = [dic[x]['email'] for x in dic]    
    print mylist
    
    #[mylist.append(dic['email']) for dic['email'] in dic]
    
    #for dict1 in dic:
    #mylist = [(dict1['email']) for x in dict1 if x == 'email']
    #return mylist
    

customer = [{'name': 'Jonh Doe', 'age' : 45, 'email': 'john@hotmail.com'}, {'name': 'Ben', 'age' : 12, 'email': 'ben@yahoo.com'}]

customer_email(customer)


#Brendan's Code:

#a) 

def customer_emails(customers):
    emails = [x['email'] for x in customers]
    print emails

customer_emails([{'name':'John', 'age':45, 'email':'john@yahoo.com'}, {'name':'Ben', 'age':42, 'email':'ben@yahoo.com'}, {'name':'Alex', 'age':1, 'email':'alex@yahoo.com'}])

#b)

def customer_emails(customers, domain = None):
    emails = [x['email'] for x in customers if domain in x['email'] or domain == None]
    print emails

customer_emails([{'name':'John', 'age':45, 'email':'john@yahoo.com'},
                 {'name':'Ben', 'age':42, 'email':'ben@yahoo.com'},
                 {'name':'Alex', 'age':1, 'email':'alex@hotmail.com'},
                 {'name':'Josh', 'age':2, 'email': 'josh@google.com'}], '@google.com')
                 
                 

##########~~~~~~~~~ \\/\/\\*** Alan's Code ***//\/\// ~~~~~~~~~############:

def customer_email(dic):
    """ Returns customer emails from list of customers & info"""
        emails = [dic[x]['email'] for x in range(len(dic))] 
    return emails
    
    
def customer_email2(dic, domain=""):
    """ Returns customer email, with option to filter by email service"""
    emails = [x['email'] for x in dic if domain in x['email']]
    return emails
    
#lambda function which returns emails or emails by service    
emails = lambda dic, domain="": [x['email'] for x in dic if domain in x['email']]

#test
#print emails(customer_emails)