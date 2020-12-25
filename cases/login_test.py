# -*- coding: UTF-8 -*-
# @time     : 2020-11-23 16:03
# @Auther   : Aaron
# @File     : pytest.py

import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from data.login_data import cases_error, case_success


class TestLogin:

    @pytest.mark.parametrize("test_info", cases_error)
    def test_login_fail(self, test_info, browser):
        login_page = LoginPage(browser)
        login_page.login(test_info["mobile"], test_info["pwd"])
        user_info = login_page.erroe_msg_elem()
        try:
            assert test_info["expected"] == user_info
            print("pass")
        except AssertionError as e:
            print("not pass")
            raise e

    @pytest.mark.parametrize("test_info", case_success)
    def test_login_success(self, test_info, browser):
        login_page = LoginPage(browser)
        login_page.login(test_info["mobile"], test_info["pwd"])
        user_info = HomePage(browser).get_user_account()
        try:
            assert test_info["expected"] == user_info
            print("pass")
        except AssertionError as e:
            print("not pass")
            raise e

