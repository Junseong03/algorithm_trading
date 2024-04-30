from api.Kiwoom import *
import sys

app = QApplication(sys.argv)
Kiwoom = Kiwoom()


position = Kiwoom.get_balance()
print(position)

app.exec_()

# 오류난 사람 지금 이야기하기..!