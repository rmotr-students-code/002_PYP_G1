
# go for it I guess i start with savings and we can just keep cehcking the other's every now and the
# I'll make a small notes area for methods that overlap which we can put in the abstract class
#sounds good.
#ok
#I'm going to start building Current on a different page. I'll check your sheet every now and then
# sounds perfect. I'll keep the savings on here then 
#looks like at least account number and initial amount overlap
# true, i think continuing to write them out and then refactoring later might be better practice
# ok
# ok I think I finally got it
# awesome paste it here and we can smooth things out if we need to.
#I'm going to inherit account_number and initial_money
# yeah that sounds good. Would shorter variable names be better?
#like which ones?
#we both did this a little differently. There may be room for more overlapping methods. Let me take a look at your approach.
# better to  chat on slack. It's easier to keep track of what you're saying there



class TransactionError(Exception):
    pass


class Account(object):
    
    
    def __init__(self, account, initial_money=0):
        self.account = account
        self.initial_money = initial_money
        self.transaction_history = []


    def deposit(self, deposit_amount):
        self.initial_money += deposit_amount
        deposit_message = "Deposited ${0:.2f}".format(deposit_amount)
        self.transaction_history.append(deposit_message)
        
        
    def show_balance(self):
        self.transaction_history.append("Shown Balance")
        print("${0:.2f}".format(self.initial_money))


    def show_transaction_history(self):
        self.transaction_history.append("Asked for transaction history")
        if self.transaction_history:
            print("There are no events to report!")
        else:
            print("Your account history is as followed:")
            for event in self.transaction_history:
                print(event)
                
    def withdraw(self, amount):
        
             
    def transfer(self, amount, destination_account):
        # redo with separate withdraw methods
        # if amount > self.initial_money:
        #     failed_transfer_message = "You have failed to make a transfer."
        #     self.transaction_history.append(failed_transfer_message)
        #     raise TransactionError("You do not have the neccesary funds to make that transfer")
        # else:
        #     withdrawal()
        #     destination_account.deposit(amount)
        #     self.initial_money -= amount
        #     success_transfer_message = "You have made a ${0:.2f} transfer to {}".format(amount, destination_account)
        #     self.transaction_history.append(success_transfer_message)
    

class SavingAccount(Account):
    
    # This is the only thing different I can see that the savings account needs from the Account class. 
    # Also trying to figure out how to make the monthly accruement work. 
    def withdraw(self, amount):
        self.initial_money -= 
    
    def add_interest(self, yearly_interest_rate, months):
        interest = self.initial_money * yearly_interest_rate
        self.initial_money += interest
        interest_message = "Added ${0:.2f} in concept of interest.".format(interest)
        
        self.transaction_history.append(interest_message)
        

class CurrentAccount(Account):
    def __init__(self, account_number, initial_money, overdraft_limit):
        super(CurrentAccount, self).__init__(account_number, initial_money)
        self.overdraft_limit = overdraft_limit
        self.current_balance = initial_money
        self.deposit_amount = 0

    def deposit(self, current_deposit):
        self.current_balance += current_deposit
        self.deposit_amount += current_deposit
        return current_deposit

    def withdrawal(self, withdrawal, destination_account):
        if withdrawal <= self.current_balance:
            self.current_balance -= withdrawal
            destination_account.deposit(withdrawal)
            return "Withdrawal from account successful!"
        elif withdrawal > self.current_balance and withdrawal < (self.current_balance + self.overdraft_limit):
            self.overdraft_limit = self.overdraft_limit - self.current_balance - (withdrawal - self.current_balance)
            self.current_balance = 0
            destination_account.deposit(withdrawal)
            return "withdrawal from overdraft successful."
        else:
            raise TransactionError("You don't have enougth money in you account")


    def show_balance(self):
        return self.current_balance
    
    # Need transaction_history method if you want to keep using your return statements. 
