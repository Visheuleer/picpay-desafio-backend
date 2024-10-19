from mysqldb import db_connection
from models import Wallet


def find_wallet_by_id(id):
    session = db_connection.db_session()
    wallet = session.query(Wallet).filter(
        Wallet.id == id
    ).first()
    session.close()
    return wallet


def find_wallet_by_document(document):
    session = db_connection.db_session()
    wallet = session.query(Wallet).filter(
        Wallet.document == document
    ).first()
    session.close()
    return wallet


def save_wallet(wallet):
    session = db_connection.db_session()
    session.add(Wallet(**wallet))
    session.commit()
    session.close()

def update_wallet(wallet):
    session = db_connection.db_session()
    session.query(Wallet).filter(
        Wallet.id == wallet.id
    ).update(
        {
            Wallet.balance: wallet.balance
        }
    )
    session.commit()
    session.close()