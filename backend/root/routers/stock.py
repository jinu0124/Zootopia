from datetime import datetime, timedelta

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.root.config.lstm_model import Config
from backend.root.database import stock_crud
from backend.root.exception.handler import handler
from backend.root.schema import stock
from backend.root.database.conn import db
from backend.root.schema.predict import Predict
from backend.root.service.stock_service import stock_service

router = APIRouter()


@router.get("/symbol", response_model=stock.Stock)
async def get_symbol(name: str, db: Session = Depends(db.get_db)):
    if name is None:
        handler.code(404)

    stock_profile = stock_crud.get_symbol(db, name=name)

    return stock_profile

@router.get("/predict")
async def stock_predict(symbol: str):
    if symbol is None: handler.code(404)
    print("a")
    predict_stock = stock_service.predict(symbol)

    conf = Config()
    pred = Predict()
    ret = dict()

    for i, e in enumerate(predict_stock):
        pred.price.append(int(e))
        pred.day.append(datetime.today().date() + timedelta(conf.FORECAST - len(predict_stock) + i + 1))

    ret['price'] = pred.price
    ret['day'] = pred.day
    return ret

