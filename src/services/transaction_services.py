def can_make_transaction(wallet_type):
    if wallet_type == 1:
        return True
    return False


def isBalanceEnough(wallet, value):
    if wallet.balance < value:
        return False
    return True