from api.Kiwoom import *
from util.make_up_universe import *
from util.db_helper import *
import math

class RSIStrategy(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.strategy_name = "RSIStrategy"
        self.Kiwoom = Kiwoom()
        self.init_strategy()

    def init_strategy(self):
        self.check_and_get_universe()

    def check_and_get_universe(self):
        if not check_table_exist(self.strategy_name, 'universe'):
            universe_list = get_universe()
            print(universe_list)

    def run(self):
        pass