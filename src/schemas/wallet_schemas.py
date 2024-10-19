from pydantic import BaseModel


class WalletSchemaBase(BaseModel):
    fullname: str
    document: str
    email: str
    type: int
    balance: float


class WalletSchemaCreate(WalletSchemaBase):
    password: str
