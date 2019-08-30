#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File    :   radar.py    
@License :   (C)Copyright 2017-2020, Pickwick

@Modify Time    @Author     @Version    @Desciption
------------    -------     --------    -----------
2019/8/29       pickwick    1.0         创建.
"""

import sim


class Radar(sim.Entity):
    """ 雷达.   
    """

    def __init__(self, **kwargs):
        """ 雷达构造函数.

        TODO: Radar init.
        """
        super().__init__()
        self.position = [0., 0., 0.]

    def step(self):
        pass

    def access(self, other):
        """  被其他对象影响.
        探测其他可探测对象，形成探测结果.

        TODO: radar access.
        """
        if hasattr(other, 'detectable'):
            pass
