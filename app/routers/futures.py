import requests as requests
from fastapi import Depends,APIRouter
from app.utils.pylog import logger
from app.utils.pycode import formate_response,formate_pandas,formate_response_decorator
from app.utils.pytushare import tushare
from datetime import datetime , timedelta

router = APIRouter()

@logger.catch
@router.get("/base")
async def get_stock_list(exchange:str,fut_type=None):
    logger.info('call once')
    _base_data = tushare.fut_basic(exchange,fut_type)
    _list = formate_pandas(_base_data)
    return formate_response(200,_list,'ok')
    
@logger.catch
@router.get("/daily")
async def get_stock_list(rade_date=None,ts_code=None,exchange=None,start_date=None,end_date=None):
    logger.info('call once')
    _daily_data = tushare.fut_daily(rade_date,ts_code,exchange,start_date,end_date)
    _list = formate_pandas(_daily_data)
    return formate_response(200,_list,'ok')

@logger.catch
@router.get('/holding')
async def get_holding(trade_date=None, symbol=None,start_date=None,end_date=None, exchange=None):
    logger.info('call once')
    _holding_data = tushare.fut_holding(trade_date=trade_date,symbol=symbol,start_date=start_date,end_date=end_date,exchange=exchange)
    _list = formate_pandas(_holding_data)
    return formate_response(200,_list,'ok')

@logger.catch
@router.get('/wsr')
async def get_wsr(trade_date=None,symbol=None,start_date=None,end_date=None,exchange=None):
    logger.info('call once')
    _wsr_data = tushare.fut_wsr(trade_date=trade_date,symbol=symbol,start_date=start_date,end_date=end_date,exchange=exchange)
    _list = formate_pandas(_wsr_data)
    return formate_response(200,_list,'ok')

@logger.catch
@router.get('/settle')
async def get_settle(trade_date=None,ts_code=None,start_date=None,end_date=None,exchange=None):
    logger.info('call once')
    _settle_data = tushare.fut_settle(trade_date=trade_date,ts_code=ts_code,start_date=start_date,end_date=end_date,exchange=exchange)
    _list = formate_pandas(_settle_data)
    return formate_response(200,_list,'ok')

@logger.catch
@router.get('/index')
async def get_index_daily(ts_code=None,trade_date=None,start_date=None,end_date=None):
    logger.info('call once')
    _index_data = tushare.index_daily(ts_code=ts_code,trade_date=trade_date,start_date=start_date,end_date=end_date)
    _list = formate_pandas(_index_data)
    return formate_response(200,_list,'ok')

@logger.catch
@router.get('/mapping')
async def get_mapping(ts_code=None,trade_date=None,start_date=None,end_date=None):
    logger.info('call once')
    _index_data = tushare.fut_mapping(ts_code=ts_code,trade_date=trade_date,start_date=start_date,end_date=end_date)
    _list = formate_pandas(_index_data)
    return formate_response(200,_list,'ok')

@logger.catch
@router.get('/wdetail')
async def get_fut_weekly_detail(week=None,prd=None,start_week=None,end_week=None,exchange=None):
    logger.info('call once')
    _index_data = tushare.fut_weekly_detail(week=week,prd=prd,start_week=start_week,end_week=end_week,exchange=exchange)
    _list = formate_pandas(_index_data)
    return formate_response(200,_list,'ok')