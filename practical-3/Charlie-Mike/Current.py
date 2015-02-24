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