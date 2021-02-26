from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.utils.pytool import tool

ip = tool.get_host_ip()

if ip not in ['10.6.128.81','10.6.128.82','10.6.128.83']:
    # 本地开发环境
    db_name             = 'fastapi_development'
    db_user_name        = 'root'
    db_user_password    = 'rc123456'
    db_addr             = 'localhost'
else:
    db_name             = mysql_setting['db_name']
    db_user_name        = mysql_setting['db_user_name']
    db_user_password    = mysql_setting['db_user_password']
    db_addr             = mysql_setting['db_addr']

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://"+db_user_name+":"+db_user_password+"@"+db_addr+":3306/"+db_name

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine)

Base = declarative_base()