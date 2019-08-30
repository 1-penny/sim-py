#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File    :   test_tool.py    
@License :   (C)Copyright 2017-2020, Pickwick

@Modify Time    @Author     @Version    @Desciption
------------    -------     --------    -----------
2019/8/29       pickwick    1.0         创建.
"""

import unittest
from sim import tool


class Test(unittest.TestCase):
    def test_vec(self):
        self.assertEqual(tool.add_v([1, 2], [3, 4]), [4, 6])
        self.assertEqual(tool.mul_v([1, 2], [3, 4]), [3, 8])
        self.assertEqual(tool.mul_va([1, 2], 3), [3, 6])


if __name__ == '__main__':
    unittest.main()
