from fastapi import Depends,APIRouter
from app.utils.pylog import logger
from app.utils.pycode import formate_response,formate_pandas,formate_response_decorator
from app.utils.pypandas import PyPandas
from app.utils.pytool import tool

from typing import List , Optional
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.db import models,crud,schemas
from app.db.database import SessionLocal, engine

router = APIRouter()

@logger.catch
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get("/one")
@logger.catch
def get_haiguan(db: Session = Depends(get_db)):
	r = crud.show_haiguan(db)
	# logger.info(r)
	return formate_response(r[0],r[1],r[2])

@router.get("/limit")
@logger.catch
def get_haiguans(db: Session = Depends(get_db), page:int = 1, pagesize:int = 50):
    skip = page*pagesize
    limit = pagesize
    r = crud.limit_haiguan(db,skip,limit)
    # logger.info(r)
    return formate_response(r[0],r[1],r[2])

@router.get("/all")
@logger.catch
def get_haiguans(db: Session = Depends(get_db)):
    r = crud.all_haiguan(db)
    # logger.info(r)
    return formate_response(r[0],r[1],r[2])




# def initPandas():
#     _file_path = tool.get_pwd(__file__)
#     _one = tool.get_pwd_upper(_file_path)
#     _two = tool.get_pwd_upper(_one)
#     _three = tool.get_pwd_upper(_two)
#     _excel_data = _three + '/static/data_2020.12_all.xlsx'
#     # print(_excel_data)
#     pypandas = PyPandas(_excel_data)
#     return pypandas

# @logger.catch
# @router.get("/all")
# async def get_haiguan_list():
#     logger.info('call once')
#     _pandas = initPandas()
#     _list = _pandas.read_excel()
#     # print(_file_path)
#     return formate_response(200,_list,'ok')