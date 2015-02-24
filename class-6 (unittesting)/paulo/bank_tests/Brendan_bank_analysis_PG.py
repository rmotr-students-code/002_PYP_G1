# # Bank system
# Create a class hierarchy for a bank system. SavingsAccount and CurrentAccount class must
# inherit from Account abstract class. Both classes must implement needed attributes and methods
# as required by the following usage sample:


class TransactionError(Exception):
    pass


class Account(object):

    def __init__(self, number, initial_money):
        self.number = number
        self.balance = int(initial_money)
        self.initial_money = initial_money
        self.action_list = ['Opened account number {number}'.format(number=self.number)]

    def deposit(self, amount):
        self.balance += amount
        self.action_list.append('Deposited ${amount}'.format(amount=amount))

    def show_balance(self):
        self.action_list.append('Shown balance')
        return self.balance

    def show_transaction_history(self):
        self.action_list.append('Asked for transaction history')
        return '\n'.join(self.action_list)

    def withdraw(self, amount):
        raise NotImplementedError('Withdraw method should be defined in child class')

    def __str__(self):
        return 'Created acct {0} with initial deposit of ${1}'.format(self.number, self.initial_money)

class SavingsAccount(Account):

    def __init__(self, number, initial_money):
        super(SavingsAccount, self).__init__(number, initial_money)
        self.interest_made = 0

    def add_interest(self, yearly_interest_rate, months):
        self.interest_made = self.balance * yearly_interest_rate / 12 * months
        self.balance += self.interest_made
        self.action_list.append('Added {interest} in concept of interest'.format(interest=self.interest_made))

    def transfer(self, amount, destination_account):
        self.withdraw(amount)
        destination_account.deposit(amount)
        self.action_list.append('Transferred ${amount} '
                                'from SavingsAccount {s_number} to CurrentAccount {c_number}'
                                .format(amount=amount, s_number=self.number, c_number=destination_account.number))

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise TransactionError('You don\'t have enough money in your account!')


class CurrentAccount(Account):
    def __init__(self, number, initial_money, overdraft_limit):
        super(CurrentAccount, self).__init__(number, initial_money)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance - amount > - self.overdraft_limit:
            self.balance -= amount
            self.action_list.append('Withdrew {amount}'.format(amount=amount))
        else:
            raise TransactionError('Overdraft limit exceeded')

# # ## This works!
# sa = SavingsAccount(number="123", initial_money=100)
# sa.deposit(1000)
# sa.add_interest(yearly_interest_rate=0.1, months=12)
# print(sa.show_balance())
# #print(sa.show_transaction_history())
# sa.withdraw(100)
# print(sa.show_balance())
# #print(sa.show_transaction_history())

