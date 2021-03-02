import requests as requests
from fastapi import Depends,APIRouter
from app.utils.pylog import logger
from app.utils.pycode import formate_response,formate_response_decorator

router = APIRouter()

@logger.catch
@router.get("/all")
# @formate_response_decorator
async def get_xinguan_data():
    logger.info('call once')
    _request = requests.get('https://interface.sina.cn/news/wap/fymap2020_data.d.json')
    _data = _request.json()['data']['worldlist']
    # print(_data)
    return formate_response(200,_data,'ok')


