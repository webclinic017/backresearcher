#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：liuyx
@Date    ：2022/7/4 8:04 下午 
@Description ：backresearcher 
"""
import backtrader as bt
import backtrader.indicators as btind

from strategy.AdvanceBaseStrategy import AdvanceBaseStrategy


class RsiStrategy(AdvanceBaseStrategy):
    def __init__(self):
        super().__init__()
        self.rsi = btind.RelativeStrengthIndex(self.data.close, period=3)
        self.atr = btind.AverageTrueRange(self.data, period=14)  # atr

        self.buy_signal = bt.And(self.rsi.rsi(-1) > 3, self.rsi.rsi(0) < 3)
        self.sell_signal = bt.And(self.rsi.rsi(-1) < 97, self.rsi.rsi(0) > 97)

    def next(self):

        if self.buy_signal[0]:
            pos = self.getposition()
            if pos:
                print(f"Current Position:{pos.size}")

            size = 3000 / self.data.close[0]
            self.buy_bracket(price=self.data.close[0], size=3000 / self.data.close[0],
                             limitprice=self.data.close[0] + 2*self.atr.atr[0],
                             stopprice=self.data.low[0] * 0.95)
        #
        # if self.sell_signal[0]:
        #     self.close()
