# Exception Messages 
class TransactionError(Exception):
    pass

class OverdraftError(Exception):
    pass


class Account(object):
    
    def __init__(self, account, current_balance=0):
        self.account = account
        self.current_balance = current_balance
        created_at_message = "Account {} was created.".format(account)
        self.transaction_history = [created_at_message]
        

    def __unicode__(self):
        return self.account
    
    def __str__(self):
        return self.account

    def deposit(self, deposit_amount):
        self.current_balance += deposit_amount
        deposit_message = "Deposited ${0:.2f}".format(deposit_amount)
        current_balance_message = "Current balance: ${0:.2f}.".format(self.current_balance)
        self.transaction_history.append(deposit_message)
        self.transaction_history.append(current_balance_message)
        
    def show_balance(self):
        self.transaction_history.append("Checked Balance.")
        print("${0:.2f}".format(self.current_balance))

    def show_transaction_history(self):
        self.transaction_history.append("Asked for transaction history.")
        print("Account {}'s history is as followed:".format(self.account))
        print("*"*50)
        for event in self.transaction_history:
            print(event)
        print("*"*50)        
                
    def withdraw(self, amount):
        if amount > self.current_balance:
            failed_withdraw_message = "Failed to withdraw ${0:.2f} due to insufficient funds.".format(amount)
            current_balance_message = "Current balance: ${0:.2f}.".format(self.current_balance)
            self.transaction_history.append(failed_withdraw_message)
            self.transaction_history.append(current_balance_message)
            raise TransactionError("You have insufficient funds for that request.")
        else:
            self.current_balance -= amount
            withdraw_message = "Withdrew ${0:.2f}.".format(amount)
            current_balance_message = "Current balance: ${0:.2f}.".format(self.current_balance)
            self.transaction_history.append(withdraw_message)
            self.transaction_history.append(current_balance_message)
                 
    def __accept_transfer(self, amount, sender):
        self.current_balance += amount
        accept_transfer_message = "You have accepted a money transfer of ${0:.2f} from account {1}.".format(amount, sender)
        current_balance_message = "Current balance: ${0:.2f}.".format(self.current_balance)
        self.transaction_history.append(accept_transfer_message)
        self.transaction_history.append(current_balance_message)
    
    def transfer(self, amount, destination_account):
        # Chose not to use the withdraw() methods to have customized messages for the history.
        # using the withdraw() method would add a withdraw item to the history instead of a transfer message.
        if amount > self.current_balance:
            failed_transfer_message = "You have failed to make a transfer due to insufficient funds."
            self.transaction_history.append(failed_transfer_message)
            raise TransactionError("You do not have the neccesary funds to make that transfer")
        else:
            self.current_balance -= amount
            destination_account.__accept_transfer(amount, self.account)
            success_transfer_message = "You have made a ${0:.2f} transfer to account {1}.".format(amount, destination_account)
            current_balance_message = "Current balance: ${0:.2f}.".format(self.current_balance)
            self.transaction_history.append(success_transfer_message)
            self.transaction_history.append(current_balance_message)
    

class SavingAccount(Account):

    # Need to incorporate months by tracking time. 
    # Something along the lines of every month:
    #   Check current balance
    #   Find interest and add to current balance
    #   add interest_message to notify user
    
    def add_interest(self, yearly_interest_rate, months):
        interest = self.current_balance * yearly_interest_rate
        self.current_balance += interest
        interest_message = "Added ${0:.2f} in concept of interest.".format(interest)
        self.transaction_history.append(interest_message)
        

class CurrentAccount(Account):
    
    def __init__(self, account, overdraft_limit, current_balance=0):
        # similar to super()?
        Account.__init__(self, account, current_balance)
        self.overdraft_limit = overdraft_limit
        created_at_message = "Account {} was created.".format(account)
        self.transaction_history = [created_at_message]

    def withdraw(self, amount):
        
        # is this even allowed? embedded methods?
        def successful_withdrawal(amount):
            self.current_balance -= amount
            withdraw_message = "Withdrew ${0:.2f}.".format(amount)
            current_balance_message = "Current balance: ${0:.2f}.".format(self.current_balance)
            self.transaction_history.append(withdraw_message)
            self.transaction_history.append(current_balance_message)

        if self.current_balance < amount:
            if self.current_balance - amount < -(self.overdraft_limit):
                overdraft_message = "Overdraft limit reached, withdrawal amount of ${0:.2f} could not be processed.".format(amount)
                current_balance_message = "Current balance: ${0:.2f}.".format(self.current_balance)
                self.transaction_history.append(overdraft_message)
                self.transaction_history.append(current_balance_message)
                raise OverdraftError("You have reached your overdraft limit!")
            else:
               successful_withdrawal(amount)
        else:
            successful_withdrawal(amount)
    
            
# Tests            
sample_account = CurrentAccount('001', 1000, 0)

assert sample_account.account == '001'
assert sample_account.overdraft_limit == 1000
assert sample_account.current_balance == 0

sample_account.deposit(1500)
assert sample_account.current_balance == 1500

sample_account.withdraw(2000)
assert sample_account.current_balance == -500

# how to check to see if an exception was raised
# assert sample_account.withdraw(501) == raise OverdraftError("You have reached your overdraft limit!")
try:
    sample_account.withdraw(501)
except OverdraftError:
    print("OverdraftError seems to work!")

sample_savings = SavingAccount('002', 5000)

assert sample_savings.account == '002'
assert sample_savings.current_balance == 5000

sample_savings.deposit(500)
assert sample_savings.current_balance == 5500

sample_savings.withdraw(2000)
assert sample_savings.current_balance == 3500

#sample_savings.show_transaction_history()
assert len(sample_savings.transaction_history) == 5 # does not include show_transaction_history message

#sample_account.show_transaction_history()
assert len(sample_account.transaction_history) == 7 # ditto

sample_savings.add_interest(0.1, 12)
assert sample_savings.current_balance == 3850.00

sample_savings.transfer(2000, sample_account)
assert sample_account.current_balance == 1500
assert sample_savings.current_balance == 1850

# sample_savings.withdraw(50000000000) == raise Error
try: 
    sample_savings.withdraw(50000000)
except TransactionError:
    print("TransactionError also seems to work!")
print("#" * 50)
print('\n')

sample_account.show_transaction_history()
print('\n')
sample_savings.show_transaction_history()

