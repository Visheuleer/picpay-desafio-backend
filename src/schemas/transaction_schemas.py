from datetime import datetime
from pydantic import BaseModel


class TransactionSchemaCreate(BaseModel):
    payer_id: str
    payee_id: str
    value: float
    created_at: datetime