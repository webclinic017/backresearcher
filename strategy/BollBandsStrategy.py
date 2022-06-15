#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：liuyx
@Date    ：2022/6/15 9:34 下午 
@Description ：backresearcher 
"""

import backtrader as bt
import backtrader.indicators as btind


class BollBandsStrategy(bt.Strategy):
    def __init__(self):
        self.boll = btind.BollingerBands(self.data.close, period=20)

    def next(self):
        pass
