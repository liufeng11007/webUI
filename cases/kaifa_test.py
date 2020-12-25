# -*- coding: UTF-8 -*-
# @time     : 2020-11-27 14:29
# @Auther   : Aaron
# @File     : kaifa_test.py

import pytest, time

from pages.kaifa_page import KaiFa
from data.kaifa_data import case_required, case_success

@pytest.mark.staging
@pytest.mark.kaifa
class Test_KaiFa:
    # @pytest.mark.skip
    @pytest.mark.parametrize("test_info", case_required)
    def test_tips(self, test_info, login):
        create_kf = KaiFa(login)
        create_kf.get()
        time.sleep(2)
        create_kf.click_create()
        time.sleep(2)
        create_kf.create_customer(test_info)
        time.sleep(2)
        if test_info["on_create_contact"] == str(1):
            create_kf.click_create_contact()
            create_kf.create_contact(test_info)
        time.sleep(2)
        create_kf.click_commit()
        time.sleep(1)
        actual_tip = create_kf.get_tip()
        try:
            assert test_info["expected"] == actual_tip
            print("测试用例通过！")
        except AssertionError as e:
            print(f"测试用例不同：{e}")
            raise e

    # @pytest.mark.skip
    @pytest.mark.parametrize("test_info", case_success)
    def test_success(self, test_info, login):
        time.sleep(2)
        create_kf = KaiFa(login)
        create_kf.get()
        time.sleep(2)
        create_kf.click_create()
        time.sleep(2)
        create_kf.create_customer(test_info)
        time.sleep(2)
        if test_info["on_create_contact"] == str(1):
            create_kf.click_create_contact()
            time.sleep(2)
            create_kf.create_contact(test_info)
        time.sleep(2)
        create_kf.click_commit()
        time.sleep(1)
        actual_tip = create_kf.get_success_tip()
        try:
            assert test_info["expected"] == actual_tip
            print("测试用例通过！")
        except AssertionError as e:
            print(f"测试用例不同：{e}")
            raise e

    # @pytest.mark.parametrize("test_info",case_contact)
    # def test_create_contact(self,test_info, login):
    #     create_kf = KaiFa(login)
    #     create_kf.get()
    #     time.sleep(2)
    #     create_kf.click_create()
    #     time.sleep(2)
    #     create_kf.create_customer(test_info)



