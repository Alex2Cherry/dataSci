#!/usr/bin/python
# -*- coding: UTF-8 -*-

""" glaxy9模拟器自动化操控脚本 """

import uiautomator2 as u2
import time
import random


def test():
    print("test")


def doAutoTask(d):
    """2.启动APP"""
    d.app_start("com.anc.botdetectdemo", ".MainActivity")
    time.sleep(5)

    """3. 向下滑动两次"""
    d.swipe(600, 700, 400, 300)
    time.sleep(random.randint(1, 5))

    d.swipe(666, 713, 515, 443)
    # time.sleep(random.randint(3, 10))

    """4. 勾选复选框"""
    d(scrollable=True).scroll.toEnd()
    d(text="朕知道了").click()
    time.sleep(1)

    """5. 向上滑动两次"""
    d.swipe(600, 300, 400, 852)
    time.sleep(random.randint(1, 5))

    d.swipe(666, 230, 515, 763)

    """6. 填写用户名/密码"""
    d(scrollable=True).scroll.toBeginning()

    d(text="UserName").set_text("13826513967")
    time.sleep(2)
    d.press("back")
    time.sleep(random.randint(1, 5))

    d(text="password").set_text("12345678")
    time.sleep(2)
    d.press("back")
    time.sleep(random.randint(3, 8))

    """7. 点击LOGIN,退出APP"""
    d(text="LOGIN").click()
    time.sleep(random.randint(1, 5))

    d.press("back")
    d.press("back")

    return


if __name__ == '__main__':
    """1.连接设备"""
    d = u2.connect()
    assert isinstance(d.info, object)
    print(d.info)

    times = 6
    for idx in range(times):
        doAutoTask(d)
        time.sleep(10)

    test()
