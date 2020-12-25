# -*- coding: UTF-8 -*-
# @time     : 2020-11-24 16:55
# @Auther   : Aaron
# @File     : xiansuo_data.py

import time,random

# print(time.strftime("%Y/%m/%d %H:%m:%S"))
time = time.strftime("%Y/%m/%d %H:%m:%S")
number = random.randint(1,100)
# print(number)

# 必填项测试，最后一条用例是查重测试
case_required = [
    {
         "name": "",
         "company_name": "",
         "jyfw": "",
         "phone": "",
         "call": "",
         "address": "",
         "bz": "",
         "zdhwb": "",
         "zmhwb": "",
         "zsz": "",
         "zzs": "",
         "zrq": "",
         "ztime": "",
         "zrqsj": "",
         "zdh": "",
         "zemail": "",
         "zaaddr": "",
         "expected": " 请输入姓名！  "
         },
    {
         "name": "WebUI自动创建线索测试0001",
         "company_name": "",
         "jyfw": "",
         "phone": "",
         "call": "",
         "address": "",
         "bz": "",
         "zdhwb": "",
         "zmhwb": "",
         "zsz": "",
         "zzs": "",
         "zrq": "",
         "ztime": "",
         "zrqsj": "",
         "zdh": "",
         "zemail": "",
         "zaaddr": "",
         "expected": " 请输入公司名称！  "
         },
    {
  "name": "WebUI自动创建线索测试0001",
  "company_name": "WebUI自动创建线索测试0001",
  "jyfw": "",
  "phone": "",
  "call": "",
  "address": "",
  "bz": "",
  "zdhwb": "",
  "zmhwb": "",
  "zsz": "",
  "zzs": "",
  "zrq": "",
  "ztime": "",
  "zrqsj": "",
  "zdh": "",
  "zemail": "",
  "zaaddr": "",
  "expected": " 请输入经营范围！  "
 },
    {
  "name": "WebUI自动创建线索测试0001",
  "company_name": "WebUI自动创建线索测试0001",
  "jyfw": "fasdgsfgsfd\n"
          "adfsasdfasdf43241234\n"
          "43241324321413241\n"
          "芙兰达手机放拉丝机都发了第三法师打发点是发大水",
  "phone": "",
  "call": "",
  "address": "",
  "bz": "",
  "zdhwb": "",
  "zmhwb": "",
  "zsz": "",
  "zzs": "",
  "zrq": "",
  "ztime": "",
  "zrqsj": "",
  "zdh": "",
  "zemail": "",
  "zaaddr": "",
  "expected": " 请输入手机！  "
 },
    {
  "name": "WebUI自动创建线索测试0001",
  "company_name": "WebUI自动创建线索测试0001",
  "jyfw": "fasdgsfgsfd\n"
          "adfsasdfasdf43241234\n"
          "43241324321413241\n"
          "芙兰达手机放拉丝机都发了第三法师打发点是发大水",
  "phone": "5432523452345",
  "call": "",
  "address": "",
  "bz": "",
  "zdhwb": "",
  "zmhwb": "",
  "zsz": "",
  "zzs": "",
  "zrq": "",
  "ztime": "",
  "zrqsj": "",
  "zdh": "",
  "zemail": "",
  "zaaddr": "",
  "expected": " 请输入座机！  "
 },
    {
  "name": "WebUI自动创建线索测试0001",
  "company_name": "WebUI自动创建线索测试0001",
  "jyfw": "fasdgsfgsfd\n"
          "adfsasdfasdf43241234\n"
          "43241324321413241\n"
          "芙兰达手机放拉丝机都发了第三法师打发点是发大水",
  "phone": "5432523452345",
  "call": "7777777777",
  "address": "",
  "bz": "",
  "zdhwb": "",
  "zmhwb": "",
  "zsz": "",
  "zzs": "",
  "zrq": "",
  "ztime": "",
  "zrqsj": "",
  "zdh": "",
  "zemail": "",
  "zaaddr": "",
  "expected": " 请输入详细地址！  "
 },
    {
  "name": "WebUI自动创建线索测试0001",
  "company_name": "WebUI自动创建线索测试0001",
  "jyfw": "fasdgsfgsfd\n"
          "adfsasdfasdf43241234\n"
          "43241324321413241\n"
          "芙兰达手机放拉丝机都发了第三法师打发点是发大水",
  "phone": "5432523452345",
  "call": "777777777",
  "address": "是梵蒂冈是大法官是公司公司",
  "bz": "",
  "zdhwb": "",
  "zmhwb": "",
  "zsz": "",
  "zzs": "",
  "zrq": "",
  "ztime": "",
  "zrqsj": "",
  "zdh": "",
  "zemail": "",
  "zaaddr": "",
  "expected": " 请输入备注！  "
 },
    {
  "name": "WebUI自动创建线索测试0001",
  "company_name": "WebUI自动创建线索测试0001",
  "jyfw": "fasdgsfgsfd\n"
          "adfsasdfasdf43241234\n"
          "43241324321413241\n"
          "芙兰达手机放拉丝机都发了第三法师打发点是发大水",
  "phone": "5432523452345",
  "call": "777777777",
  "address": "是梵蒂冈是大法官是公司公司",
  "bz": "发的给对方是个是否都更是的啊撒旦法师打发发生大法师的发生大法师大法师打发"
        "是点发发是大法师的法师法师发法师的法师法",
  "zdhwb": "",
  "zmhwb": "",
  "zsz": "",
  "zzs": "",
  "zrq": "",
  "ztime": "",
  "zrqsj": "",
  "zdh": "",
  "zemail": "",
  "zaaddr": "",
  "expected": " 请输入自定义单行文本！  "
 },
    {
  "name": "WebUI自动创建线索测试0001",
  "company_name": "WebUI自动创建线索测试0001",
  "jyfw": "fasdgsfgsfd\n"
          "adfsasdfasdf43241234\n"
          "43241324321413241\n"
          "芙兰达手机放拉丝机都发了第三法师打发点是发大水",
  "phone": "5432523452345",
  "call": "777777777",
  "address": "是梵蒂冈是大法官是公司公司",
  "bz": "发的给对方是个是否都更是的啊撒旦法师打发发生大法师的发生大法师大法师打发"
        "是点发发是大法师的法师法师发法师的法师法",
  "zdhwb": "告诉对方感受到分公司的发个",
  "zmhwb": "",
  "zsz": "",
  "zzs": "",
  "zrq": "",
  "ztime": "",
  "zrqsj": "",
  "zdh": "",
  "zemail": "",
  "zaaddr": "",
  "expected": " 请输入自定义多行文本！  "
 },
    {
  "name": "WebUI自动创建线索测试0001",
  "company_name": "WebUI自动创建线索测试0001",
  "jyfw": "fasdgsfgsfd\n"
          "adfsasdfasdf43241234\n"
          "43241324321413241\n"
          "芙兰达手机放拉丝机都发了第三法师打发点是发大水",
  "phone": "5432523452345",
  "call": "777777777",
  "address": "是梵蒂冈是大法官是公司公司",
  "bz": "发的给对方是个是否都更是的啊撒旦法师打发发生大法师的发生大法师大法师打发"
        "是点发发是大法师的法师法师发法师的法师法",
  "zdhwb": "告诉对方感受到分公司的发个",
  "zmhwb": "否的国防生的故事梵蒂冈撒发顺丰\n"
           "312423412342134123413241234123412342134\n\n\n\n"
           "fsadfasfasfasfasfadsfasdfasdfasdfasdf",
  "zsz": "",
  "zzs": "",
  "zrq": "",
  "ztime": "",
  "zrqsj": "",
  "zdh": "",
  "zemail": "",
  "zaaddr": "",
  "expected": " 请输入自定义数字！  "
 },
    {
  "name": "WebUI自动创建线索测试0001",
  "company_name": "WebUI自动创建线索测试0001",
  "jyfw": "fasdgsfgsfd\n"
          "adfsasdfasdf43241234\n"
          "43241324321413241\n"
          "芙兰达手机放拉丝机都发了第三法师打发点是发大水",
  "phone": "5432523452345",
  "call": "777777777",
  "address": "是梵蒂冈是大法官是公司公司",
  "bz": "发的给对方是个是否都更是的啊撒旦法师打发发生大法师的发生大法师大法师打发"
        "是点发发是大法师的法师法师发法师的法师法",
  "zdhwb": "告诉对方感受到分公司的发个",
  "zmhwb": "否的国防生的故事梵蒂冈撒发顺丰\n"
           "312423412342134123413241234123412342134\n\n\n\n"
           "fsadfasfasfasfasfadsfasdfasdfasdfasdf",
  "zsz": "654654654.321321",
  "zzs": "",
  "zrq": "",
  "ztime": "",
  "zrqsj": "",
  "zdh": "",
  "zemail": "",
  "zaaddr": "",
  "expected": " 请输入自定义整数！  "
 },
    {
  "name": "WebUI自动创建线索测试0001",
  "company_name": "WebUI自动创建线索测试0001",
  "jyfw": "fasdgsfgsfd\n"
          "adfsasdfasdf43241234\n"
          "43241324321413241\n"
          "芙兰达手机放拉丝机都发了第三法师打发点是发大水",
  "phone": "5432523452345",
  "call": "777777777",
  "address": "是梵蒂冈是大法官是公司公司",
  "bz": "发的给对方是个是否都更是的啊撒旦法师打发发生大法师的发生大法师大法师打发"
        "是点发发是大法师的法师法师发法师的法师法",
  "zdhwb": "告诉对方感受到分公司的发个",
  "zmhwb": "否的国防生的故事梵蒂冈撒发顺丰\n"
           "312423412342134123413241234123412342134\n\n\n\n"
           "fsadfasfasfasfasfadsfasdfasdfasdfasdf",
  "zsz": "654654654.321321",
  "zzs": "35345345345332",
  "zrq": "",
  "ztime": "",
  "zrqsj": "",
  "zdh": "",
  "zemail": "",
  "zaaddr": "",
  "expected": " 请输入自定义日期！  "
 },
    {
  "name": "WebUI自动创建线索测试0001",
  "company_name": "WebUI自动创建线索测试0001",
  "jyfw": "fasdgsfgsfd\n"
          "adfsasdfasdf43241234\n"
          "43241324321413241\n"
          "芙兰达手机放拉丝机都发了第三法师打发点是发大水",
  "phone": "5432523452345",
  "call": "777777777",
  "address": "是梵蒂冈是大法官是公司公司",
  "bz": "发的给对方是个是否都更是的啊撒旦法师打发发生大法师的发生大法师大法师打发"
        "是点发发是大法师的法师法师发法师的法师法",
  "zdhwb": "告诉对方感受到分公司的发个",
  "zmhwb": "否的国防生的故事梵蒂冈撒发顺丰\n"
           "312423412342134123413241234123412342134\n\n\n\n"
           "fsadfasfasfasfasfadsfasdfasdfasdfasdf",
  "zsz": "654654654.321321",
  "zzs": "35345345345332",
  "zrq": "2020-11-27",
  "ztime": "",
  "zrqsj": "",
  "zdh": "",
  "zemail": "",
  "zaaddr": "",
  "expected": " 请输入自定义时间！  "
 },
    {
  "name": "WebUI自动创建线索测试0001",
  "company_name": "WebUI自动创建线索测试0001",
  "jyfw": "fasdgsfgsfd\n"
          "adfsasdfasdf43241234\n"
          "43241324321413241\n"
          "芙兰达手机放拉丝机都发了第三法师打发点是发大水",
  "phone": "5432523452345",
  "call": "777777777",
  "address": "是梵蒂冈是大法官是公司公司",
  "bz": "发的给对方是个是否都更是的啊撒旦法师打发发生大法师的发生大法师大法师打发"
        "是点发发是大法师的法师法师发法师的法师法",
  "zdhwb": "告诉对方感受到分公司的发个",
  "zmhwb": "否的国防生的故事梵蒂冈撒发顺丰\n"
           "312423412342134123413241234123412342134\n\n\n\n"
           "fsadfasfasfasfasfadsfasdfasdfasdfasdf",
  "zsz": "654654654.321321",
  "zzs": "35345345345332",
  "zrq": "2020-11-27",
  "ztime": "08:00",
  "zrqsj": "",
  "zdh": "",
  "zemail": "",
  "zaaddr": "",
  "expected": " 请输入自定义日期+时间！  "
 },
    {
  "name": "WebUI自动创建线索测试0001",
  "company_name": "WebUI自动创建线索测试0001",
  "jyfw": "fasdgsfgsfd\n"
          "adfsasdfasdf43241234\n"
          "43241324321413241\n"
          "芙兰达手机放拉丝机都发了第三法师打发点是发大水",
  "phone": "5432523452345",
  "call": "777777777",
  "address": "是梵蒂冈是大法官是公司公司",
  "bz": "发的给对方是个是否都更是的啊撒旦法师打发发生大法师的发生大法师大法师打发"
        "是点发发是大法师的法师法师发法师的法师法",
  "zdhwb": "告诉对方感受到分公司的发个",
  "zmhwb": "否的国防生的故事梵蒂冈撒发顺丰\n"
           "312423412342134123413241234123412342134\n\n\n\n"
           "fsadfasfasfasfasfadsfasdfasdfasdfasdf",
  "zsz": "654654654.321321",
  "zzs": "35345345345332",
  "zrq": "2020-11-27",
  "ztime": "08:00",
  "zrqsj": "2020-11-28 13:53",
  "zdh": "",
  "zemail": "",
  "zaaddr": "",
  "expected": " 请输入自定义电话！  "
 },
    {
  "name": "WebUI自动创建线索测试0001",
  "company_name": "WebUI自动创建线索测试0001",
  "jyfw": "fasdgsfgsfd\n"
          "adfsasdfasdf43241234\n"
          "43241324321413241\n"
          "芙兰达手机放拉丝机都发了第三法师打发点是发大水",
  "phone": "5432523452345",
  "call": "777777777",
  "address": "是梵蒂冈是大法官是公司公司",
  "bz": "发的给对方是个是否都更是的啊撒旦法师打发发生大法师的发生大法师大法师打发"
        "是点发发是大法师的法师法师发法师的法师法",
  "zdhwb": "告诉对方感受到分公司的发个",
  "zmhwb": "否的国防生的故事梵蒂冈撒发顺丰\n"
           "312423412342134123413241234123412342134\n\n\n\n"
           "fsadfasfasfasfasfadsfasdfasdfasdfasdf",
  "zsz": "654654654.321321",
  "zzs": "35345345345332",
  "zrq": "2020-11-27",
  "ztime": "08:00",
  "zrqsj": "2020-11-28 13:53",
  "zdh": "66666666666666",
  "zemail": "",
  "zaaddr": "",
  "expected": " 请输入自定义邮箱！  "
 },
    {
  "name": "WebUI自动创建线索测试0001",
  "company_name": "WebUI自动创建线索测试0001",
  "jyfw": "fasdgsfgsfd\n"
          "adfsasdfasdf43241234\n"
          "43241324321413241\n"
          "芙兰达手机放拉丝机都发了第三法师打发点是发大水",
  "phone": "5432523452345",
  "call": "777777777",
  "address": "是梵蒂冈是大法官是公司公司",
  "bz": "发的给对方是个是否都更是的啊撒旦法师打发发生大法师的发生大法师大法师打发"
        "是点发发是大法师的法师法师发法师的法师法",
  "zdhwb": "告诉对方感受到分公司的发个",
  "zmhwb": "否的国防生的故事梵蒂冈撒发顺丰\n"
           "312423412342134123413241234123412342134\n\n\n\n"
           "fsadfasfasfasfasfadsfasdfasdfasdfasdf",
  "zsz": "654654654.321321",
  "zzs": "35345345345332",
  "zrq": "2020-11-27",
  "ztime": "08:00",
  "zrqsj": "2020-11-28 13:53",
  "zdh": "66666666666666",
  "zemail": "23423fd",
  "zaaddr": "",
  "expected": " 自定义邮箱格式错误！  "
 },
    {
  "name": "WebUI自动创建线索测试0001",
  "company_name": "WebUI自动创建线索测试0001",
  "jyfw": "fasdgsfgsfd\n"
          "adfsasdfasdf43241234\n"
          "43241324321413241\n"
          "芙兰达手机放拉丝机都发了第三法师打发点是发大水",
  "phone": "5432523452345",
  "call": "777777777",
  "address": "是梵蒂冈是大法官是公司公司",
  "bz": "发的给对方是个是否都更是的啊撒旦法师打发发生大法师的发生大法师大法师打发"
        "是点发发是大法师的法师法师发法师的法师法",
  "zdhwb": "告诉对方感受到分公司的发个",
  "zmhwb": "否的国防生的故事梵蒂冈撒发顺丰\n"
           "312423412342134123413241234123412342134\n\n\n\n"
           "fsadfasfasfasfasfadsfasdfasdfasdfasdf",
  "zsz": "654654654.321321",
  "zzs": "35345345345332",
  "zrq": "2020-11-27",
  "ztime": "08:00",
  "zrqsj": "2020-11-28 13:53",
  "zdh": "66666666666666",
  "zemail": "23423fd@daj.da",
  "zaaddr": "",
  "expected": " 请输入自定义网址！  "
 },
    {
  "name": "自2020/11/26 14:11:20",
  "company_name": "WebUI自动创建线索测试0001+time",
  "jyfw": "fasdgsfgsfd\n"
          "adfsasdfasdf43241234\n"
          "43241324321413241\n"
          "芙兰达手机放拉丝机都发了第三法师打发点是发大水",
  "phone": "543252345234512",
  "call": "777777777",
  "address": "WebUI自动创建线索测试0001+time",
  "bz": "发的给对方是个是否都更是的啊撒旦法师打发发生大法师的发生大法师大法师打发"
        "是点发发是大法师的法师法师发法师的法师法",
  "zdhwb": "告诉对方感受到分公司的发个",
  "zmhwb": "否的国防生的故事梵蒂冈撒发顺丰\n"
           "312423412342134123413241234123412342134\n\n\n\n"
           "fsadfasfasfasfasfadsfasdfasdfasdfasdf",
  "zsz": "654654654.321321",
  "zzs": "35345345345332",
  "zrq": "2020-11-27",
  "ztime": "08:00",
  "zrqsj": "2020-11-28 13:53",
  "zdh": "66666666666666",
  "zemail": "23423fd@daj.da",
  "zaaddr": "asdfasdfasdfasdfasd",
  "expected": " 姓名,手机,详细地址,公司名称已经存在!  "
 }

]
#  线索创建成功
case_success = [
    {
  "name": "自"+time,
  "company_name": "WebUI自动创建线索测试0001"+time,
  "jyfw": "fasdgsfgsfd\n"
          "adfsasdfasdf43241234\n"
          "43241324321413241\n"
          "芙兰达手机放拉丝机都发了第三法师打发点是发大水",
  "phone": "5432523452345"+str(number),
  "call": "777777777",
  "address": "WebUI自动创建线索测试0001"+time,
  "bz": "发的给对方是个是否都更是的啊撒旦法师打发发生大法师的发生大法师大法师打发"
        "是点发发是大法师的法师法师发法师的法师法",
  "zdhwb": "告诉对方感受到分公司的发个",
  "zmhwb": "否的国防生的故事梵蒂冈撒发顺丰\n"
           "312423412342134123413241234123412342134\n\n\n\n"
           "fsadfasfasfasfasfadsfasdfasdfasdfasdf",
  "zsz": "654654654.321321",
  "zzs": "35345345345332",
  "zrq": "2020-11-27",
  "ztime": "08:00",
  "zrqsj": "2020-11-28 13:53",
  "zdh": "66666666666666",
  "zemail": "23423fd@daj.da",
  "zaaddr": "asdfasdfasdfasdfasd",
  "expected": "线索创建成功"
 }
]

