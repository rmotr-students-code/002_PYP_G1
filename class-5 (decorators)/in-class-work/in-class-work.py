# library

class NotEnoughMoneyException(Exception):
    pass

class TyringToWithdrawFromInactiveAccExcpetion(Exception):
    pass


def withdraw_money(acc, amount):
    if amount > acc.balance:
        raise NotEnoughMoneyException("Your balance is not enough")
    if acc.active is False:
        raise TyringToWithdrawFromInactiveAccExcpetion()


# user

withdraw_money(get_from_db(id=123), amount)

