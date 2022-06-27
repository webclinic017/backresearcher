#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：liuyx
@Date    ：2022/6/15 9:34 下午 
@Description ：backresearcher 
"""
import backtrader as bt
import backtrader.indicators as btind

from strategy.AdvanceBaseStrategy import AdvanceBaseStrategy


class BollBandsStrategy(AdvanceBaseStrategy):
    def __init__(self):
        super().__init__()
        self.boll = btind.BollingerBands(self.data.close, period=20)  # boll
        self.atr = btind.AverageTrueRange(self.data, period=20)  # atr
        self.rsi = btind.RelativeStrengthIndex(self.data.close, period=20)
        self.close_cross_down_top = bt.And(self.data.close(-1) > self.boll.top(-1), self.data.close(0) < self.boll.top(0))
        self.close_cross_over_top = bt.And(self.data.close(-1) < self.boll.top(-1), self.data.close(0) > self.boll.top(0))
        self.close_cross_down_bot = bt.And(self.data.close(-1) > self.boll.bot(-1), self.data.close(0) < self.boll.bot(0))
        self.close_cross_over_bot = bt.And(self.data.close(-1) < self.boll.bot(-1), self.data.close(0) > self.boll.bot(0))

    def next(self):

        # print(f"Boll:mid:{self.boll.mid(0)},top:{self.boll.top(0)},bot:{self.boll.bot(0)}")

        # print(self.close_cross_down_top(0))

        # close cross down top,open short
        if self.close_cross_down_bot[0]:
            brackets = self.sell_bracket(price=self.data.close[0], size=3000 / self.data.close[0],
                                         limitprice=self.data.close[0] - 2 * self.atr.atr[0],
                                         stopprice=self.data.high[0] + self.atr.atr[0])

        # close cross up bot,open long
        if self.close_cross_over_top[0]:
            brackets = self.buy_bracket(price=self.data.close[0], size=3000 / self.data.close[0],
                                        limitprice=self.data.close[0] + 2 * self.atr.atr[0],
                                        stopprice=self.data.low[0] - self.atr.atr[0])
