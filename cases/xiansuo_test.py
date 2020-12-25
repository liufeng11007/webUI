# -*- coding: UTF-8 -*-
# @time     : 2020-11-24 10:03
# @Auther   : Aaron
# @File     : xiansuo.py

import pytest,time
from pages.home_page import HomePage
from pages.xiansuo_page import XianSuo
from data.xiansuo_data import case_success,case_required

@pytest.mark.staging
@pytest.mark.xiansuo
class Test_Xiansuo:
    # @pytest.mark.skip
    @pytest.mark.parametrize("test_info", case_required)
    def test_tips(self, test_info, login):
        # print(test_info)
        # click = HomePage(login)
        # time.sleep(3)
        # click.click_crm_menu()
        # click.click_xiaosouxiansuo()
        # time.sleep(3)
        createxs = XianSuo(login)
        # createxs.refresh()
        # time.sleep(3)
        createxs.get()
        time.sleep(3)
        createxs.click_xinjianxiansuo()
        time.sleep(3)
        createxs.create_xiansuo(test_info)
        time.sleep(3)
        createxs.click_commite()
        time.sleep(3)
        actual_result = createxs.get_tips()
        try:
            assert test_info["expected"] == actual_result
            print("测试用例通过！")
        except AssertionError as e:
            print(f"测试用例不同：{e}")
            raise e

    # @pytest.mark.skip
    @pytest.mark.parametrize("test_info", case_success)
    def test_success(self, test_info, login):
        createxs = XianSuo(login)
        createxs.get()
        time.sleep(3)
        createxs.click_xinjianxiansuo()
        time.sleep(3)
        createxs.create_xiansuo(test_info)
        time.sleep(3)
        createxs.click_commite()
        time.sleep(3)
        actual_result = createxs.create_success()
        try:
            assert test_info["expected"] == actual_result
            print("测试用例通过！")
        except AssertionError as e:
            print(f"测试用例不同：{e}")
            raise e




