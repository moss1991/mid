from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.utils.pytool import tool

# 本地开发环境
db_name             = 'flm_haiguan'
db_user_name        = 'root'
db_user_password    = 'rc123456'
db_addr             = 'localhost'


SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://"+db_user_name+":"+db_user_password+"@"+db_addr+":3306/"+db_name

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine)

Base = declarative_base()