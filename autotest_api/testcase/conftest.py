import random
from time import sleep, time

import pytest

from autotest_api.api_service.services import Services
from autotest_api.api_service.track_geofence import TrackGeofence
from autotest_api.base_page.base_api import BaseApi
#from autotest_api.base_page.log1 import log


@pytest.fixture()
def some_data():
      print("setup")
      yield some_data
      print("teardown")


@pytest.fixture(scope="function")
def services_list():
      r = Services().search_services()
      if len(r["data"]["results"]) == 0:

            Services().creat_services(playload={"name": Services().name_var()[0], "desc": "test123"})
      elif len(r["data"]["results"]) == 15:
            Services().delete_service()

      yield services_list


@pytest.fixture(scope="function")
def terminals_list():
      r = Services().search_termnial()
      if r["data"]["count"] == 0:
            Services().cearte_termianl()
            Services().cearte_termianl()

      elif r["data"]["count"] == 100000:
            Services().delete_terminal()

      yield terminals_list

@pytest.fixture(scope="function")
def geofences_list():
      r_playload = Services().geofence_data()['geofence_list']
      r = TrackGeofence().geofence_list(r_playload)
      if r["data"]["count"] == 0:
            circle_playload = Services().geofence_data()['circle']
            polygon_playload = Services().geofence_data()['polygon']
            district_playload = Services().geofence_data()['district']
            polyline_playload = Services().geofence_data()['polyline']
            TrackGeofence().add_circle(circle_playload)
            TrackGeofence().add_polygon(polygon_playload)
            TrackGeofence().add_district(district_playload)
            TrackGeofence().add_polyline(polyline_playload)

      yield geofences_list

@pytest.fixture(scope="function")
def uploadtrack_newest():
      r = Services().search_track()
      if r["errcode"] == 21504:
            Services().track_upload()
            sleep(60)
            Services().track_upload()

      yield uploadtrack_newest










# @pytest.fixture
# def ceartservice():
#     url = "http://test-trapi.langgemap/v1/track/service/add?key=76984a1ccba04ab8815a87d25f300fa2"
#
#     # 改变name的值
#     name = f"测试服务{random.randint(111119, 999999)}"
#     playload = {"name": name, "desc": None}
#
#     # 获取返回的值data
#     ir = BaseApi()
#
#     r = ir.run_method(url=url, json=playload, method='post')
#
#     # print(type(r))
#     sid = r["data"]["sid"]
#     yield sid
#
#
# @pytest.fixture(scope="session")
# def getsso_login(self):
#     url = "http://dev-sso.langgemap/langgemap-sso/account/login"
#     playload = {"userName": "Feifei.Hong1@geely.com",
#                 "password": "E8EF02C821C7C7AFC4906DF255F97D70",
#                 "serviceUrl": "sso"
#                 }
#
#     ir = BaseApi()
#
#     r = ir.run_method(url=url, json=playload, method='post')
#
#     # print(type(r))
#     token = r["data"]["token"]
#
#     return token
#
# @pytest.fixture
# def getlogin(self,getsso_login):
#     url = "http://dev-api-router.langgemap/rest?method=logcollect.manager.account.login"
#     token = getsso_login()
#     playload = {"token": token}
#     header = {"version": "1",
#               "env": "dev-k8s",
#               "appkey": "788628",
#               "nonce": "1231fsvnaj qsi1jb je12 ckjxc",
#               "Accept": "application/json, text/plain, */*",
#               "timestamp": "1650442597800",
#               "LG-TraceID": "API documents",
#               "sign": "f1bf7cfd2a8d91d90152f2853a916c9b",
#               "No-Sign": "QvSpMB3meNKw",
#               "Content-Type": "application/json;charset=UTF-8",
#               "Connection": "keep-alive"}
#
#     ir = BaseApi()
#
#     r = ir.run_method(url=url, json=playload, headers=header, method='post')
#     print(r)
#     token = r["data"]["token"]
#     return token
