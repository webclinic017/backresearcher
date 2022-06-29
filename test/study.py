from datetime import datetime
import backtrader as bt  # 导入 Backtrader
import backtrader.indicators as btind  # 导入指标分析模块
import backtrader.feeds as btfeeds  # 导入数据模块

from strategy.BollBandsStrategy import BollBandsStrategy

data = bt.feeds.GenericCSVData(
    dataname="../resource/feed/BTC-USDT-SWAP-week.csv",
    fromdate=datetime.strptime("2022-06-27 00:01:00", "%Y-%m-%d %H:%M:%S"),  # 起止日期
    todate=datetime.strptime("2022-06-28 20:50:00", "%Y-%m-%d %H:%M:%S"),
    nullvalue=0.0,
    dtformat="%Y-%m-%d %H:%M:%S",  # 日期列的格式
    datetime=0,  # 各列的位置，从0开始，如列缺失则为None，-1表示自动根据列名判断
    open=1,
    high=2,
    low=3,
    close=4,
    volume=5,
    openinterest=6
)

cerebro = bt.Cerebro()

# 从自定义类加载数据
cerebro.adddata(data)

# 经纪商配置
cerebro.broker.setcash(35000)
cerebro.broker.setcommission(0.0004)

# cerebro.signal_accumulate(True)
# cerebro.signal_concurrency(True)

cerebro.addstrategy(BollBandsStrategy)
# 回测启动运行
cerebro.run()
print('组合期末资金: %.2f' % cerebro.broker.getvalue())
cerebro.plot(dpi=300)
