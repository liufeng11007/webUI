# -*- coding: UTF-8 -*-
# @time     : 2021-01-25 14:48
# @Auther   : Aaron
# @File     : run.py
import os

import pytest

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
REPORT_PATH = os.path.join(ROOT_PATH, "output")
REPORT_FILE = os.path.join(REPORT_PATH, "demo_report.html")

if __name__ == '__main__':
    # pytest.main(["-m xiansuo", f"--html={REPORT_FILE}", "--alluredir=reports/"])
<<<<<<< HEAD
    pytest.main(["-m gonghai", "--alluredir=reports/"])
=======
    pytest.main(["-m login", "--alluredir=reports/"])
>>>>>>> 2dad2dfe681b49343aa8e9360c64088c2f7949a8


