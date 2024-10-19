from fastapi import APIRouter, HTTPException, status
from schemas import WalletSchemaCreate
from services import wallet_services
from repositories import wallet_repository


router = APIRouter(prefix='/wallet')


@router.get('/{document}', status_code=status.HTTP_200_OK)
def get_wallet(document: str):
    wallet = wallet_repository.find_wallet_by_document(document)
    if not wallet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'CPF {document} não encontrado.')
    return wallet


@router.post('/register', status_code=status.HTTP_201_CREATED)
def register_wallet(wallet: WalletSchemaCreate):
    if wallet_repository.find_wallet_by_document(wallet.document):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'CPF {wallet.document} já está cadastrado.')
    hashed_password = wallet_services.hash_password(wallet.password)
    wallet.password = hashed_password
    wallet_repository.save_wallet(wallet.dict())
    return wallet