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
        # self.boll = btind.BollingerBands(self.data.close, period=60)  # boll
        # self.atr = btind.AverageTrueRange(self.data, period=60)  # atr
        self.rsi = btind.RelativeStrengthIndex(self.data.close, period=3)

        self.buy_signal = bt.And(self.rsi.rsi(-1) > 3, self.rsi.rsi(0) < 3)
        self.sell_signal = bt.And(self.rsi.rsi(-1) < 97, self.rsi.rsi(0) > 97)
        # self.close_cross_down_top = bt.And(self.data.close(-1) > self.boll.top(-1), self.data.close(0) < self.boll.top(0))
        # self.close_cross_over_top = bt.And(self.data.close(-1) < self.boll.top(-1), self.data.close(0) > self.boll.top(0))

    def next(self):

        if self.buy_signal[0]:
            self.buy_bracket(size=3000 / self.data.close[0], price=self.data.close[0], stopprice=self.data.low[0] * 0.95)

        if self.sell_signal[0]:
            self.sell(exectype=bt.Order.Close)
