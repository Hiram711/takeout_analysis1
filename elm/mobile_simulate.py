# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

if not cli_setup():
    auto_setup(__file__, logdir=None, devices=[
        "Android://127.0.0.1:5037/127.0.0.1:62001?cap_method=JAVACAP&&ori_method=ADBORI",
    ])

# script content
print("start...")
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
time.sleep(3)
poco("饿了么").click()
time.sleep(30)
while not poco(text='推荐商家'):
    poco.swipe([0.5, 0.9], [0.5, 0.1])
    time.sleep(1)

poco(text="距离").click()

for i in range(25000):
    poco.swipe([0.5, 0.9], [0.5, 0.1])
    time.sleep(1)
