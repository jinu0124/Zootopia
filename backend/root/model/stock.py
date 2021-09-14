from sqlalchemy import Column, Integer, String

from backend.root.database.conn import Base

class Stock(Base):
    __tablename__ = "stock"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String)
    market = Column(String)
    NAME = Column(String)
    sector = Column(String, index=True)
    region = Column(String)

