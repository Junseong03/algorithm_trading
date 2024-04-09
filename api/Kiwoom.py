from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time
class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        self._make_Kiwoom_instance()
        self._set_signal_slots()
        self._comm_connect()
        self.account_number = self.get_account_number()
        self.tr_event_loop = QEventLoop()

    def _make_Kiwoom_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def _set_signal_slots(self):
        self.OnEventConnect.connect(self._login_slot)
        self.OnReceiveTrData.connect(self._on_receive_tr_data)


    def _login_slot(self, err_code):
        if err_code == 0:
            print("connected")

        else:
            print("not connected")

        self.login_event_loop.exit()


    def _comm_connect(self):
        self.dynamicCall("CommConnect()")

        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()


    def get_account_number(self, tag="ACCNO"):
        account_list = self.dynamicCall("GetLoginInfo(QString)", tag)
        account_number = account_list.split(';')[0]
        print(account_number)

        return account_number

    # 여기 아래 하고 있는 중
    def get_code_list_by_market(self, market_type):
        code_list = self.dynamicCall("GetCodeListByMarket(QString)", market_type)
        code_list = code_list.split(';')[:-1]
        return code_list


    def get_master_code_name(self, code):
        code_name = self.dynamicCall("GetMasterCodeName(QString)", code)
        return code_name

    # 여기부터
    def _on_receive_tr_data(self,screen_no, rqname, trcode, record_name, next, unused1,
                            unused2, unused3, unused4):
        print("[Kiwoom] _on_receive_tr_data is called {} / {} / {}".format(screen_no, rqname, trcode))
        tr_data_cnt = self.dynamicCall("GetRepeatCnt(QString, QString)", trcode, rqname)

        if next == '2':
            self.has_next_tr_data = True
        else:
            self.has_next_tr_data = False

        if rqname == "opw00001_req":
            deposit = self.dynamicCall("GetCommData(QString, QString, int, QString)",
                                       trcode, rqname, 0, "주문가능금액")
            self.tr_data = int(deposit)
            print(self.tr_data)

        self.tr_event_loop.exit()
        time.sleep(0.5) #time 라이브러리를 안가져옴.  맨 위에 import time 구문 적어주기.






    # 여기부터. 현재 파일은 Kiwoom.py입니다.
    def get_deposit(self):
        self.dynamicCall("SetInputValue(QString, QString)", "계좌번호", self.account_number)
        self.dynamicCall("SetInputValue(QString, QString)", "비밀번호입력매체구분", "00")
        self.dynamicCall("SetInputValue(QString, QString)", "조회구분", "2")
        self.dynamicCall("CommRqData(QString, QString, int, QString)", "opw00001_req",
                         "opw00001", 0, "0002")

        self.tr_event_loop.exec_()
        return self.tr_data
