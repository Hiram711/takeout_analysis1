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
poco(text="浏览器").click()
time.sleep(10.0)
poco(resourceId="com.android.browser:id/url").click()
text('https://h5.waimai.meituan.com/waimai/mindex/home')
time.sleep(60.0)
poco(text="距离最近").click()
for i in range(10):
    time.sleep(1)
    poco.swipe([0.5, 0.8], [0.5, 0.1])
