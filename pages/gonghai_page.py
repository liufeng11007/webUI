# -*- coding: UTF-8 -*-
# @time     : 2020-12-07 15:40
# @Auther   : Aaron
# @File     : gonghai_page.py


from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Gonghai(BasePage):

    url = "http://staging.ukuaiqi.com/dashboard#customer-public"

    # 公海客户总数
    total_numb = (By.XPATH, '//span[@class="totalRecords-span"]')

    # 全选







