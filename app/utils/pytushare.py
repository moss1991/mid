import tushare as ts
from datetime import datetime
# from app.config import config


def singleton(cls):
    # 单下划线的作用是这个变量只能在当前模块里访问,仅仅是一种提示作用
    # 创建一个字典用来保存类的实例对象
    _instance = {}

    def _singleton(*args, **kwargs):
        # 先判断这个类有没有对象
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)  # 创建一个对象,并保存到字典当中
        # 将实例对象返回
        return _instance[cls]

    return _singleton

# def tushare_maker():
#     token = config['tushare']['token']
#     print(token)
#     ts.set_token(token)
#     pro = ts.pro_api()
#     return pro

@singleton
class Tushare(object):
    def __init__(self, token=''):
        self.token = token
        self.pro = ts.pro_api(self.token)
        # print('这是A的类的初始化方法')

    def get_pro(self):
        return self.pro
    
    def stock_list(self):
        """
        description
        查询当前所有正常上市交易的股票列表

        input
        名称	类型	必选	描述
        ts_code	str	N	股票代码
        list_status	str	N	上市状态： L上市 D退市 P暂停上市，默认L
        exchange	str	N	交易所 SSE上交所 SZSE深交所 HKEX港交所(未上线)
        is_hs	str	N	是否沪深港通标的，N否 H沪股通 S深股通

        output
        名称	类型	描述
        ts_code	str	TS代码
        symbol	str	股票代码
        name	str	股票名称
        area	str	所在地域
        industry	str	所属行业
        fullname	str	股票全称
        enname	str	英文全称
        market	str	市场类型 （主板/中小板/创业板/科创板/CDR）
        exchange	str	交易所代码
        curr_type	str	交易货币
        list_status	str	上市状态： L上市 D退市 P暂停上市
        list_date	str	上市日期
        delist_date	str	退市日期
        is_hs	str	是否沪深港通标的，N否 H沪股通 S深股通
        """
        info = self.pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')
        print(type(info))
        return info

    def trade_cal(self,start_data='20180901',end_date='20181001'):
        
        """
        获取各大交易所交易日历数据,默认提取的是上交所

        input
        名称	类型	必选	描述
        exchange	str	N	交易所 SSE上交所,SZSE深交所,CFFEX 中金所,SHFE 上期所,CZCE 郑商所,DCE 大商所,INE 上能源
        start_date	str	N	开始日期 （格式：YYYYMMDD 下同）
        end_date	str	N	结束日期
        is_open	str	N	是否交易 '0'休市 '1'交易

        output
        exchange	str	Y	交易所 SSE上交所 SZSE深交所
        cal_date	str	Y	日历日期
        is_open	str	Y	是否交易 0休市 1交易
        pretrade_date	str	N	上一个交易日
        """
        info = self.pro.trade_cal(exchange='', start_date=start_data, end_date=end_date, fields='exchange,cal_date,is_open,pretrade_date', is_open='0')
        return info

    # 股票曾用名
    def name_change(self,ts_code='600848.SH'):
        '''
        description
        历史名称变更记录

        input
        名称	类型	必选	描述
        ts_code	str	N	TS代码
        start_date	str	N	公告开始日期
        end_date	str	N	公告结束日期

        output
        名称	类型	默认输出	描述
        ts_code	str	Y	TS代码
        name	str	Y	证券名称
        start_date	str	Y	开始日期
        end_date	str	Y	结束日期
        ann_date	str	Y	公告日期
        change_reason	str	Y	变更原因
        '''
        info = self.pro.namechange(ts_code=ts_code, fields='ts_code,name,start_date,end_date,change_reason')
        return info
    
    # 沪深股通成份股
    def hs_const(self,hs_type='SH'):
        """
        获取沪股通、深股通成分数据

        名称	类型	必选	描述
        hs_type	str	Y	类型SH沪股通SZ深股通
        is_new	str	N	是否最新 1 是 0 否 (默认1)

        名称	类型	默认显示	描述
        ts_code	str	Y	TS代码
        hs_type	str	Y	沪深港通类型SH沪SZ深
        in_date	str	Y	纳入日期
        out_date	str	Y	剔除日期
        is_new	str	Y	是否最新 1是 0否
        """
        info = self.pro.hs_const(hs_type=hs_type) 
        return info
    
    # 上市公司基本信息
    def stock_company(self,exchange='SZSE'):
        """
        获取上市公司基础信息，单次提取4500条，可以根据交易所分批提取

        名称	类型	必须	描述
        ts_code	str	N	股票代码
        exchange	str	N	交易所代码 ，SSE上交所 SZSE深交所

        名称	类型	默认显示	描述
        ts_code	str	Y	股票代码
        exchange	str	Y	交易所代码 ，SSE上交所 SZSE深交所
        chairman	str	Y	法人代表
        manager	str	Y	总经理
        secretary	str	Y	董秘
        reg_capital	float	Y	注册资本
        setup_date	str	Y	注册日期
        province	str	Y	所在省份
        city	str	Y	所在城市
        introduction	str	N	公司介绍
        website	str	Y	公司主页
        email	str	Y	电子邮件
        office	str	N	办公室
        employees	int	Y	员工人数
        main_business	str	N	主要业务及产品
        business_scope	str	N	经营范围
        """
        info = self.pro.stock_company(exchange=exchange, fields='ts_code,chairman,manager,secretary,reg_capital,setup_date,province')
        return info
    
    # 上市公司管理层 2000积分限制 undone
    def stk_managers(self,ts_code='000001.SZ'):
        """
        获取上市公司管理层

        名称	类型	必选	描述
        ts_code	str	N	股票代码，支持单个或多个股票输入
        ann_date	str	N	公告日期（YYYYMMDD格式，下同）
        start_date	str	N	公告开始日期
        end_date	str	N	公告结束日期

        名称	类型	默认显示	描述
        ts_code	str	Y	TS股票代码
        ann_date	str	Y	公告日期
        name	str	Y	姓名
        gender	str	Y	性别
        lev	str	Y	岗位类别
        title	str	Y	岗位
        edu	str	Y	学历
        national	str	Y	国籍
        birthday	str	Y	出生年月
        begin_date	str	Y	上任日期
        end_date	str	Y	离任日期
        resume	str	N	个人简历
        """
        info = self.pro.stk_managers(ts_code=ts_code)
        return info
    
    # 管理层薪酬和持股 2000分限制 undone
    def stk_rewards(self):
        """
        名称	类型	必选	描述
        ts_code	str	Y	TS股票代码，支持单个或多个代码输入
        end_date	str	N	报告期

        名称	类型	默认显示	描述
        ts_code	str	Y	TS股票代码
        ann_date	str	Y	公告日期
        end_date	str	Y	截止日期
        name	str	Y	姓名
        title	str	Y	职务
        reward	float	Y	报酬
        hold_vol	float	Y	持股数
        """
        info = self.pro.stk_rewards(ts_code='000001.SZ')
        return info
    
    def new_share(self,start_date='20180901', end_date='20181018'):
        # 获取新股上市列表数据
        """
        获取新股上市列表数据

        名称	类型	必选	描述
        start_date	str	N	上网发行开始日期
        end_date	str	N	上网发行结束日期

        名称	类型	默认显示	描述
        ts_code	str	Y	TS股票代码
        sub_code	str	Y	申购代码
        name	str	Y	名称
        ipo_date	str	Y	上网发行日期
        issue_date	str	Y	上市日期
        amount	float	Y	发行总量（万股）
        market_amount	float	Y	上网发行总量（万股）
        price	float	Y	发行价格
        pe	float	Y	市盈率
        limit_amount	float	Y	个人申购上限（万股）
        funds	float	Y	募集资金（亿元）
        ballot	float	Y	中签率
        """
        info = self.pro.new_share(start_date=start_date, end_date=end_date)
        return info
    
    def daily(self,ts_code='600519.SZ',start_date='20210118', end_date='20210218'):
        """
        获取股票行情数据，或通过通用行情接口获取数据，包含了前后复权数据

        名称	类型	必选	描述
        ts_code	str	N	股票代码（支持多个股票同时提取，逗号分隔）
        trade_date	str	N	交易日期（YYYYMMDD）
        start_date	str	N	开始日期(YYYYMMDD)
        end_date	str	N	结束日期(YYYYMMDD)

        名称	类型	描述
        ts_code	str	股票代码
        trade_date	str	交易日期
        open	float	开盘价
        high	float	最高价
        low	float	最低价
        close	float	收盘价
        pre_close	float	昨收价
        change	float	涨跌额
        pct_chg	float	涨跌幅 （未复权，如果是复权请用 通用行情接口 ）
        vol	float	成交量 （手）
        amount	float	成交额 （千元）
        """
        info = self.pro.daily(ts_code, start_date=start_date, end_date=end_date)
        return info

tushare = Tushare('4c694540458ed9aeb5d832523255cb51f8c478ce5ccd06ba6e69b587')
# tushare1 = Tushare('4c694540458ed9aeb5d832523255cb51f8c478ce5ccd06ba6e69b587')
# tushare2 = Tushare('4c694540458ed9aeb5d832523255cb51f8c478ce5ccd06ba6e69b587')
# print(id(tushare1))
# print(id(tushare2))
# print(tushare.stock_list())
# print(tushare.trade_cal())
# print(tushare.name_change())
# print(tushare.hs_const())
# print(tushare.stock_company())
# print(tushare.new_share())
# print(tushare.daily())