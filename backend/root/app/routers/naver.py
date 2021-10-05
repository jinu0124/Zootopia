from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()

from ..database.conn import db
from ..database import stock_posi_negative_crud as spn_crud
from ..schema import stock_posi_negative as spn_schema

from datetime import datetime, timedelta, timezone

@router.get("/postspn")
async def postspn(db: Session = Depends(db.get_db)):
    now = datetime.now()
    input_spn = spn_schema.Stock_posi_negative(code='123457', date=datetime(now.year, now.month, now.day, tzinfo=KST), score=0.55)
    return spn_crud.create_spn(db = db, spn=input_spn)
    

@router.get("/getspn")
async def getspn(db: Session = Depends(db.get_db)):
    now = datetime.now()
    return spn_crud.get_spn(db = db, code='123456', date=datetime(now.year, now.month, now.day, tzinfo=KST))

