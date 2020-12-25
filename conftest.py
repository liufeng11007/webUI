# -*- coding: UTF-8 -*-
# @time     : 2020-11-23 16:07
# @Auther   : Aaron
# @File     : configtest.py
import time

import pytest
from selenium import webdriver

from data.login_data import case_success
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.fixture(scope="class")
def browser():
    """启动浏览器和关闭浏览器"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver

    driver.quit()


@pytest.fixture(scope="class")
def login(browser):
    login_page = LoginPage(browser)
    user_info = case_success[0]
    login_page.login(user_info["mobile"], user_info["pwd"])

    yield browser


@pytest.fixture()
def xiansuo(browser):
    click = HomePage(login)
    time.sleep(3)
    click.click_crm_menu()
    click.click_xiaosouxiansuo()
    time.sleep(3)




