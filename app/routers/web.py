import requests as requests
from fastapi import Depends,APIRouter
from app.utils.pylog import logger
from app.utils.pycode import formate_response,formate_response_decorator
from app.utils.pytool import tool

router = APIRouter()

# @logger.catch
# @router.get("/all")
# async def get_xinguan_data():
#     logger.info('call once')
#     _request = requests.get('https://interface.sina.cn/news/wap/fymap2020_data.d.json')
#     _data = _request.json()['data']['worldlist']
#     # print(_data)
#     return formate_response(200,_data,'ok')

@logger.catch
@router.get("/rate")
async def get_stock_list():
    logger.info('call once')
    _rate_data = tool.get_rate()
    return formate_response(200,_rate_data,'ok')
