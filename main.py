from api.Kiwoom import *
import sys

app = QApplication(sys.argv)
Kiwoom = Kiwoom()

order_result = Kiwoom.send_order('send_buy_order', 1001, 1, '005930',
                                 1, 80300, '00')



print(order_result)
app.exec_()

