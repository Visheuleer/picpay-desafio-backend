from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.dialects.mysql import CHAR
import uuid
from models import Base

class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    fullname = Column(String(80), nullable=False, index=True)
    document = Column(String(13), nullable=False, index=True)
    email = Column(String(30), nullable= False, unique=True, index=True)
    password = Column(String(250), nullable=False)
    type = Column(Integer, nullable=False)
    balance = Column(DECIMAL(10, 2), nullable=False)

