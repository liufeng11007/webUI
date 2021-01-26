# -*- coding: UTF-8 -*-
# @time     : 2020-12-29 16:02
# @Auther   : Aaron
# @File     : gonghai_test.py

import pytest, time

from pages.gonghai_page import Gonghai


@pytest.mark.staging
@pytest.mark.gonghai
class Test_GongHai:
    def test_dpl_operation(self, login):
        ghkh = Gonghai(login)
        ghkh.get()
        time.sleep(1)
        kh_name = ghkh.get_name()
        ghkh.search_ghkh(kh_name)
        ghkh.dpl_operation()
        time.sleep(15)
        ghkh.search_ghkh(kh_name)
        time.sleep(2)
        s_total = ghkh.ghkh_total()
        time.sleep(2)
        try:
            assert int(s_total) == 0
            print("测试用例通过！")
        except AssertionError as e:
            print(f"测试用例不同：{e}")
            raise e

    # @pytest.mark.skip
    def test_pltr(self, login):
        ghkh = Gonghai(login)
        ghkh.get()
        old_total = ghkh.ghkh_total()
        ghkh.click_qx()
        # 获取全选的数量
        qx_numb = ghkh.qx_number()
        ghkh.pltr()
        tr_tip = ghkh.get_tips()
        time.sleep(1)
        new_total = ghkh.ghkh_total()
        try:
            assert int(old_total)-int(qx_numb) == int(new_total)
            assert tr_tip == " 客户挑入成功  "
            print("测试用例通过！")
        except AssertionError as e:
            print(f"测试用例不同：{e}")
            raise e

    # @pytest.mark.skip
    def test_delet(self, login):
        ghkh = Gonghai(login)
        ghkh.get()
        old_total = ghkh.ghkh_total()
        time.sleep(2)
        ghkh.click_qx()
        # 获取全选的数量
        qx_numb = ghkh.qx_number()
        ghkh.delet_pl()
        d_tip = ghkh.get_tips()
        time.sleep(1)
        new_total = ghkh.ghkh_total()
        try:
            assert int(old_total)-int(qx_numb) == int(new_total)
            assert d_tip == " 客户删除成功  "
            print("测试用例通过！")
        except AssertionError as e:
            print(f"测试用例不同：{e}")
            raise e




