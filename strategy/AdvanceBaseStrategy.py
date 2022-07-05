#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：liuyx
@Date    ：2022/6/16 9:30 上午 
@Description ：backresearcher 
"""

import backtrader as bt


class AdvanceBaseStrategy(bt.Strategy):
    def __init__(self):
        self.order_status = {0: "Created",
                             1: "Submitted",
                             2: "Accepted",
                             3: "Partial",
                             4: "Completed",
                             5: "Canceled",
                             6: "Expired",
                             7: "Margin",
                             8: "Rejected"}
        super().__init__()

    def log(self, s):

        print("%s %s" % (self.datas[0].datetime.date(0), s))

    # def notify_order(self, order):
    #     if order.status in [order.Submitted, order.Accepted]:
    #         return
    #
    #     if order.status in [order.Completed]:
    #
    #         if order.isbuy():
    #             self.log(
    #                 'Buy, price: %.2f, value: %.2f, commission %.2f' %
    #                 (order.executed.price,
    #                  order.executed.value,
    #                  order.executed.comm))
    #
    #             self.buyprice = order.executed.price
    #             self.buycomm = order.executed.comm
    #         elif order.issell():
    #             self.log('Sell, price: %.2f, value: %.2f, commission %.2f' %
    #                      (order.executed.price,
    #                       order.executed.value,
    #                       order.executed.comm))
    #         # 记录当前交易数量
    #         self.bar_executed = len(self)
    #
    #     elif order.status in [order.Canceled, order.Margin, order.Rejected]:
    #         self.log(self.order_status.get(order.status))
    #     self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return
        self.log('TradePnl: %.2f,TradePnlcomm%.2f' % (trade.pnl, trade.pnlcomm))
