from datetime import datetime
import backtrader as bt  # 导入 Backtrader
import backtrader.indicators as btind  # 导入策略分析模块
import backtrader.feeds as btfeeds  # 导入数据模块

if __name__ == '__main__':
    data = bt.feeds.GenericCSVData(
        dataname="../resource/feed/BTC-USDT-SWAP.csv",
        fromdate=datetime.strptime("2020-05-31 23:59:00", "%Y-%m-%d %H:%M:%S"),  # 起止日期
        todate=datetime.strptime("2022-06-05 20:08:00", "%Y-%m-%d %H:%M:%S"),
        nullvalue=0.0,
        dtformat=("%Y-%m-%d %H:%M:%S"),  # 日期列的格式
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
    # 回测启动运行
    cerebro.run()
    cerebro.plot(dpi=100)
