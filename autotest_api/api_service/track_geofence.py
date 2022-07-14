
import yaml
from functools import reduce


import random
import string

from autotest_api.api_service.services import Services
from autotest_api.base_page.base_api import BaseApi


class TrackGeofence(BaseApi):



        def add_circle(self,playload:dict):           #添加圆形围栏接口
             key =Services().public_data()["params"]["key"]
             host =Services().public_data()["params"]["host"]
             url = f"{host}/v1/track/geofence/add/circle?key={key}"

             sid= playload.get("sid")
             if "#sid#"== sid:

                 sid = Services().search_services()["data"]["results"][0]["sid"]

             playload['sid'] = sid
             name = playload.get("name")
             if "#name#" == name:
                 name = f"圆形围栏{random.randint(111119, 999999)}"
             playload['name'] = name

             ir = BaseApi()

             r = ir.run_method(url=url, json=playload, method='post')

             return r

        def add_polygon(self,playload:dict):       #添加多边形围栏接口
             key =Services().public_data()["params"]["key"]
             host =Services().public_data()["params"]["host"]
             url = f"{host}/v1/track/geofence/add/polygon?key={key}"

             sid= playload.get("sid")
             if "#sid#"== sid:

                 sid = Services().search_services()["data"]["results"][0]["sid"]

             playload['sid'] = sid
             name = playload.get("name")
             if "#name#" == name:
                 name = f"多边形围栏{random.randint(111119, 999999)}"
             playload['name'] = name

             ir = BaseApi()

             r = ir.run_method(url=url, json=playload, method='post')

             return r

        def add_polyline(self,playload:dict):       #添加线形围栏接口
             key =Services().public_data()["params"]["key"]
             host =Services().public_data()["params"]["host"]
             url = f"{host}/v1/track/geofence/add/polyline?key={key}"

             sid= playload.get("sid")
             if "#sid#"== sid:

                 sid = Services().search_services()["data"]["results"][0]["sid"]

             playload['sid'] = sid
             name = playload.get("name")
             if "#name#" == name:
                 name = f"线形围栏{random.randint(111119, 999999)}"
             playload['name'] = name

             ir = BaseApi()

             r = ir.run_method(url=url, json=playload, method='post')

             return r

        def add_district(self, playload: dict):  #添加行政区域划围栏接口
            key = Services().public_data()["params"]["key"]
            host = Services().public_data()["params"]["host"]
            url = f"{host}/v1/track/geofence/add/district?key={key}"

            sid = playload.get("sid")
            if "#sid#" == sid:
                sid = Services().search_services()["data"]["results"][0]["sid"]
            playload['sid'] = sid

            name = playload.get("name")
            if "#name#" == name:
                name = f"行政区域划围栏{random.randint(111119, 999999)}"
            playload['name'] = name

            ir = BaseApi()

            r = ir.run_method(url=url, json=playload, method='post')

            return r

        def update_circle(self,playload1:dict):    #更新圆形围栏接口
             key =Services().public_data()["params"]["key"]
             host =Services().public_data()["params"]["host"]
             url = f"{host}/v1/track/geofence/update/circle?key={key}"

             # 将sid,gfid,name封装成变量写入yaml文件 ,然后改变sid,gfid,name的值
             sid= playload1.get("sid")
             if "#sid#"== sid:

                 sid = Services().search_services()["data"]["results"][0]["sid"]

             playload1['sid'] = sid
             gfid = playload1.get("gfid")
             if "#gfid#" == gfid:
                 playload = Services().geofence_data()['geofence_list']
                 gfid = self.geofence_list(playload)["data"]["results"][0]["gfid"]

             playload1['gfid'] = gfid
             name = playload1.get("name")
             if "#name#" == name:
                 name = f"圆形围栏1{random.randint(111119, 999999)}"
             playload1['name'] = name

             ir = BaseApi()

             r = ir.run_method(url=url, json=playload1, method='post')

             return r

        def update_polygon(self,playload1:dict):     #更新多边形围栏接口
             key =Services().public_data()["params"]["key"]
             host =Services().public_data()["params"]["host"]
             url = f"{host}/v1/track/geofence/update/polygon?key={key}"

             # 将sid,gfid,name封装成变量写入yaml文件 ,然后改变sid,gfid,name的值
             sid= playload1.get("sid")
             if "#sid#"== sid:

                 sid = Services().search_services()["data"]["results"][0]["sid"]

             playload1['sid'] = sid

             gfid = playload1.get("gfid")
             if "#gfid#" == gfid:
                 playload = Services().geofence_data()['geofence_list']
                 gfid = self.geofence_list(playload)["data"]["results"][0]["gfid"]


             playload1['gfid'] = gfid

             name = playload1.get("name")
             if "#name#" == name:
                 name = f"更新多变形围栏{random.randint(111119, 999999)}"
             playload1['name'] = name

             ir = BaseApi()

             r = ir.run_method(url=url, json=playload1, method='post')

             return r

        def update_polyline(self, playload1: dict):   #更新线形围栏接口
            key = Services().public_data()["params"]["key"]
            host = Services().public_data()["params"]["host"]
            url = f"{host}/v1/track/geofence/update/polyline?key={key}"

            # 将sid,gfid,name封装成变量写入yaml文件 ,然后改变sid,gfid,name的值
            sid = playload1.get("sid")
            if "#sid#" == sid:
                sid = Services().search_services()["data"]["results"][0]["sid"]

            playload1['sid'] = sid
            gfid = playload1.get("gfid")
            if "#gfid#" == gfid:
                playload = Services().geofence_data()['geofence_list']
                gfid = self.geofence_list(playload)["data"]["results"][0]["gfid"]
            playload1['gfid'] = gfid

            name = playload1.get("name")
            if "#name#" == name:
                name = f"更新线形围栏{random.randint(111119, 999999)}"
            playload1['name'] = name

            ir = BaseApi()

            r = ir.run_method(url=url, json=playload1, method='post')

            return r

        def update_district(self, playload1: dict):    #更新行政区域划围栏接口
            key = Services().public_data()["params"]["key"]
            host = Services().public_data()["params"]["host"]
            url = f"{host}/v1/track/geofence/update/district?key={key}"

            # 将sid,gfid,name封装成变量写入yaml文件 ,然后改变sid,gfid,name的值
            name = playload1.get("name")
            if "#name#" == name:
                name = f"更新行政划围栏{random.randint(111119, 999999)}"
            playload1['name'] = name

            sid = playload1.get("sid")
            if "#sid#" == sid:
                sid = Services().search_services()["data"]["results"][0]["sid"]

            playload1['sid'] = sid
            gfid = playload1.get("gfid")
            if "#gfid#" == gfid:

                playload = Services().geofence_data()['geofence_list']
                gfid = self.geofence_list(playload)["data"]["results"][0]["gfid"]
            playload1['gfid'] = gfid





            ir = BaseApi()

            r = ir.run_method(url=url, json=playload1, method='post')

            return r

        def geofence_list(self, playload: dict):     #查询围栏接口
            key = Services().public_data()["params"]["key"]
            host = Services().public_data()["params"]["host"]
            url = f"{host}/v1/track/geofence/list?key={key}"
            sid = playload.get("sid")
            if "#sid#" == sid:
                sid = Services().search_services()["data"]["results"][0]["sid"]
            playload['sid'] = sid

            ir = BaseApi()

            r = ir.run_method(url=url, json=playload, method='post')

            return r

        def geofence_delete(self, playload: dict):  #删除围栏接口
            key = Services().public_data()["params"]["key"]
            host = Services().public_data()["params"]["host"]
            url = f"{host}/v1/track/geofence/delete?key={key}"
            sid = playload.get("sid")
            if "#sid#" == sid:
                sid = Services().search_services()["data"]["results"][0]["sid"]
            playload['sid'] = sid
            gfids = playload.get("gfids")
            if "#gfids#" == gfids:
                playload = Services().geofence_data()['geofence_list']
                gfids=self.geofence_list(playload)["data"]["results"][-1]["gfid"]

            playload['gfids'] = gfids
            ir = BaseApi()

            r = ir.run_method(url=url, json=playload, method='post')

            return r

        def geofence_bind(self,playload1: dict):   #增加监测对象接口
            key = Services().public_data()["params"]["key"]
            host = Services().public_data()["params"]["host"]

            url = f"{host}/v1/track/geofence/terminal/bind?key={key}"
            sid = playload1.get("sid")
            if "#sid#" == sid:
                sid = Services().search_services()["data"]["results"][0]["sid"]
            playload1['sid'] = sid
            gfid = playload1.get("gfid")
            if "#gfid#" == gfid:
                playload = Services().geofence_data()['geofence_list']
                gfid = self.geofence_list(playload)["data"]["results"][0]["gfid"]
            playload1['gfid'] = gfid

            tids = playload1.get("tids")
            if "#tids#" == tids:
                r=Services().search_termnial()
                tid_list = []  # 将查询终端接口返回tid 放到列表中
                for i in range(0,r["data"]["count"]):
                    tid_list.append([r["data"]["results"][i]["tid"]])


                tids_list = reduce(lambda x, y: x + y, tid_list) #  将二维列表转换成一维列表


                tids = ','.join(str(n) for n in tids_list) #将列表转换为字符串，由于列表中包含数字所以不能直接使用','.join(tids_list)

            playload1['tids'] = tids



            ir = BaseApi()

            r = ir.run_method(url=url, json=playload1, method='post')

            return r

        def geofence_unbind(self,playload1: dict):   #删除监测对象接口
            key = Services().public_data()["params"]["key"]
            host = Services().public_data()["params"]["host"]

            url = f"{host}/v1/track/geofence/terminal/unbind?key={key}"
            sid = playload1.get("sid")
            if "#sid#" == sid:
                sid = Services().search_services()["data"]["results"][0]["sid"]
            playload1['sid'] = sid
            gfid = playload1.get("gfid")
            if "#gfid#" == gfid:
                playload = Services().geofence_data()['geofence_list']
                gfid = self.geofence_list(playload)["data"]["results"][0]["gfid"]
            playload1['gfid'] = gfid

            tids = playload1.get("tids")
            if "#tids#" == tids:

                r = Services().search_termnial()
                tid_list = []  # 将查询终端接口返回tid 放到列表中
                for i in range(0, r["data"]["count"]):
                    tid_list.append([r["data"]["results"][i]["tid"]])

                tids_list = reduce(lambda x, y: x + y, tid_list)  # 将二维列表转换成一维列表

                tids = ','.join(str(n) for n in tids_list)  # 将列表转换为字符串，由于列表中包含数字所以不能直接使用','.join(tids_list)

            playload1['tids'] = tids

            ir = BaseApi()

            r = ir.run_method(url=url, json=playload1, method='post')

            return r

        def geofence_bindlist(self, playload1: dict):  #查询监测对象接口
            key = Services().public_data()["params"]["key"]
            host = Services().public_data()["params"]["host"]

            url = f"{host}/v1/track/geofence/terminal/list?key={key}"
            sid = playload1.get("sid")
            if "#sid#" == sid:
                sid = Services().search_services()["data"]["results"][0]["sid"]
            playload1['sid'] = sid
            gfid = playload1.get("gfid")
            if "#gfid#" == gfid:
                playload = Services().geofence_data()['geofence_list']
                gfid = self.geofence_list(playload)["data"]["results"][0]["gfid"]
            playload1['gfid'] = gfid


            ir = BaseApi()

            r = ir.run_method(url=url, json=playload1, method='post')

            return r

        def geofence_terminal(self,data:dict ):  #查询检测对象与围栏关系
            key = Services().public_data()["params"]["key"]
            host = Services().public_data()["params"]["host"]


            sid = data.get("sid")
            if "#sid#" == sid:
                sid = Services().search_services()["data"]["results"][0]["sid"]
                data['sid']  = sid
            tid = data.get("tid")
            if "#tid#" == tid:

                tid =Services().search_termnial()["data"]["results"][0]["tid"]
            data['tid'] = tid


            url = f"{host}/v1/track/geofence/status/terminal?key={key}&sid={sid}&tid={tid}"
            ir = BaseApi()

            r = ir.run_method(url=url, method='get')

            return r

        def geofence_location(self, data: dict):  # 查询指定坐标与围栏关系
            key = Services().public_data()["params"]["key"]
            host = Services().public_data()["params"]["host"]

            sid = data.get("sid")
            if "#sid#" == sid:
                sid = Services().search_services()["data"]["results"][0]["sid"]
            data['sid'] = sid

            location = Services().geofence_data()["geofence_location"]["location"]


            url = f"{host}/v1/track/geofence/status/location?key={key}&sid={sid}&location={location}"
            ir = BaseApi()

            r = ir.run_method(url=url, method='get')

            return r
        def drivingbehavior(self, data: dict):  # 驾驶行为分析接口
            key = Services().public_data()["params"]["key"]
            host = Services().public_data()["params"]["host"]

            sid = data.get("sid")
            if "#sid#" == sid:
                sid = Services().search_services()["data"]["results"][0]["sid"]
            data['sid'] = sid
            tid = data.get("tid")
            if "#tid#" == tid:
                tid = Services().search_termnial()["data"]["results"][0]["tid"]
            data['tid'] = tid
            trid = data.get("trid")
            if "#trid#" == trid:
                trid = Services().search_track()["data"]["track"][-1]["trid"]
            data['trid'] = trid

            url = f"{host}/v1/track/analysis/drivingbehavior?key={key}&sid={sid}&tid={tid}&trid={trid}"
            ir = BaseApi()

            r = ir.run_method(url=url, method='get')

            return r

        def staypoint(self, data: dict):  # 停留点分析
            key = Services().public_data()["params"]["key"]
            host = Services().public_data()["params"]["host"]

            sid = data.get("sid")
            if "#sid#" == sid:
                sid = Services().search_services()["data"]["results"][0]["sid"]
            data['sid'] = sid
            tid = data.get("tid")
            if "#tid#" == tid:
                tid = Services().search_termnial()["data"]["results"][0]["tid"]
            data['tid'] = tid
            trid= data.get("trid")
            if "#trid#" == trid:
                trid = Services().search_track()["data"]["track"][-1]["trid"]
            data['trid'] = trid

            url = f"{host}/v1/track/analysis/staypoint?key={key}&sid={sid}&tid={tid}&trid={trid}"
            ir = BaseApi()

            r = ir.run_method(url=url, method='get')

            return r
        def track_match (self):  # 轨迹重合度分析接口
            key = Services().public_data()["params"]["key"]
            host = Services().public_data()["params"]["host"]
            sid = Services().search_services()["data"]["results"][0]["sid"]

            tid= Services().search_termnial()["data"]["results"][0]["tid"]

            trid1 = Services().search_track()["data"]["track"][0]["trid"]
            trid2 = Services().search_track()["data"]["track"][-1]["trid"]
            playload={
                      "baseline": {
                           "sid": sid,
                           "tid": tid,
                           "trid": trid1
                                      },
                      "target":{
                            "sid": sid,
                            "tid": tid,
                            "trid":trid2
                                      },
                       "ispoints":1
                                }



            url = f"{host}/v1/track/match?key={key}"
            ir = BaseApi()

            r = ir.run_method(url=url,json=playload, method='post')






            return r

if __name__ == '__main__':
    a = TrackGeofence()
    #a.add_corcle()
    #a.geofence_data
    #a.geofence_bind()
    #a.update_polygon()
    a.update_district(playload={
    "sid": 10548,
    "gfid":"105480107",
    "name": "ABC13_abc艾莉1232432432432000-ejfhhrjjr--rjrj","adcode":33100})
