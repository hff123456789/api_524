import random

import pytest
import requests

from API_test.base_page import BaseApi




@pytest.fixture
def ceartservice():
    url = "http://test-trapi.langgemap/v1/track/service/add?key=76984a1ccba04ab8815a87d25f300fa2"

    # 改变name的值
    name = f"测试服务{random.randint(111119, 999999)}"
    playload = {"name": name, "desc": None}

    # 获取返回的值data
    ir = BaseApi()

    r = ir.run_method(url=url, json=playload, method='post')

    # print(type(r))
    sid=r["data"]["sid"]
    yield sid


