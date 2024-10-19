from fastapi import APIRouter, HTTPException, status
from schemas import TransactionSchemaCreate
from services import wallet_services, transaction_services
from repositories import transaction_repository, wallet_repository
import requests


router = APIRouter(prefix='/transaction')


@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_transaction(id):
    transaction = transaction_repository.find_transaction_by_id(id)
    if not transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Transação {id} não encontrada.')
    return transaction

@router.post('/payment', status_code=status.HTTP_202_ACCEPTED)
def payment(transaction: TransactionSchemaCreate):
    wallet_payer = wallet_repository.find_wallet_by_id(transaction.payer_id)
    wallet_payee = wallet_repository.find_wallet_by_id(transaction.payee_id)
    if not transaction_services.can_make_transaction(wallet_payer.type):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Carteiras do tipo Lojista não podem realizar transações, apenas receber.')

    if not transaction_services.isBalanceEnough(wallet_payer, transaction.value):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Saldo insuficiente.')

    if not requests.get('https://util.devi.tools/api/v2/authorize').ok:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Pagamento não autorizado.')
    new_wallet_payer = wallet_services.wallet_debit(wallet_payer, transaction.value)
    new_wallet_payee = wallet_services.wallet_credit(wallet_payee, transaction.value)
    wallet_repository.update_wallet(new_wallet_payer)
    wallet_repository.update_wallet(new_wallet_payee)
    transaction_repository.save_transaction(transaction.dict())
    return transaction