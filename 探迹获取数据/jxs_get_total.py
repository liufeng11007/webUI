# -*- coding: UTF-8 -*-
# @time     : 2020-12-09 16:10
# @Auther   : Aaron
# @File     : jxs_get_total.py

import ddt, time,json
import unittest
from rw_excel import RW_Excel
from get_zzzs_total import Request


@ddt.ddt
class TestGetTotal(unittest.TestCase):
    filename = r"F:\工作\竞品测试\各省招投标-备份.xlsx"
    sheetname = "ztb"
    do_excel = RW_Excel(filename, sheetname)
    testcases = do_excel.read_data()
    # print(testcases)
    # jxs_url = "https://baize-api.jingxiansuo.com/DataService/api/v1/company/list/multiple"
    @classmethod
    def setUpClass(cls):
        cls.header_dict ={
            "authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyVGVscGhvbmUiOiIxNTgwMjgxMTAwMyIsInJvbGVJZCI6MTk0MzQ1MTY4LCJjb21wYW55TmFtZSI6Iua1i-ivlS0tLea1i-ivlee7hOWImOmUiyIsInN5c0RhdGFOYW1lIjoi5Liq5Lq6IiwidXNlckNyZWF0ZWRhdGUiOjE1NzczNzYwMDAwMDAsImJzc09yZ05hbWUiOiLlpKflj5HmkpLml6bms5XluIjmiZPlj5Hor7QiLCJ1c2VyTmFtZSI6IuasouWTpeeahOi_lOWbnuWIsCIsInVzZXJJZCI6MTA3OTksInN5c0RhdGFJbmZvIjoi5Y-q6IO95pON5L2c6Ieq5bex5ZKM5LiL5bGe55qE5pWw5o2uIiwidmVyc2lvbiI6MTAxMDMsImNvbXBhbnlJZCI6MzYwLCJic3NPcmdJZCI6NDk0LCJyb2xlTmFtZSI6ImZkc2dzZGdzIiwiZXhwaXJlRGF0ZSI6MTg5MzA0NjY5MDAwMCwidXNlclJvbGVJZCI6MTAwNzg1LCJmcmVlIjoiZmFsc2UiLCJzeXNEYXRhSWQiOjEwMDQsInZlcnNpb25uYW1lIjoi5LyB5Lia54mIIiwidXBCc3NPcmdJZCI6NDkzLCJ1c2VybmFtZSI6IjE1ODAyODExMDAzIn0.tkyO09VSwkPtVom-YMxFMVffsYwt75SA1gmoHPjxGueayHxvF-RVAWbtG8M4rCEMhNSc-F_gdRM_DzWpAFFEYw",
        }
        cls.do_request = Request()
        cls.do_request.add_header(cls.header_dict)

    @classmethod
    def tearDownClass(cls):
        cls.do_request.close()

    @ddt.data(*testcases)
    def test_get(self, one_testcase):
        time.sleep(3)
        # print(one_testcase)
        # 资质证书参数

        # json_data = {
        #       "haveLeads": True,
        #       "pageSize": 100,
        #       "pageIndex": 1,
        #       "condition": '{\"must\":[{\"mobile\":[{\"exist\":\"'+str(one_testcase.hasMobile)+'\"}]},{\"businessLocation\":[{\"in\":[\"'+one_testcase.address+'\"]}]},{\"certification\":[{\"exist\":\"'+str(one_testcase.hasCertificate)+'\"}]},{\"certificationName\":[{\"eq\":[\"'+one_testcase.zs_name+'\"]}]}]}'
        # }

        # 知识产权-专利国际分类
        # data1 = {
        #     "haveLeads":True,
        #     "pageSize":100,
        #     "pageIndex":1,
        #     "condition":'{\"must\":[{\"mobile\":[{\"exist\":\"'+str(one_testcase.hasMobile)+'\"}]},{\"businessLocation\":[{\"in\":[\"'+one_testcase.address+'\"]}]},{\"brand\":[{\"exist\":\"'+str(one_testcase.hasTrademark)+'\"}]},{\"brandCategory\":[{\"eq\":[\"'+str(one_testcase.fenClass)+'\"]}]}]}'
        # }
        # 行业、注册资本
        # data2 = {
        #     "haveLeads": True, "pageSize": 100, "pageIndex": 1,
        #     "condition": '{\"must\":[{\"mobile\":[{\"exist\":\"'+str(one_testcase.hasMobile)+'\"}]},{\"businessLocation\":[{\"in\":[\"'+one_testcase.address+'\"]}]},{\"companyIndustry\":[{\"eq\":[\"'+one_testcase.companyIndustry+'\"]}]},{\"operateState\":[{\"eq\":[\"'+one_testcase.operateState1+'\",\"'+one_testcase.operateState2+'\"]}]},{\"registCapital\":[{\"gte\":'+str(one_testcase.gte)+',\"lte\":'+str(one_testcase.lte)+'}]}]}'
        #          }
        # print(data2)

        # 成立日期注册资本
        # data3 = {
        #   "haveLeads": True,
        #   "pageSize": 100,
        #   "pageIndex": 1,
        #   "condition": '{\"must\":[{\"foundTime\":[{\"gte\":\"2020-01-01\",\"lte\":\"2020-12-15\"}]},{\"businessLocation\":[{\"in\":[\"'+one_testcase.address+'\"]}]},{\"registCapital\":[{\"gte\":'+str(one_testcase.r_gte)+',\"lte\":'+str(one_testcase.r_lte)+'}]},{\"companyIndustry\":[{\"eq\":[\"'+one_testcase.industries+'\"]}]}]}'
        # }
        # 招聘渠道、地址、人数
#         zp_data = {
#           "haveLeads": True,
#           "pageSize": 100,
#           "pageIndex": 1,
#           "condition": '{\"must\":[{\"recruitChannel\":[{\"eq\":[\"'+one_testcase.recruitChannel+'\"]}]},{\"recruitAddr\":[{\"in\":[\"'+one_testcase.recruitAddr+'\"]}]},{\"recruitNumbers\":[{\"gte\":'+str(one_testcase.gte)+',\"lte\":'+str(one_testcase.lte)+'}]}]}'
# }
#       # 招聘地址、发布时间、平均薪酬
#         t_data = one_testcase.d_gte
#         a = t_data.split('"')[1]
#         b = one_testcase.d_lte.split('"')[1]

        # zpxc_data = {
        #   "haveLeads": True,
        #   "pageSize": 100,
        #   "pageIndex": 1,
        #   "condition": '{\"must\":[{\"recruitAddr\":[{\"in\":[\"'+one_testcase.recruitAddr+'\"]}]},{\"recruitInfoReleaseDate\":[{\"gte\":\"'+a+'\",\"lte\":\"'+b+'\"}]},{\"averageSalary\":[{\"gte\":'+str(one_testcase.ws_gte)+',\"lte\":'+str(one_testcase.ws_lte)+'}]}]}'
        # }

        # 各省经营异常数量
        # gsyc = {
        #   "haveLeads": True,
        #   "pageSize": 100,
        #   "pageIndex": 1,
        #   "condition": '{\"must\":[{\"haveAbnormalOperation\":[{\"exist\":\"'+str(one_testcase.hasAnomalyList)+'\"}]},{\"haveAbnormalOperationPresent\":[{\"exist\":\"'+str(one_testcase.isAnomaly)+'\"}]},{\"moveInAbnormalOperationTime\":[{\"gte\":\"'+a+'\",\"lte\":\"'+b+'\"}]},{\"businessLocation\":[{\"in\":[\"'+one_testcase.address+'\"]}]}]}'
        # }
        # 各省行政处罚
        # xzcf = {
        #   "haveLeads": True,
        #   "pageSize": 100,
        #   "pageIndex": 1,
        #   "condition": '{\"must\":[{\"haveAdministrativePenalties\":[{\"exist\":\"'+str(one_testcase.hasPunishment)+'\"}]},{\"administrativePenaltiesTime\":[{\"gte\":\"'+a+'\",\"lte\":\"'+b+'\"}]},{\"businessLocation\":[{\"in\":[\"'+one_testcase.address+'\"]}]}]}'
        # }
        # ICP备案网站
        # gw = {
        #   "haveLeads": True,
        #   "pageSize": 100,
        #   "pageIndex": 1,
        #   "condition": '{\"must\":[{\"haveRecordWebsite\":[{\"exist\":\"'+str(one_testcase.homepage)+'\"}]},{\"domainNameEndTime\":[{\"gte\":\"'+a+'\",\"lte\":\"'+b+'\"}]}]}'
        # }
        # 手机号渠道为官网
        # sjgw = {
        #   "haveLeads": True,
        #   "pageSize": 100,
        #   "pageIndex": 1,
        #   "condition": '{\"must\":[{\"mobileComeFrom\":[{\"in\":[\"'+one_testcase.mobileSourceList+'\"]}]},{\"businessLocation\":[{\"in\":[\"'+one_testcase.address+'\"]}]}]}'
        # }
        # 媒体信息：新闻、微博、微信、自媒体
        # news = {
        #   "haveLeads": True,
        #   "pageSize": 100,
        #   "pageIndex": 1,
        #   "condition": '{\"must\":[{\"'+one_testcase.hasNews+'\":[{\"exist\":\"1\"}]},{\"businessLocation\":[{\"in\":[\"'+one_testcase.address+'\"]}]}]}'
        # }

        # 有无推广
        # tuig = {
        #     "haveLeads": True,
        #     "pageSize": 100,
        #     "pageIndex": 1,
        #     "condition": '{\"must\":[{\"havePromotion\":[{\"exist\":\"1\"}]},{\"promotionChannel\":[{\"eq\":[\"百度\",\"360\"]}]},{\"lastPromotionTime\":[{\"gte\":\"'+a+'\",\"lte\":\"'+b+'\"}]}]}'
        # }
        # 各省招投标
        ztb = {
          "haveLeads": True,
          "pageSize": 100,
          "pageIndex": 1,
          "condition": '{\"must\":[{\"haveTenderAndBid\":[{\"exist\":\"1\"}]},{\"businessLocation\":[{\"in\":[\"'+one_testcase.address+'\"]}]}]}'
        }

        # print(zpxc_data)
        # print(json.dumps(zpxc_data))

        res = self.do_request.send("POST", one_testcase.url, json=ztb)
        print(res.json())

        try:
            total = res.json()["data"]["totalRecords"]
            self.do_excel.write_total(one_testcase.row, one_testcase.jxs_column, total)
        except AssertionError as e:
            print(res.json())
            raise e
