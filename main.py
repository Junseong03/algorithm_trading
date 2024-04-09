from api.Kiwoom import *
import sys

app = QApplication(sys.argv)
Kiwoom = Kiwoom()

deposit = Kiwoom.get_deposit()




app.exec_()

