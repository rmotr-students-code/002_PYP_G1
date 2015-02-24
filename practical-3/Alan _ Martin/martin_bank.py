class TransactionError(Exception):
    pass

# Abstract class which contains all basic account functions
class Account(object):
    def __init__(self, number, balance):
        self.number = number
        self.balance = 0
        self.history = []
    
    def deposit(self, amount):
        if isinstance(amount, int):
            try:
                self.balance += amount
                self.history.append('Deposit ${}'.format(amount))
            except TypeError:
                print "Please enter a number"
    
    def withdraw(self, amount):
        raise NotImplementedError("This has to be implemented in the subclasses")

    def show_balance(self):
        self.history.append(('Checked Balance'))
        print ('Account #{} balance: {}'.format(self.number,self.balance))

    def print_history(self):
        for item in self.history:
            print item
    
    def transfer(self, amount, destination_account):
        if self.balance >= amount:
            self.balance -= amount
            destination_account.balance += amount
            self.history.append('transfered ${} to account #{}'.format(amount, destination_account.number))
            destination_account.history.append('received ${} from account#{}'.format(amount, self.number))
            
        else:
            raise TransactionError("TransactionError")

class SavingsAccount(Account):
    def __init__(self, number, balance):
        super(SavingsAccount, self).__init__(number, balance)
        
    def add_interest(self,interest_rate, term_len):
        interest=self.balance * (interest_rate*(term_len/12))
        self.balance=self.balance + interest
        self.history.append("Added ${} in concept of interest".format(interest))

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(('Withdraw ${}'.format(amount)))
            return amount
        else:
            raise TransactionError("TransactionError:Insufficient funds") 

class CurrentAccount(Account):
    def __init__(self, number, balance, overdraft_limit):
        super(CurrentAccount, self).__init__(number,balance)
        self.overdraft_limit=overdraft_limit
        
    def withdraw(self,amount):
        if amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            self.history.append(('Withdrawal ${}'.format(amount)))
            return amount
        else:
            raise TransactionError("TransactionError: Overdraft limit exceeded")



       
sa = SavingsAccount(number="321", balance=0)
ca=CurrentAccount(number="123", balance=0, overdraft_limit=1000)

    
"""
account_list = [acc1, acc2, acc3]
for acc in account_list:
    acc.withdraw()

"""