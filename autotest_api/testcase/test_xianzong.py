import random

import allure
import pytest
import yaml

from autotest_api.api_service.services import Services
from autotest_api.api_service.track_geofence import TrackGeofence
from autotest_api.base_page.base_api import BaseApi
#from autotest_api.base_page.log1 import log


@allure.feature("仙踪服务")
class TestXianzong:

    def setup(self):

        self.services = Services()
        self.geofence=TrackGeofence()
        #由于下面的接口需要获取查询服务接口的ｓｉｄ，所以先判断服务列表是都有数据,且是否达到最大数量
        # r = Services().search_services()
        # if len(r["data"]["results"]) == 0:
        #
        #     Services().creat_services(playload={"name": Services().name_var()[0], "desc": "test123"})
        # elif len(r["data"]["results"]) == 15:
        #     Services().delete_service()

        # r1 = Services().search_termnial()
        # if r1["data"]["count"]==0:
        #     Services().cearte_termianl()
        # elif r1["data"]["count"]==100000:
        #     Services().delete_terminal()

        #先判断围栏列表是否又数据，没有的话先添加围栏
        # r2_playload=Services().geofence_data()['geofence_list']
        # r2=TrackGeofence().geofence_list(r2_playload)
        # if r2["data"]["count"]==0:
        #    circle_playload = Services().geofence_data()['circle']
        #    polygon_playload = Services().geofence_data()['polygon']
        #    district_playload = Services().geofence_data()['district']
        #    polyline_playload = Services().geofence_data()['polyline']
        #
        #    TrackGeofence().add_circle(circle_playload)
        #    TrackGeofence().add_polygon(polygon_playload)
        #    TrackGeofence().add_district(district_playload)
        #    TrackGeofence().add_polyline(polyline_playload)
        #先判断是否能查询到轨迹点，如果不能查询到轨迹点，那么先创建轨迹，然后上传轨迹点
        # r3=Services().search_track()
        # if r3["errcode"]== 21504:
        #
        #     Services().track_upload()
        #
        #     Services().track_upload()









    @allure.story("新增服务")
    @allure.title("新增服务参数校验")
    @pytest.mark.parametrize("playload", yaml.safe_load(open("../config/name_data.yaml", encoding="utf-8")),ids=['name为空','name包含特殊字符','正常的参数'])
    def test_creat_services(self,services_list,playload):

        errcode=playload["errcode"]
        errmsg=playload["errmsg"]
        allure.attach("用例参数", "{0}".format(playload))
        r=Services().creat_services(playload)
        #log.info("返回结果为：{}".format(r))
        assert r["errcode"]==errcode
        assert r["errmsg"]==errmsg

    @allure.feature("服务管理")
    @allure.story("新增服务")
    @allure.title("新增服务最大值校验")
    def test_services_max(self,services_list):
        r1 = Services().search_services()
        len1 = len(r1["data"]["results"])
        len2 = 15- len1

        for i in range (1, len2+1):

             r=Services().creat_services(playload={"name": Services().name_var()[0], "desc": "test123"})

        r = Services().creat_services(playload={"name": Services().name_var()[0], "desc": "test123"})
       # log.info("返回结果为：{}".format(r))
        assert r['errcode'] == 21118
        assert r['errmsg'] in "超过service最大数量15"



    @allure.feature("服务")
    @allure.story("查询服务")
    @allure.title("查询服务")
    def test_search_service(self):
       r= Services().search_services()
       #log.info("返回结果为：{}".format(r))
       assert r['errcode'] == 0



    @allure.feature("服务")
    @allure.story("删除服务")
    @allure.title("删除服务成功")
    def test_delete_service(self,services_list):

        r=Services().delete_service()
       # log.info("返回结果为：{}".format(r))
        assert r['errcode']==0

    @allure.feature("服务")
    @allure.story("修改服务服务")
    @allure.title("修改服务成功")
    def test_update_service(self,services_list):


        r=Services().update_service()
       # log.info("返回结果为：{}".format(r))

        assert r['errcode']==0



    @allure.feature("终端")
    @allure.story("创建终端")
    @allure.title("创建终端成功")
    def test_creat_termianl(self,services_list,terminals_list):
        r=Services().cearte_termianl()
       # log.info("返回结果为：{}".format(r))

        assert r["errcode"] == 0
        assert r["data"]["sid"] ==Services().search_services()["data"]["results"][0]["sid"]
        assert r["errmsg"]=="请求正常"

    @allure.feature("终端")
    @allure.story("查询终端")
    @allure.title("查询sid下所有终端")
    def test_search_TERM(self,services_list):
        r=Services().search_termnial()
       # log.info("返回结果为：{}".format(r))

        assert r["errcode"] == 0

    @allure.feature("终端")
    @allure.story("修改终端")
    @allure.title("修改终端描述")
    def test_update_TERM(self,services_list,terminals_list):
        r = Services().update_terminal()
       # log.info("返回结果为：{}".format(r))

        assert r["errcode"] == 0

    @allure.feature("终端")
    @allure.story("删除终端")
    @allure.title("删除终端")
    def test_delete_TERM(self,services_list,terminals_list):
        r = Services().delete_terminal()
        assert r["errcode"] == 0

    @allure.feature("轨迹")
    @allure.story("轨迹上传及管理")
    @allure.title("创建轨迹")
    def test_creat_track(self,services_list,terminals_list):

        r = Services().creat_track()
       # log.info("返回结果为：{}".format(r))
        assert r["errcode"] == 0

    @allure.feature("轨迹")
    @allure.story("轨迹上传及管理")
    @allure.title("轨迹点上传")
    def test_track_upload(self,services_list,terminals_list):

        r = Services().track_upload()
        #log.info("返回结果为：{}".format(r))
        assert r["errcode"] == 0

    @allure.feature("轨迹")
    @allure.story("查询轨迹点")
    @allure.title("查询轨迹点信息")
    def test_search_track(self,services_list,terminals_list):


        r = Services().search_track()
        #log.info("返回结果为：{}".format(r))
        assert r["errcode"] == 0



    @allure.feature("终端位置实时监控")
    @allure.story("查询终端位置")
    @allure.title("查询终端实时位置")
    def test_terminal_lastpoint(self,services_list,terminals_list):


        r = Services().terminal_lastpoint()
       # log.info("返回结果为：{}".format(r))
        assert r["errcode"] == 0




    @allure.feature("搜索终端")
    @allure.title("关键字查找终端")
    def test_keysearch(self,services_list,terminals_list):

        r = Services().search_KEY()
       # log.info("返回结果为：{}".format(r))

        assert r["errcode"]==0

    @allure.feature("搜索终端")
    @allure.title("多边形搜索终端")
    def test_polygonsearch(self,services_list):

        r = Services().polygonsearch()
       # log.info("返回结果为：{}".format(r))

        assert r["errcode"] == 0

    @allure.feature("搜索终端")
    @allure.title("周边搜索终端")
    def test_aroundsearch(self,services_list):

        r = Services().aroundsearch()
       # log.info("返回结果为：{}".format(r))
        assert r["errcode"] == 0

    @allure.feature("搜索终端")
    @allure.title("行政区域搜索终端")
    def test_districtsearch(self,services_list):

        r = Services().districtsearch()
      #  log.info("返回结果为：{}".format(r))
        assert r["errcode"] == 0




    #@pytest.mark.parametrize("playload", yaml.safe_load(open("../config/geofence_data.yaml", encoding="utf-8")))
    @allure.feature("围栏管理")
    @allure.title("创建圆形围栏")
    def test_creat_circlegeofence(self,services_list):

        playload=Services().geofence_data()['circle']

        errorCode=Services().geofence_data()['circle']['errorCode']
        errmsg=Services().geofence_data()['circle']['errmsg']

        r=TrackGeofence().add_circle(playload)
      #  log.info("返回结果为：{}".format(r))

        assert r['errorCode'] == errorCode
        assert r["errmsg"] == errmsg


    @allure.feature("围栏管理")
    @allure.title("创建多边形围栏")
    def test_creat_polygongeofence(self,services_list):


         playload = Services().geofence_data()['polygon']
         errorCode = Services().geofence_data()['polygon']['errorCode']
         errmsg = Services().geofence_data()['polygon']['errmsg']


         r = TrackGeofence().add_polygon(playload)
       #  log.info("返回结果为：{}".format(r))


         assert r['errorCode'] == errorCode
         assert r["errmsg"] == errmsg

    @allure.feature("围栏管理")
    @allure.title("创建线形围栏")
    def test_creat_polylinegeofence(self,services_list):


        playload = Services().geofence_data()['polyline']
        errorCode = Services().geofence_data()['polyline']['errorCode']
        errmsg = Services().geofence_data()['polyline']['errmsg']

        r = TrackGeofence().add_polyline(playload)
      #  log.info("返回结果为：{}".format(r))
        assert r['errorCode'] == errorCode
        assert r["errmsg"] == errmsg


    @allure.feature("围栏管理")
    @allure.title("创建行政区域划围栏")
    def test_creat_districtgeofence(self,services_list):

        playload = Services().geofence_data()['district']
        errorCode = Services().geofence_data()['district']['errorCode']
        errmsg = Services().geofence_data()['district']['errmsg']

        r = TrackGeofence().add_district(playload)
       # log.info("返回结果为：{}".format(r))
        assert r['errorCode'] == errorCode
        assert r["errmsg"] == errmsg

    @allure.feature("围栏管理")
    @allure.title("查询围栏")
    def test_geofence_list(self,services_list):

        playload = Services().geofence_data()['geofence_list']

        errorCode = Services().geofence_data()['geofence_list']['errorCode']
        errmsg = Services().geofence_data()['geofence_list']['errmsg']

        r = TrackGeofence().geofence_list(playload)
       # log.info("返回结果为：{}".format(r))

        assert r['errorCode'] == errorCode
        assert r["errmsg"] == errmsg
    @allure.feature("围栏管理")
    @allure.title("更新圆形围栏")
    def test_update_circle(self,services_list,geofences_list):

        playload1 = Services().geofence_data()['updatecircle']

        errorCode = Services().geofence_data()['updatecircle']['errorCode']
        errmsg = Services().geofence_data()['updatecircle']['errmsg']

        r = TrackGeofence().update_circle(playload1)
      #  log.info("返回结果为：{}".format(r))
        assert r['errorCode'] == errorCode
        assert r["errmsg"] == errmsg

    @allure.feature("围栏管理")
    @allure.title("更新多边形围栏")
    def test_update_polygon(self,services_list,geofences_list):

        playload1 = Services().geofence_data()['updatepolygon']

        errorCode = Services().geofence_data()['updatepolygon']['errorCode']
        errmsg = Services().geofence_data()['updatepolygon']['errmsg']

        r = TrackGeofence().update_polygon(playload1)
      #  log.info("返回结果为：{}".format(r))

        assert r['errorCode'] == errorCode
        assert r["errmsg"] == errmsg

    @allure.feature("围栏管理")
    @allure.title("更新线形围栏")
    def test_update_polyline(self,services_list,geofences_list):

        playload1 = Services().geofence_data()['updatepolyline']

        errorCode = Services().geofence_data()['updatepolyline']['errorCode']
        errmsg = Services().geofence_data()['updatepolyline']['errmsg']

        r = TrackGeofence().update_polyline(playload1)
      #  log.info("返回结果为：{}".format(r))
      
        assert r['errorCode'] == errorCode
        assert r["errmsg"] == errmsg
    @allure.feature("围栏管理")
    @allure.title("更新行政区域划围栏")
    def test_update_district(self,services_list,geofences_list):

        playload1= Services().geofence_data()['updatedistrict']



        errorCode = Services().geofence_data()['updatedistrict']['errorCode']
        errmsg = Services().geofence_data()['updatedistrict']['errmsg']

        r = TrackGeofence().update_district(playload1)
      #  log.info("返回结果为：{}".format(r))

        assert r['errorCode'] == errorCode
        assert r["errmsg"] == errmsg

    @allure.feature("围栏管理")
    @allure.title("删除围栏")
    def test_geofence_delete(self,services_list,geofences_list):

        playload = Services().geofence_data()['geofence_delete']

        errorCode = Services().geofence_data()['geofence_delete']['errorCode']
        errmsg = Services().geofence_data()['geofence_delete']['errmsg']

        r = TrackGeofence().geofence_delete(playload)
     #   log.info("返回结果为：{}".format(r))

        assert r['errorCode'] == errorCode
        assert r["errmsg"] == errmsg



    @allure.feature("围栏管理")
    @allure.title("增加监测对象")
    def test_geofence_bind(self,services_list,geofences_list,terminals_list):
        playload1 = Services().geofence_data()['geofence_bind']


        errorCode = Services().geofence_data()['geofence_bind']['errorCode']
        errmsg = Services().geofence_data()['geofence_bind']['errmsg']

        r = TrackGeofence().geofence_bind(playload1)
      #  log.info("返回结果为：{}".format(r))

        assert r['errorCode'] == errorCode
        assert r["errmsg"] == errmsg

    @allure.feature("围栏管理")
    @allure.title("查询监测对象")
    def test_geofence_bindlist(self,services_list,geofences_list):
        playload1 = Services().geofence_data()['geofence_bindlist']

        errorCode = Services().geofence_data()['geofence_bindlist']['errorCode']
        errmsg = Services().geofence_data()['geofence_bindlist']['errmsg']

        r = TrackGeofence().geofence_bindlist(playload1)
     #   log.info("返回结果为：{}".format(r))

        assert r['errorCode'] == errorCode
        assert r["errmsg"] == errmsg
    @allure.feature("围栏关系判断")
    @allure.title("查询监测对象与围栏关系")
    def test_geofence_terminal(self,services_list,terminals_list):

        #先保证改终端下有轨迹，且已上传点，且上传点的时间尽量是最新的


        Services().track_upload()

        data=Services().geofence_data()["geofence_terminal"]

        errorCode = Services().geofence_data()['geofence_terminal']['errorCode']
        errmsg = Services().geofence_data()['geofence_terminal']['errmsg']

        r = TrackGeofence().geofence_terminal(data)
      #  log.info("返回结果为：{}".format(r))

        assert r["errcode"] == errorCode
        assert r["errmsg"] == errmsg


    @allure.feature("围栏管理")
    @allure.title("删除监测对象")
    def test_geofence_unbind(self,services_list,geofences_list,terminals_list):
        playload1 = Services().geofence_data()['geofence_unbind']

        errorCode = Services().geofence_data()['geofence_unbind']['errorCode']
        errmsg = Services().geofence_data()['geofence_unbind']['errmsg']

        r = TrackGeofence().geofence_unbind(playload1)
      #  log.info("返回结果为：{}".format(r))

        assert r['errorCode'] == errorCode
        assert r["errmsg"] == errmsg



    @allure.feature("围栏关系判断")
    @allure.title("查询指定坐标与围栏关系")
    def test_geofence_location(self,services_list):



        data = Services().geofence_data()["geofence_location"]

        errorCode = Services().geofence_data()['geofence_location']['errorCode']
        errmsg = Services().geofence_data()['geofence_location']['errmsg']

        r = TrackGeofence().geofence_location(data)
     #   log.info("返回结果为：{}".format(r))

        assert r["errcode"] == errorCode
        assert r["errmsg"] == errmsg

    @allure.feature("轨迹行为分析")
    @allure.title("驾驶行为分析")
    def test_drivingbehavior(self,services_list,terminals_list,uploadtrack_newest):



        data = Services().geofence_data()["drivingbehavior"]

        errorCode = Services().geofence_data()['drivingbehavior']['errorCode']
        errmsg = Services().geofence_data()['drivingbehavior']['errmsg']

        r = TrackGeofence().drivingbehavior(data)
      #  log.info("返回结果为：{}".format(r))

        assert r["errcode"] == errorCode
        assert r["errmsg"] == errmsg

    @allure.feature("轨迹行为分析")
    @allure.title("停留点分析")
    def test_staypoint(self,services_list,terminals_list,uploadtrack_newest):

        data = Services().geofence_data()["staypoint"]

        errorCode = Services().geofence_data()['staypoint']['errorCode']
        errmsg = Services().geofence_data()['staypoint']['errmsg']

        r = TrackGeofence().staypoint(data)
     #   log.info("返回结果为：{}".format(r))

        assert r["errcode"] == errorCode
        assert r["errmsg"] == errmsg

    @allure.feature("轨迹重合度分析")
    @allure.title("两个相同轨迹点的轨迹")
    def test_track_match(self,services_list,terminals_list,uploadtrack_newest):
        r0=Services().search_track()
        if r0["data"]["counts"]==1:
            Services().track_upload()

        errorCode = Services().geofence_data()['track_match']['errorCode']
        errmsg = Services().geofence_data()['track_match']['errmsg']

        r = TrackGeofence().track_match()
      #  log.info("返回结果为：{}".format(r))

        assert r["errcode"] == errorCode
        assert r["errmsg"] == errmsg



    #校验一个围栏绑定10000个终端
    # def test_bind_terminal(self):
    #     for i in range(1,10000):
    #         TrackGeofence().geofence_bind()
    #         print(i)




