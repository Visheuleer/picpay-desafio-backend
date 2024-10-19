import decimal

import bcrypt
from models import Wallet

def hash_password(plain_password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(plain_password.encode('utf-8'), salt).decode('utf-8')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


def wallet_debit(wallet: Wallet, value: float) -> Wallet:
    wallet.balance = float(wallet.balance)
    wallet.balance -= value
    return wallet


def wallet_credit(wallet: Wallet, value: float) -> Wallet:
    wallet.balance = float(wallet.balance)
    wallet.balance += value
    return wallet