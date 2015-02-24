# # Bank system
# Create a class hierarchy for a bank system. SavingsAccount and CurrentAccount class must
# inherit from Account abstract class. Both classes must implement needed attributes and methods
# as required by the following usage sample:

class Account(object):
   """ def __init__(self, number, initial_money):
        self.number = number
        self.initial_money = initial_money
        self.balance = 0
        """
    pass

class SavingsAccount(Account):
    
    def __init__(self, number, initial_money):
        #super(SavingsAccount, self).__init__(number, initial_money)
        self.initial_money = initial_money
        self.number = number
        self.balance = 0
        self.interest_made = interest_made
        self.deposit_list = []

    def deposit(self, amount):
        self.deposit_list.append(amount)
        self.balance += amount 
        #return self.balance + amount #what exists + deposit -> must iterate, otherwise won't change the variable
        return balance
        
    def add_interest(self, yearly_interest_rate, months):
        self.interest_made = self.balance * yearly_interest_rate / 12 * months
        self.balance += self.interest_made
        
        
    def show_balance(self):
        
        print 'Current Balance is {balance}'.format(balance=self.balance)
        
    def show_transaction_history(self):
        
        print 'Opened account number {number}\nDeposited ${deposits}\n\
            Added ${interest} in concept of interests\nShown balance\nAsked for \
            transaction history'.format(number=self.number,deposits=','.join(self.deposit_list), interest=self.interest_made)
            
        



class CurrentAccount(Account):
    def __init__(self, number, initial_money, overdraft_limit):
        super(CurrentAccount, self).__init__(number, initial_money, balance)
        self.overdraft_limit = overdraft_limit
    
    def deposit(self, amount):
        self.balance += amount
        return balance
    
    def withdraw(self, amount):
        if amount > balance:
            print "TransactionError: Overdraft limit exceeded"
        else:
            self.balance -= amount
        return balance
    
    def show_balance(self):
        print balance

# self, number, initial_money, balance, interest_made, deposit_list
sa = SavingsAccount(number="123", initial_money="0")
ca = CurrentAccount(number="123", initial_money="0", overdraft_limit=1000)
ca.deposit(5000)
ca.withdraw(5500)

sa.deposit(1000)
sa.transfer(amount=200, destination_account=ca)
sa.show_balance()
    

