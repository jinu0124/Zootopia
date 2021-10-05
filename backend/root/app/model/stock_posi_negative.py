from sqlalchemy import Column, String, DateTime, Float

from ..database.conn import Base

class Stock_posi_negative(Base):
    __tablename__ = "stock_posi_negative"

    code = Column(String(6), primary_key=True, index=True)
    date = Column(DateTime, primary_key=True, index=True)
    score = Column(Float)
    

