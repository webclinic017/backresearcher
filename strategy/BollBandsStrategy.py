#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：liuyx
@Date    ：2022/6/15 9:34 下午 
@Description ：backresearcher 
"""
import backtrader as bt
import backtrader.indicators as btind

from strategy.BaseStrategy import BaseStrategy


class BollBandsStrategy(BaseStrategy):
    def __init__(self):
        super().__init__()
        self.boll = btind.BollingerBands(self.data.close, period=20)  # boll
        self.atr = btind.AverageTrueRange(self.data, period=14)  # atr

    def next(self):

        print(f"Boll:mid:{self.boll.mid[0]},top:{self.boll.top[0]},bot:{self.boll.bot[0]}")

        buy_signal = bt.And(self.date.close[-1] > self.boll.top[-1], self.date.close[0] < self.boll.top[0])
        sell_signal = bt.And(self.date.close[-1] < self.boll.top[-1], self.date.close[0] > self.boll.top[0])

        # close cross down top,open short
        if buy_signal[0]:
            # brackets =
            pass

        # close cross up bot,open long
        if sell_signal[0]:
            pass
