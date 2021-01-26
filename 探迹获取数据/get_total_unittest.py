# -*- coding: UTF-8 -*-
# @time     : 2020-12-08 19:56
# @Auther   : Aaron
# @File     : get_total_unittest.py

import ddt, time,random
import unittest
from rw_excel import RW_Excel
from get_zzzs_total import Request


@ddt.ddt
class TestGetTotal(unittest.TestCase):
    filename = r"F:\工作\竞品测试\各省招投标.xlsx"
    sheetname = "ztb"
    do_excel = RW_Excel(filename, sheetname)
    testcases = do_excel.read_data()
    print(testcases)

    @classmethod
    def setUpClass(cls):
        cls.header_dict = {
            "cookie": "_bl_uid=qRkgFg7h3C220vjjau8Uu9jlbsnk; _ga=GA1.2.822939062.1605149792; remember_token=5be5c3fb824bcc7d6ebd69df|8cec488aeb0a5b88ca2163737bf91b8c0fbc7e57ce8d68717275c91ca82272d0649aa13e9374ca9c30c9bcc8197feaf91b0873e6ed73fa6089197fc2c4518479; Hm_lvt_d3ee3af8af62f47558a292277356e90f=1607995531,1608166815,1608608271,1609123565; Hm_lpvt_d3ee3af8af62f47558a292277356e90f=1609123565; _gid=GA1.2.1996195571.1609123565; Hm_lvt_f2ee75449fc055cc4dbceb4fe403bea3=1608616833,1608626305,1608709448,1609123571; Hm_lpvt_f2ee75449fc055cc4dbceb4fe403bea3=1609123661; doncusSessionId=eyJfZnJlc2giOmZhbHNlLCJ1c2VyX2lkIjoiNWE2NWIxZjBmYjYxNWMyNmRhNDNjODUzIn0.EsrbQw.q1xFkgZbiambCSGl4wCXaKeaZxU; accountCenterSessionId=.eJwtjU0LgkAUAP_LO3sQvypvktClXQm0wMvi232brWbgbiVF_70lOg7MMG-YiJSw3YOEuwmFkOtutBTA3dIsLgpySJFSGWtcRwlKuVIZoco2SkMAsu-miUYvPQk921_AoiZiJ27aunBteXixbRhyUyT7uh-qsnF8dxz4lS1VLRdmzrEPhZ7J9v_55wuRaDEU.EsrbYg.9fXFHbo0MahEucHCCbKhxIgLVpE",
            "referer": "https://sales.tungee.com/customer-seeking/advanced-filter/enterprise"
        }
        cls.do_request = Request()
        cls.do_request.add_header(cls.header_dict)

    @classmethod
    def tearDownClass(cls):
        cls.do_request.close()

    @ddt.data(*testcases)
    def test_get(self, one_testcase):
        s = random.randint(3, 9)
        time.sleep(s)
        # print(one_testcase)
        # 资质证书
        # form_data = {
        #     "filter": '{"must":[{"hasMobile":[{"exist":"' + str(
        #         one_testcase.hasMobile) + '"}]},{"address":[{"eq":[["' + one_testcase.address + '"]]}]},{"hasCertificate":[{"exist":"' + str(
        #         one_testcase.hasCertificate) + '"}]},{"certNameList":[{"eq":[["' + one_testcase.groups + '","' + one_testcase.zs_name + '"]]}]}]}'
        # }
        # 知识产权-商标国际分类
        # sb_data = {
        #     "filter": '{"must":[{"hasMobile":[{"exist":"'+str(one_testcase.hasMobile)+'"}]},{"address":[{"eq":[["'+one_testcase.address+'"]]}]},{"hasTrademark":[{"exist":"'+str(one_testcase.hasTrademark)+'"}]},{"tmInternationalClass":[{"in":["'+one_testcase.tmInternationalClass+'"]}]}]}'
        # }
        # 行业+资本
        # hyzb_data = {
        #     "filter": '{"must": [{"hasMobile": [{"exist": "'+str(one_testcase.hasMobile)+'"}]}, {"address": [{"eq": [['+one_testcase.address+']]}]},{"industries": [{"eq": [["'+one_testcase.industries+'"]]}]}, {"operStatus_v2": [{"eq": [["'+one_testcase.operStatus_v2+'"]]}]},{"regCapitalRmb": [{"gte": '+str(one_testcase.gte)+', "lte":  '+str(one_testcase.lte)+'}]}]}'
        # }

        # 成立日期
        # clrq_data = {
        #     "filter": '{"must":[{"foundTime":[{"gte":"2020-01-01","lte":"2020-12-15"}]},{"address":[{"eq":[['+one_testcase.address+']]}]},{"regCapitalRmb":[{"gte":'+str(one_testcase.r_gte)+',"lte":'+str(one_testcase.r_lte)+'}]},{"industries":[{"eq":[["'+one_testcase.industries+'"]]}]}]}'
        # }
        # print(clrq_data)
        # 招聘渠道、地址、人数
        # zp_data = {
        #     "filter": '{"must":[{"recruitingSource":[{"in":["'+str(one_testcase.recruitingSource)+'"]}]},{"recruitingAddress":[{"in":[["'+one_testcase.recruitingAddress+'"]]}]},{"recruitingCurrentCount":[{"gte":'+str(one_testcase.gte)+',"lte":'+str(one_testcase.lte)+'}]}]}'
        # }
        # 招聘地址、发布时间、平均薪酬
        # zpxc = {
        #     "filter": '{"must":[{"recruitingAddress":[{"in":[["'+one_testcase.recruitingAddress+'"]]}]},{"recruitingPublishedTime":[{"gte":'+str(one_testcase.pt_get)+',"lte":'+str(one_testcase.pt_let)+'}]},{"recruitingAvgWorkingSalary":[{"gte":'+str(one_testcase.ws_gte)+',"lte":'+str(one_testcase.ws_lte)+'}]}]}'
        # }
        # 各省经营异常数量
        # gsyc = {
        #     "filter": '{"must":[{"hasAnomalyList":[{"exist":"'+str(one_testcase.hasAnomalyList)+'"}]},{"isAnomaly":[{"exist":"'+str(one_testcase.isAnomaly)+'"}]},{"anomalyCreateDate":[{"gte":'+one_testcase.d_gte+',"lte":'+one_testcase.d_lte+'}]},{"address":[{"eq":[["'+one_testcase.address+'"]]}]}]}'
        # }
        # # 各省行政处罚
        # xzcf = {
        #     "filter": '{"must":[{"hasPunishment":[{"exist":"'+str(one_testcase.hasPunishment)+'"}]},{"address":[{"eq":[["'+one_testcase.address+'"]]}]},{"lastPunishmentDate":[{"gte":'+one_testcase.d_gte+',"lte":'+one_testcase.d_lte+'}]}]}'
        # }
        # ICP备案
        # gw = {
        #     "filter": '{"must":[{"hasICP":[{"exist":"'+str(one_testcase.homepage)+'"}]},{"domainExpireDate":[{"gte":'+one_testcase.d_gte+',"lte":'+one_testcase.d_lte+'}]}]}'
        # }
        # 手机号渠道为官网
        # sjgw = {
        #     "filter": '{"must": [{"mobileSourceList": [{"in": [["'+one_testcase.mobileSourceList+'"]]}]}, {"address": [{"eq": [["'+one_testcase.address+'"]]}]}]}'
        # }

        # 媒体信息：新闻、微博、微信、自媒体
        # news = {
        #     "filter": '{"must":[{"'+one_testcase.hasNews+'":[{"exist":"1"}]},{"address":[{"eq":[["'+one_testcase.address+'"]]}]}]}'
        # }

        # 有无推广 按月对比
        # tuig = {
        #     "filter": '{"must":[{"hasPrmt":[{"exist":"1"}]},{"prmtSources":[{"in":["360","百度"]}]},{"lastPrmtTime":[{"gte":'+one_testcase.d_gte+',"lte":'+one_testcase.d_lte+'}]}]}'
        # }
        # 各省招投标
        ztb = {
            "filter": '{"must":[{"hasBidding":[{"exist":"1"}]},{"address":[{"eq":[["'+one_testcase.address+'"]]}]}]}'
        }



        # print(zpxc)
        res = self.do_request.send("POST", one_testcase.url, data=ztb)
        print(res.json())

        try:
            total = res.json()["total"]
            self.do_excel.write_total(one_testcase.row, one_testcase.total_column, total)
        except AssertionError as e:
            print(res.json())
            raise e





