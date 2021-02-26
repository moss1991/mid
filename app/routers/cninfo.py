from fastapi import Depends,APIRouter
from app.utils.pylog import logger
from app.utils.pycode import formate_response,formate_pandas,formate_response_decorator
from app.utils.pytushare import tushare
from datetime import datetime , timedelta

router = APIRouter()

@logger.catch
@router.get('/shibor')
async def get_shibor(date=None,start_date=None,end_date=None):
    logger.info('call once')
    _shibor_data = tushare.shibor(date=date,start_date=start_date, end_date=end_date)
    _list = formate_pandas(_shibor_data)
    return formate_response(200,_list,'ok')

@logger.catch
@router.get("/gdp")
async def get_cn_gdp(q=None,start_q=None,end_q=None):
    logger.info('call once')
    _gdp_data = tushare.cn_gdp(q=q,start_q=start_q,end_q=end_q)
    _list = formate_pandas(_gdp_data)
    return formate_response(200,_list,'ok')

@logger.catch
@router.get('/cpi')
async def get_cn_cpi(m=None,start_m=None,end_m=None):
    logger.info('call once')
    _cpi_data = tushare.cn_cpi(m=m,start_m=start_m,end_m=end_m)
    _list = formate_pandas(_cpi_data)
    return formate_response(200,_list,'ok')

@logger.catch
@router.get('/ppi')
async def get_cn_ppi(m=None,start_m=None,end_m=None):
    logger.info('call once')
    _ppi_data = tushare.cn_cpi(m=m,start_m=start_m,end_m=end_m)
    _list = formate_pandas(_ppi_data)
    return formate_response(200,_list,'ok')

@logger.catch
@router.get('/money')
async def get_m(m=None,start_m=None,end_m=None):
    logger.info('call once')
    _ppi_data = tushare.cn_cpi(m=m,start_m=start_m,end_m=end_m)
    _list = formate_pandas(_ppi_data)
    return formate_response(200,_list,'ok')