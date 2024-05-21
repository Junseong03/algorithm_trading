from api.Kiwoom import *
from util.make_up_universe import *
from util.db_helper import *
import math

class RSIStrategy(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.strategy_name = "RSIStrategy"
        self.Kiwoom = Kiwoom()
        self.universe = {}
        self.init_strategy()

    def init_strategy(self):
        self.check_and_get_universe()

    def check_and_get_universe(self):
        if not check_table_exist(self.strategy_name, 'universe'):
            universe_list = get_universe()
            print(universe_list)
            universe = {}

            now = datetime.now().strftime("%Y%m%d")
            kospi_code_list = self.Kiwoom.get_code_list_by_market("0")
            kosdaq_code_list = self.Kiwoom.get_code_list_by_market("10")

            for code in kospi_code_list + kosdaq_code_list:
                code_name = self.Kiwoom.get_master_code_name(code)

                if code_name in universe_list:
                    universe[code] = code_name

                universe_df = pd.DataFrame({
                    'code': universe.keys(),
                    'code_name':universe.values(),
                    'created_at': [now] * len(universe.keys())
                })

                insert_df_to_db(self.strategy_name, 'universe', universe_df)
            sql = "select * from universe"
            cur = execute_sql(self.strategy_name, sql)
            universe_list = cur.fetchall()

            for item in universe_list:
                idx, code, code_name, created_at = item
                self.universe[code] = {
                    'code_name' : code_name
                }

            print(self.universe)

    def run(self):
        pass