from datetime import datetime
import backtrader as bt  # 导入 Backtrader
import backtrader.indicators as btind  # 导入指标分析模块
import backtrader.feeds as btfeeds  # 导入数据模块

from strategy.BollBandsStrategy import BollBandsStrategy


class TestStrategy(bt.Strategy):
    def __init__(self):
        print("--------- 打印 self 策略本身的 lines ----------")
        print(self.lines.getlinealiases())

        print("--------- 指标计算 ----------")
        self.boll = btind.BollingerBands(self.data.close)

    def next(self):
        # print('验证索引位置为 6 的线是不是 datetime')
        print(self.data.close[0])


data = bt.feeds.GenericCSVData(
    dataname="../resource/feed/Test.csv",
    fromdate=datetime.strptime("2020-05-31 23:59:00", "%Y-%m-%d %H:%M:%S"),  # 起止日期
    todate=datetime.strptime("2022-06-05 20:08:00", "%Y-%m-%d %H:%M:%S"),
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
cerebro.broker.setcommission(0.0003)

# cerebro.signal_accumulate(True)
# cerebro.signal_concurrency(True)

cerebro.addstrategy(BollBandsStrategy)
# 回测启动运行
cerebro.run()
# cerebro.plot(dpi=300)
