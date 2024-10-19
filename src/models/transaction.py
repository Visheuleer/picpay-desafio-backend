from sqlalchemy import Column, String, DECIMAL, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.sql import func
import uuid
from models import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    payer_id = Column(CHAR(36), ForeignKey('wallets.id'), nullable=False, index=True)
    payee_id = Column(CHAR(36), ForeignKey('wallets.id'), nullable=False, index=True)
    value = Column(DECIMAL(10, 2), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)

