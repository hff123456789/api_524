
import random
import logging

import allure
import pytest
import yaml

from autotest_api.api_service.services import Services
from autotest_api.api_service.track_geofence import TrackGeofence
from autotest_api.api_service.web_api import Web_api

#from autotest_api.base_page.log1 import log


@allure.feature("web服务")
class TestWebApi:

    def setup(self):
        self.web_api=Web_api()

        pass




    @allure.title("地理编码")

    def test_geocode(self,some_data):
        data=Web_api().webapi_data()["geo"]
        allure.attach("用例参数", "{0}".format(data))

        code = Web_api().webapi_data()['geo']['code']
        message = Web_api().webapi_data()['geo']['message']
        r=Web_api().geocode(data)
       # log.info("返回结果为：{}".format(r))
        with allure.step("断言"):
          assert r["code"]==code
          assert r["message"]==message

    @allure.title("逆地理编码")
    def test_regeocode(self):
        data=Web_api().webapi_data()["regeo"]
        allure.attach("用例参数", "{0}".format(data))
        code = Web_api().webapi_data()['regeo']['code']
        message = Web_api().webapi_data()['regeo']['message']

        r=Web_api().regeocode(data)
        #log.info("返回结果为：{}".format(r))
        with allure.step("断言"):
          assert r["code"] == code
          assert r["message"] == message

    @allure.title("关键字搜索")
    def test_place_text(self):
        data=Web_api().webapi_data()["place_text"]
        allure.attach("用例参数", "{0}".format(data))
        code = Web_api().webapi_data()['place_text']['code']
        message = Web_api().webapi_data()['place_text']['message']
        r=Web_api().place_text(data)
       # log.info("返回结果为：{}".format(r))
        with allure.step("断言"):
          assert r["code"] == code
          assert r["message"] == message


    @allure.title("周边搜索")
    def test_place_around(self):
        data=Web_api().webapi_data()["place_around"]
        allure.attach("用例参数", "{0}".format(data))
        code = Web_api().webapi_data()['place_around']['code']
        message = Web_api().webapi_data()['place_around']['message']
        r=Web_api().place_around(data)
       # log.info("返回结果为：{}".format(r))

        assert r["code"] ==200
        assert r["message"] == message


    @allure.title("多边形搜索")
    def test_place_polygon(self):
        data = Web_api().webapi_data()["place_polygon"]
        allure.attach("用例参数", "{0}".format(data))
        code = Web_api().webapi_data()['place_polygon']['code']
        message = Web_api().webapi_data()['place_polygon']['message']
        r = Web_api().place_polygon(data)
       # log.info("返回结果为：{}".format(r))
        with allure.step("断言"):
          assert r["code"] == code
          assert r["message"] == message

    @allure.title("驾车路径规划")
    def test_driving(self):
        data = Web_api().webapi_data()["driving"]
        allure.attach("用例参数", "{0}".format(data))
        code = Web_api().webapi_data()['driving']['code']
        message = Web_api().webapi_data()['driving']['message']
        r = Web_api().driving(data)
        #log.info("返回结果为：{}".format(r))
        with allure.step("断言"):
          assert r["code"] == code
          assert r["message"] == message

    @allure.title("批量驾车路径规划")
    def test_driving_batch(self):
        data = Web_api().webapi_data()["driving_batch"]
        allure.attach("用例参数", "{0}".format(data))
        code = Web_api().webapi_data()['driving_batch']['code']
        message = Web_api().webapi_data()['driving_batch']['message']
        r = Web_api().driving_batch(data)
        #log.info("返回结果为：{}".format(r))
        with allure.step("断言"):
          assert r["code"] == code
          assert r["message"] == message

    @allure.title("轨迹纠偏")
    def test_grasproad_track(self):

        r = Web_api().grasproad_track()

       # log.info("返回结果为：{}".format(r[0]))
        data=r[1]
        allure.attach("用例参数", "{0}".format(data))
        with allure.step("断言"):
          assert r[0]["data"] != None

    @allure.title("推荐上车点")
    def test_pickupSpot_query(self):
        data = Web_api().webapi_data()["pickupSpot_query"]
        allure.attach("用例参数", "{0}".format(data))
        code = Web_api().webapi_data()['pickupSpot_query']['code']
        message = Web_api().webapi_data()['pickupSpot_query']['message']
        r = Web_api().pickupSpot_query(data)
       # log.info("返回结果为：{}".format(r))
        with allure.step("断言"):
          assert r["code"] == code
          assert r["message"] == message

    @allure.title("推荐上车点回源")


    def test_pickupSpot_callback(self):
        data = Web_api().webapi_data()["pickupSpot_callback"]
        allure.attach("用例参数", "{0}".format(data))
        code = Web_api().webapi_data()['pickupSpot_callback']['code']
        message = Web_api().webapi_data()['pickupSpot_callback']['message']
        r = Web_api().pickupSpot_callback(data)
      #  log.info("返回结果为：{}".format(r))
        with allure.step("断言"):
          assert r["code"] == code
          assert r["message"] == message