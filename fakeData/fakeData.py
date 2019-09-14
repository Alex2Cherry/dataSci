#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import random
import time
import copy
from typing import List, Any


def test():
    print("test")
    return


def getTouchData(amount = 64):
    touchData = []
    return touchData


def getAccData(amount = 300) -> object:
    accData: List[Any] = []

    startTime = int(time.time() * 1000)
    max_x = 4.490255453651858
    min_x = -7.425179762145812
    max_y = 3.0074126327164348
    min_y = -5.769433205108815
    max_z = 12.511322
    min_z = 4.4683566

    dataItem = dict()
    for idx in range(amount):
        dataItem["t"] = startTime + 200 * idx
        dataItem["x"] = random.uniform(min_x, max_x)
        dataItem["y"] = random.uniform(min_y, max_y)
        dataItem["z"] = random.uniform(min_z, max_z)
        accData.append(copy.deepcopy(dataItem))

    return accData


def getGyroData(amount = 300):
    gyroData = []

    startTime = int(time.time() * 1000)
    max_x = 0.7631976
    min_x = -0.9423207
    max_y = 1.172355
    min_y = -2.0713217
    max_z = 0.5539326
    min_z = -0.91334826

    dataItem = dict()
    for idx in range(amount):
        dataItem["t"] = startTime + 200 * idx
        dataItem["x"] = random.uniform(min_x, max_x)
        dataItem["y"] = random.uniform(min_y, max_y)
        dataItem["z"] = random.uniform(min_z, max_z)
        gyroData.append(copy.deepcopy(dataItem))

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
