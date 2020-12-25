# -*- coding: UTF-8 -*-
# @time     : 2020-11-25 11:43
# @Auther   : Aaron
# @File     : base.page.py

from selenium.webdriver import Chrome


class BasePage:

    def __init__(self, driver: Chrome):
        self.driver = driver

    def find(self, locator):
        """查找元素"""
        try:
            e = self.driver.find_element(*locator)
            return e
        except Exception as err:
            print(f"元素定位失败{err}")

    def find_and_send(self, locator, input_content):
        """查找元素并输入内容"""
        self.find(locator).send_keys(input_content)



