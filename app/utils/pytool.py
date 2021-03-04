import os,sys
from app.utils.pydecorators import * 
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime

@singleton
class Tool():
    def __init__(self):
        pass
    
    def get_pwd(self,file_path):
        return os.path.abspath(file_path)
    
    def get_pwd_upper(self,file_path):
        return os.path.dirname(file_path)

    def get_rate(self):
        url = "http://www.safe.gov.cn/AppStructured/hlw/RMBQuery.do"
        html = urlopen(url)
        soup = BeautifulSoup(html.read(),"html.parser",from_encoding="utf-8")
        trs = soup.find_all('tr')
        titles = trs[9].find_all('th')
        _rate_list = []

        for i in range(10,20):
            tr = trs[i]
            tds = tr.find_all('td')
            # print(tds)
            for j in range(1,len(titles)):
                _dict = dict({
                    'GDATU' : ''.join(tds[0].get_text().strip().split('-')),
                    'L_CURRECNY' : '人民币',
                    'F_CURRENCY' : titles[j].get_text().strip(),
                    'UKURS' : tds[j].get_text().strip() 
                })
                _rate_list.append(_dict)

        return _rate_list

tool = Tool()