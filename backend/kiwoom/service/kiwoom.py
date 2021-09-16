import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *

from service.kiwoom_init import InitWindow

class MyWindow(InitWindow):
    def __init__(self):
        super().__init__()
        self.ocx = InitWindow.ocx
        self.ocx.OnEventConnect.connect(self._handler_login)
        self.ocx.dynamicCall("CommConnect()")

    # def getLastPrice(self, code=None):
    #     return self.ocx.dynamicCall("GetMasterLastPrice(QString)", [code])
        # print(self.ocx.GetMasterLastPrice("삼성전자"))

    def getLastPrice(self, code):
        return self.ocx.dynamicCall("GetMasterLastPrice(QString)", [int(code)])


    def getTenTimeHoga(self, symbol):
        self.ocx.dynamicCall("SetRealReg(QString, QString, QString, QString)",
                             "1000", str(symbol), "41", 1)  # screen_no, code_list, fid_list, real_type

    def removeTenTimeHoga(self, symbol):
        self.ocx.dynamicCall("SetRealRemove(QString, QString, QString, QString)",
                             "1000", str(symbol))

    def _handler_login(self, err_code):
        if err_code == 0:
            self.ocx.OnReceiveRealData.connect(self._handler_real_data)
            self.ocx.OnReceiveTrData.connect(self._handler_tr_data)
            self.ocx.OnReceiveMsg.connect(self._handler_msg_data)
            self.ocx.OnReceiveChejanData.connect(self._handler_chejan_data)
            self.ocx.OnReceiveTrCondition.connect(self._handler_trc_data)

    def _handler_tr_data(self, code, real_type, data):
        print("_handler_tr_data", code)

    def OnReceiveMsg(self, code, real_type, data):
        print("OnReceiveMsg", code)

    def OnReceiveChejanData(self, code, real_type, data):
        print("OnReceiveChejanData", code)

    def OnReceiveTrCondition(self, code, real_type, data):
        print("OnReceiveTrCondition", code)


    def _handler_real_data(self, code, real_type, data):
        if real_type == "전일가":
            print(data)


        if real_type == "주식호가잔량":
            time = self.GetCommRealData(code, 21)
            ask, bid = dict(), dict()
            for i in range(1, 11):
                ask['price' + str(i)].append(self.GetCommRealData(code, 40 + i))
                ask['volume' + str(i)].append(self.GetCommRealData(code, 60 + i))

                bid['price' + str(i)].append(self.GetCommRealData(code, 50 + i))
                bid['volume' + str(i)].append(self.GetCommRealData(code, 70 + i))

            print(ask, bid)

            print(time)

            return time, ask, bid

    def GetCommRealData(self, code, fid):
        data = self.ocx.dynamicCall("GetCommRealData(QString, int)", code, fid)
        return data

    def quit_app(self):
        appWin.exec_()

appWin = QApplication(sys.argv)
k_win = MyWindow()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     app.exec_()