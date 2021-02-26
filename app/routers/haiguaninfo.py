from fastapi import Depends,APIRouter
from app.utils.pylog import logger
from app.utils.pycode import formate_response,formate_pandas,formate_response_decorator
from app.utils.pypandas import PyPandas
from app.utils.pytool import tool

router = APIRouter()

def initPandas():
    _file_path = tool.get_pwd(__file__)
    _one = tool.get_pwd_upper(_file_path)
    _two = tool.get_pwd_upper(_one)
    _three = tool.get_pwd_upper(_two)
    _excel_data = _three + '/static/data_2020.12_all.xlsx'
    # print(_excel_data)
    pypandas = PyPandas(_excel_data)
    return pypandas

@logger.catch
@router.get("/all")
async def get_haiguan_list():
    logger.info('call once')
    _pandas = initPandas()
    _list = _pandas.read_excel()
    # print(_file_path)
    return formate_response(200,_list,'ok')