import json
import numbers

import requests
import yaml
import pytest

from API_test.base_page import BaseApi


class Track(BaseApi):

    def creat_track(self):
        url = "http://test-trapi.langgemap/v1/track/trace/add?key=e97f13deefe44387aefce3b20885328b"
        playload = {"sid":"10279","tid":10300294,"trname":"测试上传轨迹20个"}

        # r = requests.post(url=url, json=data, headers=headers)
        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')


       # print(type(r))
        #print(r)

        return r

