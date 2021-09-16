from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from exception.handler import handler
from database.conn import db
from service.kiwoom import k_win

router = APIRouter()

@router.get("/hoga")
def get_symbol(name: str, db: Session = Depends(db.get_db)):
    if name is None:
        handler.code(404)
    # k_win.

    # return stock_profile
    return "a"


@router.get("/last/{symbol}")
def get_last(symbol: int, db: Session = Depends(db.get_db)):
    if symbol is None:
        handler.code(404)
    return k_win.getLastPrice(code=symbol)
