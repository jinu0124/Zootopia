import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *

import socket
import json
import ast

host = "127.0.0.1"
port = 4000

class MyWindow():
    def __init__(self):
        super().__init__()

    def getTenTimeHoga(self, client_socket):
        ask = client_socket.recv(128)
        ask_decode = ast.literal_eval(ask.decode('utf-8'))
        bid = client_socket.recv(128)
        bid_decode = ast.literal_eval(bid.decode('utf-8'))

        return ask_decode, bid_decode


    def getLastPrice(self, symbol):
        pass

k_win = MyWindow()
