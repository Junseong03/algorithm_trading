from api.Kiwoom import *
import sys

app = QApplication(sys.argv)
Kiwoom = Kiwoom()
# 아래 한 줄.
Kiwoom.set_real_reg("1000", "005930", get_fid("장운영구분"), "0")

app.exec_()
