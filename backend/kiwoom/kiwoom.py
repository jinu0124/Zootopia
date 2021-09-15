import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
import datetime

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("주식호가잔량")
        self.setGeometry(300, 300, 300, 400)

        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")

        self.ocx.OnEventConnect.connect(self._handler_login)

        self.ocx.dynamicCall("CommConnect()")

    def _handler_login(self, err_code):
        if err_code == 0:
            self.ocx.OnReceiveRealData.connect(self._handler_real_data)
            self.ocx.dynamicCall("SetRealReg(QString, QString, QString, QString)",
                                 "1000", "005930", "41", 1)  # screen_no, code_list, fid_list, real_type

    def _handler_real_data(self, code, real_type, data):
        if real_type == "주식호가잔량":
            hoga_time = self.GetCommRealData(code, 21)
            ask01_price = self.GetCommRealData(code, 41)
            ask01_volume = self.GetCommRealData(code, 61)
            ask02_price = self.GetCommRealData(code, 42)    # 매수호가 1
            ask02_volume = self.GetCommRealData(code, 62)    # 호가 수량 1
            ask03_price = self.GetCommRealData(code, 43)
            ask03_volume = self.GetCommRealData(code, 63)
            ask04_price = self.GetCommRealData(code, 44)
            ask04_volume = self.GetCommRealData(code, 64)
            ask05_price = self.GetCommRealData(code, 45)
            ask05_volume = self.GetCommRealData(code, 65)
            ask06_price = self.GetCommRealData(code, 46)
            ask06_volume = self.GetCommRealData(code, 66)
            ask07_price = self.GetCommRealData(code, 47)
            ask07_volume = self.GetCommRealData(code, 67)
            ask08_price = self.GetCommRealData(code, 48)
            ask08_volume = self.GetCommRealData(code, 68)
            ask09_price = self.GetCommRealData(code, 49)
            ask09_volume = self.GetCommRealData(code, 69)
            ask10_price = self.GetCommRealData(code, 50)
            ask10_volume = self.GetCommRealData(code, 70)

            bid01_price = self.GetCommRealData(code, 51)
            bid01_volume = self.GetCommRealData(code, 71)
            bid02_price = self.GetCommRealData(code, 52)
            bid02_volume = self.GetCommRealData(code, 72)
            bid03_price = self.GetCommRealData(code, 53)
            bid03_volume = self.GetCommRealData(code, 73)
            bid04_price = self.GetCommRealData(code, 54)
            bid04_volume = self.GetCommRealData(code, 74)
            bid05_price = self.GetCommRealData(code, 55)
            bid05_volume = self.GetCommRealData(code, 75)
            bid06_price = self.GetCommRealData(code, 56)
            bid06_volume = self.GetCommRealData(code, 76)
            bid07_price = self.GetCommRealData(code, 57)
            bid07_volume = self.GetCommRealData(code, 77)
            bid08_price = self.GetCommRealData(code, 58)
            bid08_volume = self.GetCommRealData(code, 78)
            bid09_price = self.GetCommRealData(code, 59)
            bid09_volume = self.GetCommRealData(code, 79)
            bid10_price = self.GetCommRealData(code, 60)
            bid10_volume = self.GetCommRealData(code, 80)
            print(hoga_time)
            print(f"매도호가: {ask05_price} - {ask05_volume}")
            print(f"매도호가: {ask04_price} - {ask04_volume}")
            print(f"매도호가: {ask03_price} - {ask03_volume}")
            print(f"매도호가: {ask02_price} - {ask02_volume}")
            print(f"매도호가: {ask01_price} - {ask01_volume}")
            print(f"매수호가: {bid01_price} - {bid01_volume}")
            print(f"매수호가: {bid02_price} - {bid02_volume}")
            print(f"매수호가: {bid03_price} - {bid03_volume}")
            print(f"매수호가: {bid04_price} - {bid04_volume}")
            print(f"매수호가: {bid05_price} - {bid05_volume}")

    def GetCommRealData(self, code, fid):
        data = self.ocx.dynamicCall("GetCommRealData(QString, int)", code, fid)
        return data


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()