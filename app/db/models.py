import os
import sys
import json
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime,Boolean
from sqlalchemy.types import Date 
from app.db.database import Base
from sqlalchemy.dialects.mysql import FLOAT

class HaiguanItem(Base):
    __tablename__ = "result_2020"
    # __tablename__ = "result_2020_copy"

    id = Column(Integer , primary_key=True, autoincrement=True)
    product_id = Column(String(255),nullable=False)
    product_name = Column(String(255),nullable=False,default="")
    trade_country_id = Column(Integer,nullable=False,default=0)
    trade_country_name = Column(String(255),nullable=False,default="")
    trade_id = Column(Integer,nullable=False,default=0)
    trade_name = Column(String(255),nullable=False,default="")
    register_id = Column(Integer,nullable=False,default=0)
    register_name = Column(String(255),nullable=False,default="")
    first_unit = Column(String(255),nullable=False,default="")
    first_price = Column(Integer,nullable=False,default=0)
    second_unit = Column(String(255),nullable=False,default="")
    second_price = Column(Integer,nullable=False,default=0)
    price = Column(Integer,nullable=False,default=0)
    year = Column(Integer,nullable=False,default=2020)
    start_month = Column(Integer,nullable=False,default=1)
    end_month = Column(Integer,nullable=False,default=1)
    import_type = Column(Integer,nullable=False,default=0)
    code_type = Column(Integer,nullable=False,default=0)
    month_type  = Column(Integer,nullable=False,default=0)
    create_time = Column(DateTime,onupdate=datetime.now(), default=datetime.now())

 
    def to_dict(self):
        diction = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        for key,value in diction.items():
            if(isinstance(value,datetime)):
                diction[key] = value.strftime("%Y-%m-%d %H:%M:%S")
        
        return diction

    def to_json(self):
        diction = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        for key,value in diction.items():
            if(isinstance(value,datetime)):
                diction[key] = value.strftime("%Y-%m-%d %H:%M:%S")
        
        return json.dumps(diction)

