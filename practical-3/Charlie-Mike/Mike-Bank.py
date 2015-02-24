class Account(object):
    def __init__(self, account_number, initial_money):
        self.account_number = account_number
        self.initial_money = initial_money
        self.current_balance = initial_money
        self.transaction_history = []
        
    def deposit(self, current_deposit):
        self.current_balance += current_deposit
        deposit_message = "${} deposit.".format(current_deposit)
        self.transaction_history.append(deposit_message)
        return current_deposit
    
    def show_transaction_history(self):
        return self.transaction_history

class InsufficientFunds(Exception):
    pass

class OverdraftExceeded(Exception):
    pass

class CurrentAccount(Account):
    def __init__(self, account_number, initial_money, overdraft_limit):
        super(CurrentAccount, self).__init__(account_number, initial_money)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, withdrawal):
        if withdrawal <= self.current_balance:
            self.current_balance -= withdrawal
            withdrawal_message = "${} withdrawal.".format(withdrawal)
            self.transaction_history.append(withdrawal_message)
            return "Withdrawal from account successful!"
        elif withdrawal > self.current_balance and withdrawal < (self.current_balance + self.overdraft_limit):
            self.overdraft_limit = self.overdraft_limit - self.current_balance - (withdrawal - self.current_balance)
            self.current_balance = 0  
            withdrawal_overdraft_message = "${} withdrawal from overdraft.".format(withdrawal)
            self.transaction_history.append(withdrawal_overdraft_message)
            return "Withdrawal from overdraft successful."
        else:
            raise OverdraftExceeded("Overdraft Limit Exceeded")

    def show_balance(self):
        return "Current balance: ${0:.2f}. Overdraft balance: ${}.".format(self.current_balance, self.overdraft_limit)

class SavingsAccount(Account):
    def __init__(self, account_number, initial_money):
        super(SavingsAccount, self).__init__(account_number, initial_money)

    def add_interest(self, yearly_interest_rate, months):
        interest_earned = self.current_balance * ( yearly_interest_rate / 12 ) * months
        self.current_balance += interest_earned
        interest_message = "${0:.2f} interest earned.".format(interest_earned)
        self.transaction_history.append(interest_message)
        return "Interest earned."
    
    def transfer(self, transfer_amt, destination_acct):
        if transfer_amt <= self.current_balance:
            self.current_balance -= transfer_amt
            destination_acct.deposit(transfer_amt)
            transfer_message = "${} transfer.".format(transfer_amt)
            self.transaction_history.append(transfer_message)
            return "Transfer from account successful!"
        elif transfer_amt > self.current_balance:
            raise InsufficientFunds("Insufficient Funds in Accont")
        
    def show_balance(self):
        return "Current balance: ${0:.2f}.".format(self.current_balance)
        


        