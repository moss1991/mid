import tushare as ts
from datetime import datetime
# from app.config import config
# from app.utils.pydecorators import * 


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

    # 获取新股上市列表数据   
    def new_share(self,start_date='20180901', end_date='20181018'):
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
    
    # 期货合约信息表
    def fut_basic(self,exchange='DCE', fut_type='1'):
        '''
        获取期货合约列表数据
        名称	类型	必选	描述
        exchange	str	Y	交易所代码 CFFEX-中金所 DCE-大商所 CZCE-郑商所 SHFE-上期所 INE-上海国际能源交易中心
        fut_type	str	N	合约类型 (1 普通合约 2主力与连续合约 默认取全部)

        名称	类型	默认显示	描述
        ts_code	str	Y	合约代码
        symbol	str	Y	交易标识
        exchange	str	Y	交易市场
        name	str	Y	中文简称
        fut_code	str	Y	合约产品代码
        multiplier	float	Y	合约乘数
        trade_unit	str	Y	交易计量单位
        per_unit	float	Y	交易单位(每手)
        quote_unit	str	Y	报价单位
        quote_unit_desc	str	Y	最小报价单位说明
        d_mode_desc	str	Y	交割方式说明
        list_date	str	Y	上市日期
        delist_date	str	Y	最后交易日期
        d_month	str	Y	交割月份
        last_ddate	str	Y	最后交割日
        trade_time_desc	str	N	交易时间说明
        '''
        info = self.pro.fut_basic(exchange=exchange, fut_type=fut_type, fields='ts_code,symbol,exchange,name,fut_code,multiplier,trade_unit,per_unit,quote_unit,list_date,d_mode_desc,delist_date,d_month,last_ddate,trade_time_desc')
        return info
    
    # 期货日线行情
    def fut_daily(self,trade_date=None,ts_code=None,exchange=None,start_date=None,end_date=None):
        """
        名称	类型	必选	描述
        trade_date	str	N	交易日期
        ts_code	str	N	合约代码
        exchange	str	N	交易所代码
        start_date	str	N	开始日期
        end_date	str	N	结束日期

        名称	类型	默认显示	描述
        ts_code	str	Y	TS合约代码
        trade_date	str	Y	交易日期
        pre_close	float	Y	昨收盘价
        pre_settle	float	Y	昨结算价
        open	float	Y	开盘价
        high	float	Y	最高价
        low	float	Y	最低价
        close	float	Y	收盘价
        settle	float	Y	结算价
        change1	float	Y	涨跌1 收盘价-昨结算价
        change2	float	Y	涨跌2 结算价-昨结算价
        vol	float	Y	成交量(手)
        amount	float	Y	成交金额(万元)
        oi	float	Y	持仓量(手)
        oi_chg	float	Y	持仓量变化
        delv_settle	float	N	交割结算价
        """
        info = self.pro.fut_daily(trade_date=trade_date, ts_code=ts_code, exchange=exchange, start_date=start_date, end_date=end_date, fields='ts_code,trade_date,pre_close,pre_settle,open,high,low,close,settle,change1,change2,vol,amount,oi,oi_chg,delv_settle')
        return info
    
    # 每日成交持仓排名
    def fut_holding(self,trade_date=None,symbol=None,start_date=None,end_date=None,exchange=None):
        """
        名称	类型	必选	描述
        trade_date	str	N	交易日期 （trade_date/symbol至少输入一个参数）
        symbol	str	N	合约或产品代码
        start_date	str	N	开始日期
        end_date	str	N	结束日期
        exchange	str	N	交易所代码

        trade_date	str	Y	交易日期
        symbol	str	Y	合约代码或类型
        broker	str	Y	期货公司会员简称
        vol	int	Y	成交量
        vol_chg	int	Y	成交量变化
        long_hld	int	Y	持买仓量
        long_chg	int	Y	持买仓量变化
        short_hld	int	Y	持卖仓量
        short_chg	int	Y	持卖仓量变化
        exchange	str	N	交易所
        """
        info = self.pro.fut_holding(trade_date=trade_date, symbol=symbol,start_date=start_date,end_date=end_date, exchange=exchange)
        return info
    
    # 仓单日报
    def fut_wsr(self,trade_date=None,symbol=None,start_date=None,end_date=None,exchange=None):
        """
        名称	类型	必选	描述
        trade_date	str	N	交易日期
        symbol	str	N	产品代码
        start_date	str	N	开始日期
        end_date	str	N	结束日期
        exchange	str	N	交易所代码

        名称	类型	默认显示	描述
        trade_date	str	Y	交易日期
        symbol	str	Y	产品代码
        fut_name	str	Y	产品名称
        warehouse	str	Y	仓库名称
        wh_id	str	N	仓库编号
        pre_vol	int	Y	昨日仓单量
        vol	int	Y	今日仓单量
        vol_chg	int	Y	增减量
        area	str	N	地区
        year	str	N	年度
        grade	str	N	等级
        brand	str	N	品牌
        place	str	N	产地
        pd	int	N	升贴水
        is_ct	str	N	是否折算仓单
        unit	str	Y	单位
        exchange	str	N	交易所
        """
        info = self.pro.fut_wsr(trade_date=trade_date, symbol=symbol,start_date=start_date,end_date=end_date,exchange=exchange)
        return info 

    # 结算参数
    def fut_settle(self,trade_date=None,ts_code=None,start_date=None,end_date=None,exchange=None):
        """
        trade_date	str	N	交易日期 （trade_date/ts_code至少需要输入一个参数）
        ts_code	str	N	合约代码
        start_date	str	N	开始日期
        end_date	str	N	结束日期
        exchange	str	N	交易所代码

        名称	类型	默认显示	描述
        ts_code	str	Y	合约代码
        trade_date	str	Y	交易日期
        settle	float	Y	结算价
        trading_fee_rate	float	Y	交易手续费率
        trading_fee	float	Y	交易手续费
        delivery_fee	float	Y	交割手续费
        b_hedging_margin_rate	float	Y	买套保交易保证金率
        s_hedging_margin_rate	float	Y	卖套保交易保证金率
        long_margin_rate	float	Y	买投机交易保证金率
        short_margin_rate	float	Y	卖投机交易保证金率
        offset_today_fee	float	N	平今仓手续率
        exchange	str	N	交易所
        """
        info = self.pro.fut_settle(trade_date=trade_date, ts_code=ts_code, start_date=start_date, end_date=end_date, exchange=exchange)
        return info

    # 南华期货指数日线行情
    def index_daily(self,ts_code=None,trade_date=None,start_date=None,end_date=None):
        """
        名称	类型	必选	描述
        ts_code	str	N	指数代码（南华期货指数以 .NH 结尾，具体请参考本文最下方）
        trade_date	str	N	交易日期 （日期格式：YYYYMMDD，下同）
        start_date	str	N	开始日期
        end_date	None	N	结束日期

        名称	类型	描述
        ts_code	str	TS指数代码
        trade_date	str	交易日
        close	float	收盘点位
        open	float	开盘点位
        high	float	最高点位
        low	float	最低点位
        pre_close	float	昨日收盘点
        change	float	涨跌点
        pct_chg	float	涨跌幅
        vol	float	成交量（手）
        amount	float	成交额（千元）
        """
        info = self.pro.index_daily(ts_code=ts_code, trade_date=trade_date, start_date=start_date, end_date=end_date)
        return info
    
    # 期货主力与连续合约
    def fut_mapping(self,ts_code=None,trade_date=None,start_date=None,end_date=None):
        """
        ts_code	str	N	合约代码
        trade_date	str	N	交易日期
        start_date	str	N	开始日期
        end_date	str	N	结束日期

        ts_code	str	Y	连续合约代码
        trade_date	str	Y	起始日期
        mapping_ts_code	str	Y	期货合约代码
        """
        info = self.pro.fut_mapping(ts_code=ts_code,trade_date=trade_date,start_date=start_date,end_date=end_date)
        return info
    
    # 期货主要品种交易周报
    def fut_weekly_detail(self,week=None,prd=None,start_week=None,end_week=None,exchange=None):
        """
        名称	类型	必选	描述
        week	str	N	周期（每年第几周，e.g. 202001 表示2020第1周）
        prd	str	N	期货品种（支持多品种输入，逗号分隔）
        start_week	str	N	开始周期
        end_week	str	N	结束周期
        exchange	str	N	交易所（请参考交易所说明）
        fields	str	N	提取的字段，e.g. fields='prd,name,vol'

        名称	类型	默认显示	描述
        exchange	str	Y	交易所代码
        prd	str	Y	期货品种代码
        name	str	Y	品种名称
        vol	int	Y	成交量（手）
        vol_yoy	float	Y	同比增减（%）
        amount	float	Y	成交金额（亿元）
        amout_yoy	float	Y	同比增减（%）
        cumvol	int	Y	年累计成交总量（手）
        cumvol_yoy	float	Y	同比增减（%）
        cumamt	float	Y	年累计成交金额（亿元）
        cumamt_yoy	float	Y	同比增减（%）
        open_interest	int	Y	持仓量（手）
        interest_wow	float	Y	环比增减（%）
        mc_close	float	Y	本周主力合约收盘价
        close_wow	float	Y	环比涨跌（%）
        week	str	Y	周期
        week_date	str	Y	周日期
        """
        info = self.pro.fut_weekly_detail(week=week,prd=prd,start_week=start_week,end_week=end_week,exchange=exchange,fields='exchange,prd,name,vol,vol_yoy,amount,amout_yoy,cumvol,cumvol_yoy,cumamt,cumamt_yoy,open_interest,interest_wow,mc_close,close_wow,week,week_date')
        return info
    
    def fx_obasic(self,exchange=None,classify=None,ts_code=None):
        """
        名称	类型	必选	描述
        exchange	str	N	交易商
        classify	str	N	分类
        ts_code	str	N	TS代码

        序号	分类代码	分类名称	样例
        1	FX	外汇货币对	USDCNH（美元人民币对）
        2	INDEX	指数	US30（美国道琼斯工业平均指数）
        3	COMMODITY	大宗商品	SOYF（大豆）
        4	METAL	金属	XAUUSD （黄金）
        5	BUND	国库债券	Bund（长期欧元债券）
        6	CRYPTO	加密数字货币	BTCUSD (比特币)
        7	FX_BASKET	外汇篮子	USDOLLAR （美元指数）

        名称	类型	默认显示	描述
        ts_code	str	Y	外汇代码
        name	str	Y	名称
        classify	str	Y	分类
        exchange	str	Y	交易商
        min_unit	float	Y	最小交易单位
        max_unit	float	Y	最大交易单位
        pip	float	Y	最大交易单位
        pip_cost	float	Y	点值
        traget_spread	float	Y	目标差价
        min_stop_distance	float	Y	最小止损距离（点子）
        trading_hours	str	Y	交易时间
        break_time	str	Y	休市时间
        """
        info = self.pro.fx_obasic(exchange=exchange, classify=classify,ts_code=ts_code)
        return info
    
    def fx_daily(self,ts_code=None, start_date=None, end_date=None):
        """
        名称	类型	必选	描述
        ts_code	str	N	TS代码
        trade_date	str	N	交易日期（GMT，日期是格林尼治时间，比北京时间晚一天）
        start_date	str	N	开始日期（GMT）
        end_date	str	N	结束日期（GMT）
        exchange	str	N	交易商，目前只有FXCM

        名称	类型	默认显示	描述
        ts_code	str	Y	外汇代码
        trade_date	str	Y	交易日期
        bid_open	float	Y	买入开盘价
        bid_close	float	Y	买入收盘价
        bid_high	float	Y	买入最高价
        bid_low	float	Y	买入最低价
        ask_open	float	Y	卖出开盘价
        ask_close	float	Y	卖出收盘价
        ask_high	float	Y	卖出最高价
        ask_low	float	Y	卖出最低价
        tick_qty	int	Y	报价笔数
        exchange	str	N	交易商
        """
        info = self.pro.fx_daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
        return info
    
    # GDP
    def cn_gdp(self,q=None,start_q=None,end_q=None):
        """
        名称	类型	必选	描述
        q	str	N	季度（2019Q1表示，2019年第一季度）
        start_q	str	N	开始季度
        end_q	str	N	结束季度
        fields	str	N	指定输出字段（e.g. fields='quarter,gdp,gdp_yoy'）

        名称	类型	默认显示	描述
        quarter	str	Y	季度
        gdp	float	Y	GDP累计值（亿元）
        gdp_yoy	float	Y	当季同比增速（%）
        pi	float	Y	第一产业累计值（亿元）
        pi_yoy	float	Y	第一产业同比增速（%）
        si	float	Y	第二产业累计值（亿元）
        si_yoy	float	Y	第二产业同比增速（%）
        ti	float	Y	第三产业累计值（亿元）
        ti_yoy	float	Y	第三产业同比增速（%）
        """
        info = self.pro.cn_gdp(q=q,start_q=start_q,end_q=end_q)
        return info
    
    def cn_cpi(self,m=None,start_m=None,end_m=None):
        """
        名称	类型	必选	描述
        m	str	N	月份（YYYYMM，下同），支持多个月份同时输入，逗号分隔
        start_m	str	N	开始月份
        end_m	str	N	结束月份

        名称	类型	默认显示	描述
        month	str	Y	月份YYYYMM
        nt_val	float	Y	全国当月至
        nt_yoy	float	Y	全国同比（%）
        nt_mom	float	Y	全国环比（%）
        nt_accu	float	Y	全国累计值
        town_val	float	Y	城市当值月
        town_yoy	float	Y	城市同比（%）
        town_mom	float	Y	城市环比（%）
        town_accu	float	Y	城市累计值
        cnt_val	float	Y	农村当月值
        cnt_yoy	float	Y	农村同比（%）
        cnt_mom	float	Y	农村环比（%）
        cnt_accu	float	Y	农村累计值
        """
        info = self.pro.cn_cpi(m=m,start_m=start_m, end_m=end_m)
        return info
    
    def cn_ppi(self,m=None,start_m=None, end_m=None):
        """
        名称	类型	必选	描述
        m	str	N	月份（YYYYMM，下同），支持多个月份同时输入，逗号分隔
        start_m	str	N	开始月份
        end_m	str	N	结束月份

        名称	类型	默认显示	描述
        month	str	Y	月份YYYYMM
        ppi_yoy	float	Y	PPI：全部工业品：当月同比
        ppi_mp_yoy	float	Y	PPI：生产资料：当月同比
        ppi_mp_qm_yoy	float	Y	PPI：生产资料：采掘业：当月同比
        ppi_mp_rm_yoy	float	Y	PPI：生产资料：原料业：当月同比
        ppi_mp_p_yoy	float	Y	PPI：生产资料：加工业：当月同比
        ppi_cg_yoy	float	Y	PPI：生活资料：当月同比
        ppi_cg_f_yoy	float	Y	PPI：生活资料：食品类：当月同比
        ppi_cg_c_yoy	float	Y	PPI：生活资料：衣着类：当月同比
        ppi_cg_adu_yoy	float	Y	PPI：生活资料：一般日用品类：当月同比
        ppi_cg_dcg_yoy	float	Y	PPI：生活资料：耐用消费品类：当月同比
        
        ppi_mom	float	Y	PPI：全部工业品：环比
        ppi_mp_mom	float	Y	PPI：生产资料：环比
        ppi_mp_qm_mom	float	Y	PPI：生产资料：采掘业：环比
        ppi_mp_rm_mom	float	Y	PPI：生产资料：原料业：环比
        ppi_mp_p_mom	float	Y	PPI：生产资料：加工业：环比
        
        ppi_cg_mom	float	Y	PPI：生活资料：环比
        ppi_cg_f_mom	float	Y	PPI：生活资料：食品类：环比
        ppi_cg_c_mom	float	Y	PPI：生活资料：衣着类：环比
        ppi_cg_adu_mom	float	Y	PPI：生活资料：一般日用品类：环比
        ppi_cg_dcg_mom	float	Y	PPI：生活资料：耐用消费品类：环比
        
        ppi_accu	float	Y	PPI：全部工业品：累计同比
        ppi_mp_accu	float	Y	PPI：生产资料：累计同比
        ppi_mp_qm_accu	float	Y	PPI：生产资料：采掘业：累计同比
        ppi_mp_rm_accu	float	Y	PPI：生产资料：原料业：累计同比
        ppi_mp_p_accu	float	Y	PPI：生产资料：加工业：累计同比
        
        ppi_cg_accu	float	Y	PPI：生活资料：累计同比
        ppi_cg_f_accu	float	Y	PPI：生活资料：食品类：累计同比
        ppi_cg_c_accu	float	Y	PPI：生活资料：衣着类：累计同比
        ppi_cg_adu_accu	float	Y	PPI：生活资料：一般日用品类：累计同比
        ppi_cg_dcg_accu	float	Y	PPI：生活资料：耐用消费品类：累计同比

        """
        info = self.pro.cn_ppi(m=m,start_m=start_m, end_m=end_m)
        return info
    
    def cn_m(self,m=None,start_m=None,end_m=None):
        """
        
        m	str	N	月度（202001表示，2020年1月）
        start_m	str	N	开始月度
        end_m	str	N	结束月度
        fields	str	N	指定输出字段（e.g. fields='month,m0,m1,m2'）

        名称	类型	默认显示	描述
        month	str	Y	月份YYYYMM
        m0	float	Y	M0（亿元）
        m0_yoy	float	Y	M0同比（%）
        m0_mom	float	Y	M0环比（%）
        m1	float	Y	M1（亿元）
        m1_yoy	float	Y	M1同比（%）
        m1_mom	float	Y	M1环比（%）
        m2	float	Y	M2（亿元）
        m2_yoy	float	Y	M2同比（%）
        m2_mom	float	Y	M2环比（%）
        """
        info = self.pro.cn_m(m=m,start_m=start_m, end_m=end_m)
        return info
    
    def shibor(self,date=None,start_date=None, end_date=None):
        """
        名称	类型	必选	描述
        date	str	N	日期 (日期输入格式：YYYYMMDD，下同)
        start_date	str	N	开始日期
        end_date	str	N	结束日期

        名称	类型	默认显示	描述
        date	str	Y	日期
        on	float	Y	隔夜
        1w	float	Y	1周
        2w	float	Y	2周
        1m	float	Y	1个月
        3m	float	Y	3个月
        6m	float	Y	6个月
        9m	float	Y	9个月
        1y	float	Y	1年
        """
        info = self.pro.shibor(date=date,start_date=start_date, end_date=end_date)
        return info
    
    # 短期国债利率
    def us_tbr(self,date=None,start_date=None,end_date=None):
        """
        名称	类型	必选	描述
        date	str	N	日期
        start_date	str	N	开始日期(YYYYMMDD格式)
        end_date	str	N	结束日期

        名称	类型	默认显示	描述
        date	str	Y	日期
        w4_bd	float	Y	4周银行折现收益率
        w4_ce	float	Y	4周票面利率
        w8_bd	float	Y	8周银行折现收益率
        w8_ce	float	Y	8周票面利率
        w13_bd	float	Y	13周银行折现收益率
        w13_ce	float	Y	13周票面利率
        w26_bd	float	Y	26周银行折现收益率
        w26_ce	float	Y	26周票面利率
        w52_bd	float	Y	52周银行折现收益率
        w52_ce	float	Y	52周票面利率
        """
        info = self.pro.us_tbr(date=date,start_date=start_date,end_date=end_date)
        return info
    
    # 国债长期利率
    def us_tltr(self,date=None,start_date=None,end_date=None):
        """
        名称	类型	必选	描述
        date	str	N	日期
        start_date	str	N	开始日期
        end_date	str	N	结束日期
        fields	str	N	指定字段

        名称	类型	默认显示	描述
        date	str	Y	日期
        ltc	float	Y	收益率 LT COMPOSITE (>10 Yrs)
        cmt	float	Y	20年期CMT利率(TREASURY 20-Yr CMT)
        e_factor	float	Y	外推因子EXTRAPOLATION FACTOR
        """
        info = self.pro.us_tltr(date=date,start_date=start_date,end_date=end_date)
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
# print(tushare.fut_basic())
# print(tushare.fut_daily(ts_code='JD1907.DCE', start_date='20180101', end_date='20201231'))
# print(tushare.fut_daily(exchange="DCE", start_date='20180101', end_date='20201231'))
# print(tushare.fut_daily(start_date='20180101', end_date='20201231'))
# print(tushare.fut_holding(symbol='C'))
# print(tushare.fut_holding(trade_date='20181113', symbol='ZN'))
# print(tushare.fut_settle(trade_date='20181114', exchange='SHFE'))
# print(
#     tushare.index_daily(ts_code='CU.NH', start_date='20180101', end_date='20181201')
# )
# print(
#     tushare.fut_mapping(ts_code='TF.CFX')
# )
# print(
#     tushare.fut_weekly_detail(prd='CU', start_week='202001', end_week='202003')
# )
# print(
#     tushare.fx_obasic(exchange='FXCM', classify='INDEX')
# )
# print(
#     tushare.fx_daily(ts_code='USDCNH.FXCM', start_date='20190101', end_date='20190524')
# )
# print(
#     tushare.cn_gdp(start_q='2020Q1', end_q='2020Q4')
# )
# print(
#     tushare.cn_cpi(start_m='201801', end_m='201903')
# )
# print(
#     tushare.cn_ppi(start_m='201905', end_m='202005')
# )
# print(
#     tushare.cn_m(start_m='201901', end_m='202003')
# )
# print(
#     tushare.us_tbr(start_date='20180101', end_date='20200327')
# )
# print(
#     tushare.us_tltr(start_date='20180101', end_date='20200327')
# )