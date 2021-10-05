from typing import List, Optional

from pydantic import BaseModel

from datetime import datetime

from ..schema.trade import Trade


class Stock_posi_negative(BaseModel):

    code : str
    date : datetime
    score : float 

    class Config:
        orm_mode = True