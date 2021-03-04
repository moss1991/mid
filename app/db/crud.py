
import sys
import logging

from sqlalchemy.orm import Session
from app.db import models, schemas
from app.db.database import SessionLocal, engine
from typing import List , Optional
from app.utils.pylog import logger
from app.utils.pycode import formate_response,formate_pandas,formate_response_decorator
from app.utils.pytool import tool

def show_haiguan(db: Session):
    code = 200
    msg  = ""
    mdata = None

    try:
        one = db.query(models.HaiguanItem).filter().first()	
        mdata = one.to_dict()
    except Exception as e:
        code = 500
        msg = "Exception in show_haiguan"
        mdata = e
    return code,mdata,msg

def limit_haiguan(db: Session, skip:int =0 ,limit:int = 100):
    code = 200
    msg  = ""
    mdata = []

    try:
        many =  db.query(models.HaiguanItem).offset(skip).limit(limit).all()
        for one in many:
            mdata.append(
                one.to_dict()
            )
    except Exception as e:
        code = 500
        msg = "Exception in limit_haiguan"
        mdata = e
    return code,mdata,msg
    