#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File    :   test_sim.py    
@License :   (C)Copyright 2017-2020, Pickwick

@Modify Time    @Author     @Version    @Desciption
------------    -------     --------    -----------
2019/8/29       pickwick    1.0         创建.
"""

import sim

def print_scene_time(scene):
    print("scene time: {}\n".format(scene.time_info))

def print_entity_info(obj):
    print("* entity {}: time {}".format(obj.id, obj.time_info))

class EntityPrinter:
    def __call__(self, obj):
        print("+ entity {}: time {}".format(obj.id, obj.time_info))

scene = sim.Scene()

obj1 = sim.Entity()
scene.add(obj1)
obj1.step_handlers += [EntityPrinter()] # 方法1：绑定可调用对象.

obj2 = scene.add(sim.Entity())
obj2.step_handlers += [print_entity_info] # 方法2：绑定函数对象.

scene.step_handlers += [print_scene_time] # 绑定场景步进.

scene.run(0, 5)
