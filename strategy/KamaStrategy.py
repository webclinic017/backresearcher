#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：liuyx
@Date    ：2022/6/22 7:59 下午 
@Description ：backresearcher 
"""

import backtrader as bt
import backtrader.indicators as btind

from strategy.AdvanceBaseStrategy import AdvanceBaseStrategy


class KamaStrategy(AdvanceBaseStrategy):
    def __int__(self):
        self.kama = btind.AdaptiveMovingAverage(period=30)
        self.short_orders = list()
        self.long_orders = list()

    def __get_turn_point(self) -> float:
        length = len(self.kama.kama)
        if length > 2:
            for i in range(0, 2 - length, -1):
                if (self.kama.kama[i] > self.kama.kama[i - 1] < self.kama.kama[i - 2]) or (self.kama.kama[i] < self.kama.kama[i - 1] > self.kama.kama[i - 2]):
                    return self.kama.kama[i - 1]
        return None

    def next(self):
        turn_price = self.__get_turn_point()

        if turn_price:
            if 0 < (self.data.close[-1] - turn_price) / turn_price < 0.001 < (self.data.close[0] - turn_price) / turn_price:
                # todo open long
                pass

            if (self.data.close[0] - turn_price) / turn_price < -0.001 < (self.data.close[-1] - turn_price) / turn_price < 0:
                #  todo open short
                pass
