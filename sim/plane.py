#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File    :   plane.py    
@License :   (C)Copyright 2017-2020, Pickwick

@Modify Time    @Author     @Version    @Desciption
------------    -------     --------    -----------
2019/8/29       pickwick    1.0         创建.
"""


import sim
from sim import tool


class Plane(sim.Entity):
    """ 飞行器.   
    按照规定航线进行飞行的平台。
    """

    def __init__(self):
        super().__init__()
        self.position = [0., 0., 0.]
        self._prev_position = None
        self.velocity = [0., 0., 0.]
        self.detectable = True
        self.flyroute = None

    def step(self):
        """ 步进.
        根据航迹航行.
        """
        curr, start, step = self.time_info
        self.position = self.flyroute.get_pos(curr - start)

        if self.position is None or self._prev_position is None:
            self.velocity = [0., 0., 0.]
        else:
            self.velocity = tool.sub_v(self.position, self._prev_position)
            self.velocity = tool.mul_va(self.velocity, 1.0 / step)
        self._prev_position = self.position


"""
航线（Flyroute）：由一组航点（Waypoint）组成。
航点：（坐标，时间）

可以通过航线图，计算出任意时刻飞机的位置（position）和速度（velocity）。其中：
a. 位置如果是None，表示飞机没有飞行。
b. 速度如果是None，表示飞机没有飞行。

位置和速度的计算：
a. 位置，通过对相邻航点之间插值的方法计算的。
b. 速度，通过与前一次位置差分计算的。

对飞机飞行方式的抽象考虑可以抽象成一个飞控（航线管理），目前是考虑按固定航线飞行，以后可能要实现：
1. 具备悬停功能
2. 具备返航功能（按规定速度返回上一个航点）
3. 具备按指定位置前进功能
4. 具备按特定飞行方式飞行功能。
"""


class Flyroute:
    """ 航线.
    """

    def __init__(self):
        self.waypoints = []

    def get_pos(self, t):
        """ 计算给定时刻的位置.

        :param t:给定时刻.
        :return 当前位置，或者None

        TODO: Flyroute get_pos
        """
        return [0., 0., 0.]


class Waypoint:
    """ 航点.
    """

    def __init__(self, position, t):
        self.time = t
        self.position = position
