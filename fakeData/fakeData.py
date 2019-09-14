#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import time
from typing import List, Any


def test():
    print("test")
    return


def getTouchData(amount = 64):
    touchData = []
    return touchData


def getAccData(amount = 300) -> object:
    accData: List[Any] = []
    return accData


def getGyroData(amount = 300):
    gyroData = []
    return gyroData


if __name__ == '__main__':
    behaviorData = {"ps": "1920*1080"}

    """1. 生成触屏数据 """
    behaviorData["ts"] = getTouchData()

    """2. 生成加速度数据acc"""
    behaviorData["acc"] = getAccData()

    """3. 生成陀螺仪数据gyro"""
    behaviorData["gyro"] = getGyroData()

    """4. 写json数据文件"""
    fileName = "fakeData-" + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + ".txt"
    outFile = open("/home/alex/workstudio/botDetect/data/bot/fakeData/" + fileName, "w")
    jsonStr = json.dump(behaviorData, outFile)

    test()
