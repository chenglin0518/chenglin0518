#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :Appium_commmon.py
# @Time      :2024/4/17 22:04
# @Author    :ChengLinfeng

from appium import webdriver

desired_caps = {  
    "platformName": "Android",  
    "deviceName": "Android Emulator",  
    "appPackage": "com.example.app",  
    "appActivity": ".MainActivity",  
}  

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  
driver.find_element_by_xpath('//android.widget.Button[@text="Click me"]').click()  
driver.quit()


if __name__ == "__main__":
      run_code = 0
