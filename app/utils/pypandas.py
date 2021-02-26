import pandas as pd
from app.utils.pydecorators import * 

@singleton
class PyPandas(object):
    def __init__(self, excel_path=''):
        self.excel_path = excel_path
    
    def read_excel(self,sheet_index=0, header=0):
        _file_path = self.excel_path
        _data = pd.read_excel(io=_file_path)
        _list = list()
        for ele in _data.values: 
            _dict = dict(
                product_name=ele[1],
                first_price=ele[8],
            )
            _list.append(_dict)
        return _list 

