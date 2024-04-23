from api.Kiwoom import *
import sys

app = QApplication(sys.argv)
Kiwoom = Kiwoom()

order_result = Kiwoom.send_order('send_buy_order', 1001, 1, '005930',
                                 1, 75700, '00')
                                                        # ↑ '영웅문' 차트 보면서 가격 수정하기


print(order_result)
app.exec_()

