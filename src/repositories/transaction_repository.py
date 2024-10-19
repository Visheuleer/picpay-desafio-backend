from mysqldb import db_connection
from models import Transaction


def find_transaction_by_id(id):
    session = db_connection.db_session()
    transaction = session.query(Transaction).filter(
        Transaction.id == id
    ).first()
    session.close()
    return transaction


def save_transaction(transaction):
    session = db_connection.db_session()
    session.add(Transaction(**transaction))
    session.commit()
    session.close()