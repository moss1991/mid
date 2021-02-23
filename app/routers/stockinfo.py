import requests as requests
from fastapi import Depends,APIRouter
from app.utils.pylog import logger
from app.utils.pycode import formate_response,formate_pandas,formate_response_decorator
from app.utils.pytushare import tushare
from datetime import datetime , timedelta

router = APIRouter()

@logger.catch
@router.get("/list")
async def get_stock_list():
    logger.info('call once')
    _stock_data = tushare.stock_list()
    _list = formate_pandas(_stock_data)
    return formate_response(200,_list,'ok')


@logger.catch
@router.get("/tradecal")
async def get_trade_cal(from_date:str,to_date:str):
    logger.info('call once')
    _stock_data = tushare.trade_cal(from_date,to_date)
    _list = formate_pandas(_stock_data)
    return formate_response(200,_list,'ok')

@logger.catch
@router.get('/namechange')
async def get_name_change(ts_code:str):
    logger.info('call once')
    _name_change_data = tushare.name_change(ts_code)
    _list = formate_pandas(_name_change_data)
    return formate_response(200,_list,'ok')

@logger.catch
@router.get('/hs_const')
async def get_hs_sz_info(ts_type:str):
    logger.info('call once')
    _hs_or_zs_info = tushare.hs_const(ts_type)
    _list = formate_pandas(_hs_or_zs_info)
    return formate_response(200,_list,'ok')