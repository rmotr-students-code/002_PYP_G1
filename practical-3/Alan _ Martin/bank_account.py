#Savings account:
#attributes= acct number, initial money
#methods = add_interest(yearly_interest rate, months), deposit, 
#           show_balance, show transaction history
           
#Current Account:
# attributes = account number, inital money, overdraft limit
# methods = deposit, withdraw, show balance, transfer(amt, destination acct)



#Generic Account(abstract): 

class Account(object):
    def __init__(self, number, balance):
        self.number = number
        self.balance = 0
        self.history = []
    
    def deposit(self, amount):
        if isinstance(amount, int):
            try:
                self.balance += amount
                self.history.append('You have Deposit {}'.format(amount))
            except TypeError:
                print "Please enter a number"
    
    def withdraw(self, amount):
        raise NotImplementedError("This has to be implemented in the subclasses")
        """
        if hasattr(self, 'overdraft_limit'):
            if amount <= (self.balance + self.overdraft_limit):
                self.balance -= amount
                self.history.append(('Withdrawal', amount))
                return amount
            else:
                print "TransactionError: Overdraft limit exceeded"
        else:
            if amount <= self.balance:
                self.balance -= amount
                self.history.append(('Withdrawal', amount))
                return amount
        """
    
    def show_balance(self):
        self.history.append(('Checked Balance'))
        print self.balance

    def print_history(self):
        for item in self.history:
            print item
    
    
    def transfer(self, amount, destination_account):
        pass #incomplete



class SavingsAccount(Account):
    def __init__(self, number, balance):
        super(SavingsAccount, self).__init__(number, balance)
        
    def add_interest(self,interest_rate, term_len):
        
        interest = self.balance * (interest_rate*(term_len/12))
        self.balance = self.balance + interest

            

class CurrentAccount(Account):
    def __init__(self, number, balance, overdraft_limit):
        super(CurrentAccount, self).__init__(number,balance)
        self.overdraft_limit = overdraft_limit
        
sa = SavingsAccount(number="123", balance=0)
sa.deposit(1000)
sa.add_interest(0.1,12)
sa.show_balance()


account_list = [acc1, acc2, acc3]
for acc in account_list:
    acc.withdraw()


sa.withdraw()
ca.withdraw()