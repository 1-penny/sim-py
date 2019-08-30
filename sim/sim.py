#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File    :   sim.py    
@License :   (C)Copyright 2017-2020, Pickwick

@Modify Time    @Author     @Version    @Desciption
------------    -------     --------    -----------
2019/8/29       pickwick    1.0         创建.
"""

import copy
import time
from .tool import round_f


class EntityIdGenerator(object):
    """ 实体ID产生器.
    """
    current_id = 0

    @classmethod
    def gen(cls):
        """ 产生一个新的ID.
        """
        cls.current_id += 1
        return cls.current_id


class Entity(object):
    """ 仿真实体.

    :attribute step_handlers: 步进处理句柄. 
    """

    def __init__(self):
        """ 实体构造函数.
        """
        self.step_handlers = []
        self._id = EntityIdGenerator.gen()
        self._scene = None

    @property
    def id(self):
        """ 返回实体ID.
        """
        return self._id

    @property
    def time_info(self):
        """ 获取时间信息.
        """
        return self._scene.time_info if self._scene is not None else None

    def step(self):
        """ 步进.
        """
        pass

    def access(self, other):
        """ 被其他对象影响.
        """
        pass

    def attach(self, scene):
        """ 绑定场景.
        """
        self._scene = scene

    def reset(self):
        """ 重置状态.
        """
        pass


class Scene(object):
    """ 仿真场景.

    :attribute realtime_mode: 实时模式.  
    :attribute step_handlers: 步进处理句柄.   
    """

    def __init__(self):
        """ 仿真场景构造函数.
        """
        self.step_handlers = []
        self.realtime_mode = True
        self.objects = []

        self._current_time = None
        self._start_time = None
        self._end_time = None
        self._step_time = 0.1

        self._real_start_time = 0

    def add(self, obj):
        """ 向场景添加实体.
        """
        if obj not in self.objects:
            obj.attach(self)
            self.objects.append(obj)
        return obj

    def run(self, start, duration, step=0.1):
        """ 连续运行仿真.

        :param start:起始时间   
        :param duration:仿真时长
        :param step:仿真步长      
        """
        for obj in self.objects:
            obj.reset()

        self._init_loop(start, duration, step)

        while not self._is_finished():
            self._step()

            for handler in self.step_handlers:
                handler(self)

            self._current_time = round_f(self._current_time + self._step_time)
            self._sync_time()

    @property
    def time_info(self):
        """ 当前仿真时间信息.   

        :return: (当前时间, 起始时间, 时间步长)
        """
        return self._current_time, self._start_time, self._step_time

    def _init_loop(self, start, duration, step):
        """ 初始化仿真循环.
        """
        self._start_time = time.time() if start is None else start
        self._end_time = None if duration is None else (
            self._start_time + duration)
        self._step_time = step

        self._start_time = round_f(self._start_time)
        self._end_time = round_f(self._end_time)
        self._step_time = round_f(self._step_time)

        self._current_time = self._start_time

        self._real_start_time = time.time()

    def _step(self):
        """ 执行单步仿真.
        """
        # 1.所有对象状态步进一次.
        for obj in self.objects:
            obj.step()

        # 2.所有对象与场景中其他对象相互作用一次.
        mirror_objects = copy.deepcopy(self.objects)
        for obj in self.objects:
            for mirror_obj in mirror_objects:
                if obj.id != mirror_obj.id:
                    obj.access(mirror_obj)

        # 3.调用对象步进消息.
        for obj in self.objects:
            for handler in obj.step_handlers:
                handler(obj)

    def _sync_time(self):
        """ 同步时间.
        """
        if self.realtime_mode:
            real_diff_t = time.time() - self._real_start_time
            want_diff_t = self._current_time - self._start_time
            diff_t = want_diff_t - real_diff_t
            if diff_t > 0.01:
                time.sleep(diff_t)

    def _is_finished(self):
        """ 判断仿真是否可以结束.
        """
        if self._start_time is None or self._end_time is None:
            return True

        return self._current_time > self._end_time


if __name__ == '__main__':
    pass
