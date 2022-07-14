import logging
import time


import yaml

import random
import string
from autotest_api.api_service.services import Services

from autotest_api.base_page.base_api import BaseApi

class Web_api(BaseApi):



    def webapi_data(self):  # 读取围栏参数的yaml文件
        with open('../config/webapi_data.yaml', 'r',encoding='utf-8') as f:
            webapi_data = yaml.safe_load(f)

            return webapi_data

    def geocode(self,data:dict):#地理编码接口

        host = Services().public_data()["params"]["webapi_host"]

        url = f"{host}/geocode/v1/geo"

        ir = BaseApi()

        r = ir.run_method(url=url,data=data, method='get')


        return r

    def regeocode(self, data: dict):  # 地理编码接口

        host = Services().public_data()["params"]["webapi_host"]

        url = f"{host}/geocode/v1/regeo"

        ir = BaseApi()

        r = ir.run_method(url=url, data=data, method='get')


        return r
    def place_text(self, data: dict):  # 关键字搜索接口

        host = Services().public_data()["params"]["webapi_host"]

        url = f"{host}/place/text"

        ir = BaseApi()

        r = ir.run_method(url=url, data=data, method='get')


        return r
    def place_around(self, data: dict):  # 周边搜索接口

        host = Services().public_data()["params"]["webapi_host"]

        url = f"{host}/place/around"

        ir = BaseApi()

        r = ir.run_method(url=url, data=data, method='get')


        return r
    def place_polygon(self, data: dict):  # 多边形搜索接口

        host = Services().public_data()["params"]["webapi_host"]

        url = f"{host}/place/polygon"

        ir = BaseApi()

        r = ir.run_method(url=url, data=data, method='get')


        return r
    def driving(self, data: dict):  # 驾车路径规划

        host = Services().public_data()["params"]["webapi_host"]

        url = f"{host}/direction/driving"

        ir = BaseApi()

        r = ir.run_method(url=url, data=data, method='get')


        return r

    def driving_batch(self, data: dict):  # 批量驾车路径规划接口

        host = Services().public_data()["params"]["webapi_host"]

        url = f"{host}/direction/driving/batch"

        ir = BaseApi()

        r = ir.run_method(url=url, data=data, method='get')


        return r
    def grasproad_track (self):  # 轨迹纠偏接口
        key = Services().public_data()["params"]["key"]

        host = Services().public_data()["params"]["webapi_host"]

        url = f"{host}/grasproad/v1/track?key={key}"
        playload=[]
        for i in range(len(Web_api().webapi_data()["grasproad_track"])):
            playload.append(Web_api().webapi_data()["grasproad_track"][i])


        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')


        return r,playload

    def pickupSpot_query (self,data:dict):  # 推荐上车点接口


        host = Services().public_data()["params"]["webapi_host"]

        url = f"{host}/pickupSpot/query"

        ir = BaseApi()

        r = ir.run_method(url=url, data=data, method='get')


        return r
    def pickupSpot_callback (self,data:dict):  # 推荐上车点接口


        host = Services().public_data()["params"]["webapi_host"]

        url = f"{host}/pickupSpot/callback"

        ir = BaseApi()

        r = ir.run_method(url=url, data=data, method='get')


        return r




if __name__ == '__main__':
    a = Web_api()
    a.geocode()
    #a.grasproad_track()