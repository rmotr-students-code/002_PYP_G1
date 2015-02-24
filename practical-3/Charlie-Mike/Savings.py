import Account

class SavingAccount(Account):


    def __init__(self, account_number, initial_money=0):
        self.account_number = account_number
        self.initial_money = initial_money
        self.transaction_history = []
        
        
    def deposit(self, deposit_amount):
        self.initial_money += deposit_amount
        deposit_message = "Deposited ${}".format(deposit_amount)
        self.transaction_history.append(deposit_message)
    
    
    def show_balance(self):
        self.transaction_history.append("Shown Balance")
        return self.initial_money
        
        
    def show_transaction_history(self):
        self.transaction_history.append("Asked for transaction history")
        
        for event in self.transaction_history:
            print(event)
    
    
    def transfer(self, amount, destination_account):
        if amount > self.initial_money:
            failed_transfer_message = "You have failed to make a transfer."
            self.transaction_history.append(failed_transfer_message)
            print("You do not have the neccesary funds to make that transfer")
        else:
            destination_account.initial_money += amount
            self.initial_money -= amount
            success_transfer_message = "You have made a ${} transfer to {}".format(amount, destination_account)
            self.transaction_history.append(success_transfer_message)
    
    
    def add_interest(self, yearly_interest_rate, months):
        interest = self.initial_money * yearly_interest_rate
        self.initial_money += interest
        interest_message = "Added ${0:.2f} in concept of interest.".format(interest)
        
        self.transaction_history.append(interest_message)