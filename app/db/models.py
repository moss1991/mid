import os
import sys
import json
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime,Boolean
from sqlalchemy.types import Date
from app.db.database import Base
from sqlalchemy.dialects.mysql import FLOAT

class Basis(Base):
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
