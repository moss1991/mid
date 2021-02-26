import requests as requests
from fastapi import Depends,APIRouter
from app.utils.pylog import logger
from app.utils.pycode import formate_response,formate_pandas,formate_response_decorator
from app.utils.pytushare import tushare
from datetime import datetime , timedelta

router = APIRouter()

@logger.catch
@router.get('/base')
async def get_fx_base():
    _list = []
    return formate_response(200,_list,'ok')