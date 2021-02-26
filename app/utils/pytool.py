import os,sys
from app.utils.pydecorators import * 

@singleton
class Tool():
    def __init__(self):
        pass
    
    def get_pwd(self,file_path):
        return os.path.abspath(file_path)
    
    def get_pwd_upper(self,file_path):
        return os.path.dirname(file_path)

tool = Tool()