import json
import socket

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from exception.handler import handler
from database.conn import db
from service.kiwoom import k_win

router = APIRouter()

host = "127.0.0.1"
port = 4000

# https://dev.to/gealber/simple-chat-application-using-websockets-with-fastapi-3gn7
# Client와 Socket 연결하기
@router.get("/hoga")
def get_hoga(symbol: str, db: Session = Depends(db.get_db)):
    if symbol is None:
        handler.code(404)

    # 소켓 통신 만들기
    msg = dict()
    msg['symbol'] = str(symbol)
    msg['method'] = "get_hoga"
    byte_msg = json.dumps(msg, indent=2).encode('utf-8')

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((host, port))
    client_socket.sendall(byte_msg)

    cnt = 0
    while True:
        if cnt > 10:
            break
        cnt += 1

        ask, bid = k_win.getTenTimeHoga(client_socket)
        print("받은 데이터 ask는 \"", ask, "\" 입니다.", sep="")
        print("받은 데이터 bid는 \"", bid, "\" 입니다.", sep="")

    client_socket.close()

    return "a"


@router.get("/last/{symbol}")
def get_last(symbol: str, db: Session = Depends(db.get_db)):

    if symbol is None:
        handler.code(404)
    return k_win.getLastPrice(symbol=symbol)

