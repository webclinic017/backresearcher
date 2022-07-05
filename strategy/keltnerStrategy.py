#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：liuyx
@Date    ：2022/7/5 11:55 上午 
@Description ：backresearcher 
"""

import backtrader as bt
import backtrader.indicators as btind

from strategy.AdvanceBaseStrategy import AdvanceBaseStrategy


class KeltnerStrategy(AdvanceBaseStrategy):
    def __init__(self):
        super().__init__()
        self.atr = btind.AverageTrueRange(self.data, period=10)  # atr
        self.ema = btind.ExponentialMovingAverage(self.data.close, period=20)
        # self.upper = self.ema + self.atr * 2
        # self.lower = self.ema - self.atr * 2

        self.buy_signal = bt.And(self.data.open(0) < self.ema.ema(0) + 2 * self.atr.atr(0), self.data.close(0) > self.ema.ema(0) + 2 * self.atr.atr(0))
        self.sell_signal = bt.And(self.data.open(0) > self.ema.ema(0) - 2 * self.atr.atr(0), self.data.close(0) < self.ema.ema(0) - 2 * self.atr.atr(0))

    def next(self):
        if self.buy_signal[0]:
            # self.
            pass
        if self.sell_signal[0]:
            pass
