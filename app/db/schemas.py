from datetime import date,datetime
from sqlalchemy.sql.sqltypes import String
# from sqlalchemy import create_engine, Column, Integer, String, DateTime,Boolean
from pydantic import BaseModel
from typing import List , Optional

class HaiguanItem(BaseModel):

    id:int
    product_id:String
    product_name:String
    trade_country_id:int
    trade_country_name:String
    trade_id:int
    trade_name:String
    register_id:int
    register_name:String
    first_unit:String
    first_price:int
    second_unit:String
    second_price:int 
    price:int
    year:int
    start_month:int
    end_month:int
    import_type:int
    code_type:int
    month_type:int
    create_time:datetime


    class Config:
        orm_mode = True
        arbitrary_types_allowed = True # 遗留问题