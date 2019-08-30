#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File    :   tool.py    
@License :   (C)Copyright 2017-2020, Pickwick

@Modify Time    @Author     @Version    @Desciption
------------    -------     --------    -----------
2019/8/29       pickwick    1.0         创建.
"""

import math

def round_f(v):
    return round(v, 4)

def angle_v(v0, v1):
    """ 计算向量之间的夹角. 
    """
    n = norm(v0) * norm(v1)
    if n > 0:
        a = dot_v(v0, v1) / (norm(v0) * norm(v1))
        return math.degrees(math.acos(a))
    else:
        return 0


def proj_v(v0, v1):
    """ 向量投影.   
    计算向量v1 在向量v0 上的投影.
    """
    v = mul_va(v0, 1 / norm(v0))
    a = dot_v(v, v1)
    return mul_va(v, a)


def dot_v(v0, v1):
    """ 向量内积. 
    """
    return sum(mul_v(v0, v1))


def mul_va(v, a):
    """ 向量数乘.   
    计算向量v 与标量a 的乘积.
    """
    return list(map(lambda x: x * a, v))


def add_va(v, a):
    """ 向量数加.   
    计算向量v 与标量a 的和.
    """
    return list(map(lambda x: x + a, v))


def add_v(v1, v2):
    """ 计算向量之和. 
    """
    return list(map(lambda x1, x2: x1 + x2, v1, v2))


def sub_v(v1, v2):
    """ 计算向量之差. 
    """
    return list(map(lambda x1, x2: x1 - x2, v1, v2))


def mul_v(v1, v2):
    """ 计算向量(对应元素)之积.
     """
    return list(map(lambda x1, x2: x1 * x2, v1, v2))


def dist_v(p1, p2):
    """ 计算两个点之间的距离. 
    """
    return norm(sub_v(p1, p2))


def norm(v):
    """ 计算向量的模. 
    """
    t2 = sum(list(map(lambda x: x * x, v)))
    return math.sqrt(t2)