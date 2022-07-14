import time
from functools import reduce

import allure
import yaml

import random
import string

from autotest_api.base_page.base_api import BaseApi


class Services(BaseApi):

    def geofence_data(self):  # 读取围栏参数的yaml文件
        with open('../config/geofence_data.yaml', 'r') as f:
            geofence_data = yaml.safe_load(f)

            return geofence_data

    def track_data(self):
        with open('../config/track_data.yaml', 'r') as f:
            data = yaml.safe_load(f)


            return data

    def public_data(self):
        with open('../config/common_data.yaml', 'r') as f:
            data_key = yaml.safe_load(f)
            return data_key

    def name_var(self):
        add_service = f"新增服务{random.randint(111119, 999999)}"
        update_service = f"修改服务{random.randint(111119, 999999)}"
        add_termianl = f"新增终端1{random.randint(12, 999999)}"
        update_desc = f"修改desc{random.randint(111119, 999999)}"

        return add_service, update_service, add_termianl, update_desc

    #  def var(self):
    # vars = ''.join(random.sample(string.ascii_letters + string.digits, 20))
    # print(vars)

    def creat_services(self, playload: dict):
        key = self.public_data()["params"]["key"]
        host = self.public_data()["params"]["host"]
        url = f"{host}/v1/track/service/add?key={key}"

        # 改变name的值
        name = playload.get("name")
        if "#name#" == name:
            name = self.name_var()[0]
        playload['name'] = name

        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        # print(type(r))

        return r

    # seed = "qwer123456789测试服务"
    # str = []
    # g改哪个值？
    # for i in range(8):
    #     str.append(random.choice(seed))
    # name = ''.join(str)

    # playload=playload
    # 你把playload都当成一个整体了把....是

    # 哪儿调用creat_services
    # playload = {"name": name, "desc": None}

    # r = requests.post(url=url, json=data, headers=headers)

    def search_services(self):
        key = self.public_data()["params"]["key"]
        host = self.public_data()["params"]["host"]
        url = f"{host}/v1/track/service/list?key={key}"
        #headers = {"Content-Type": "application/json"}
        playload={"key":"76984a1ccba04ab8815a87d25f300fa2"}

        ir = BaseApi()

        r = ir.run_method(url=url,json=playload, method='post')



        # results = r["data"]["results"]
        # print(results)

        return r

    def update_service(self):
        name = self.name_var()[1]

        sid = self.search_services()["data"]["results"][0]["sid"]
        key = self.public_data()["params"]["key"]
        host = self.public_data()["params"]["host"]
        url = f"{host}/v1/track/service/update?key={key}"
        playload = {
            "sid": sid,
            "name": name,
            "desc": None}
        allure.attach("用例参数", "{0}".format(playload))
        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        # print(type(r))


        return r

    def delete_service(self):

        sid = self.search_services()["data"]["results"][-1]["sid"]
        key = self.public_data()["params"]["key"]
        host = self.public_data()["params"]["host"]
        url = f"{host}/v1/track/service/delete?key={key}"
        playload = {
            "sid": sid}

        ir = BaseApi()
        allure.attach("用例参数", "{0}".format(playload))

        r = ir.run_method(url=url, json=playload, method='post')

        # print(type(r))

        return r

    def cearte_termianl(self):

        sid = self.search_services()["data"]["results"][0]["sid"]
        key = self.public_data()["params"]["key"]
        host = self.public_data()["params"]["host"]
        url = f"{host}/v1/track/terminal/add?key={key}"
        name = self.name_var()[2]
        playload = {
            "sid": sid,
            "name": name,
            "desc": ''.join(random.sample(string.ascii_letters + string.digits, 20))

        }
        allure.attach("用例参数", "{0}".format(playload))

        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        # print(type(r))

        return r

    def search_termnial(self):
        results = self.search_services()["data"]["results"]
        if len(results) == 0:
            self.creat_services()
        sid = Services().search_services()["data"]["results"][0]["sid"]
        key = self.public_data()["params"]["key"]
        host = self.public_data()["params"]["host"]
        url = f"{host}/v1/track/terminal/list?key={key}"
        playload = {
            "sid": sid,
            "tid": None,
            "name": None,
            "page": 1

        }
        allure.attach("用例参数", "{0}".format(playload))

        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')
        # tid_list=[]   #将查询终端接口返回tid 放到列表中
        # for i in range(0,r["data"]["count"]):
        #     tid_list.append([r["data"]["results"][i]["tid"]])
        # 
        # 
        # tids_list = reduce(lambda x, y: x + y, tid_list) #  将二维列表转换成一维列表


        return r 

    def update_terminal(self):
        sid = self.search_services()["data"]["results"][0]["sid"]
        tid = self.search_termnial()["data"]["results"][0]["tid"]
        key = self.public_data()["params"]["key"]
        host = self.public_data()["params"]["host"]
        url = f"{host}/v1/track/terminal/update?key={key}"

        playload = {
            "sid": sid,
            "tid": tid,
            "desc": self.name_var()[3]
        }
        allure.attach("用例参数", "{0}".format(playload))
        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        # print(type(r))

        return r

    def delete_terminal(self):

        sid = self.search_services()["data"]["results"][0]["sid"]
        tid = self.search_termnial()["data"]["results"][-1]["tid"]
        key = self.public_data()["params"]["key"]
        host = self.public_data()["params"]["host"]
        url = f"{host}/v1/track/terminal/delete?key={key}"

        playload = {
            "sid": sid,
            "tid": tid,

        }
        allure.attach("用例参数", "{0}".format(playload))
        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        # print(type(r))

        return r

    def creat_track(self):

        sid = self.search_services()["data"]["results"][0]["sid"]
        tid = self.search_termnial()["data"]["results"][0]["tid"]
        key = self.public_data()["params"]["key"]
        host = self.public_data()["params"]["host"]
        url = f"{host}/v1/track/trace/add?key={key}"

        playload = {
            "sid": sid,
            "tid": tid,
            "trname": "轨迹1233223"

        }
        allure.attach("用例参数", "{0}".format(playload))
        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        # print(type(r))

        return r

    def track_upload(self):
        trid = self.creat_track()["data"]["trid"]
        sid = self.search_services()["data"]["results"][0]["sid"]

        tid = self.search_termnial()["data"]["results"][0]["tid"]
        key = self.public_data()["params"]["key"]
        #locatetime = int(round(time.time()*1000))
        #locatetime1=int(round(time.time()*1000)-2000)

        #locatetime2=int(round(time.time()*1000)-1000)
        playload={
            "sid": sid,
            "tid": tid,
            "trid": trid,
            "points":[{"location": "120.20701747744279,30.288684557004196","locatetime": int(round(time.time()*1000)-30000),"speed": 22.273179046005563,"direction": 224.2361015410238},
               {"location": "120.20686914949592,30.288532379165137","locatetime": int(round(time.time()*1000)-29000),"speed": 43.60087480782832,"direction": 219.35377378341366},
	           {"location": "120.20659053599174,30.288193049087177","locatetime": int(round(time.time()*1000)-26000),"speed": 55.25959259811401,"direction": 212.6096404269688},
	           {"location": "120.20626482484077,30.287684672158658","locatetime": int(round(time.time()*1000)-23000),"speed": 19.870041344791186,"direction": 279.9638041895466},
              {"location":  "120.20611647861055,30.28771047252029","locatetime": int(round(time.time()*1000)-20000),"speed": 48.16710075298795,"direction": 294.6404247499397},
            {"location": "120.20576464648033,30.287870986265297","locatetime": int(round(time.time()*1000)-19000),"speed": 42.88674895334834,"direction": 294.6645872572193},
              {"location": "120.20545140077817,30.288014049238566","locatetime": int(round(time.time()*1000)-16000),"speed": 42.88674895334834,"direction": 294.6645872572193},
              {"location": "120.20513815507603,30.288157112211834","locatetime": int(round(time.time()*1000)-13000),"speed": 18.87364079292673,"direction": 301.27480548197445},
           {"location": "120.20500282966537,30.28823891994306","locatetime": int(round(time.time()*1000)-10000),"speed": 25.854859194856704,"direction": 305.5376777923976},
             {"location": "120.20482038845391,30.288368657919047","locatetime": int(round(time.time()*1000)-9000),"speed": 22.253729349139896,"direction": 311.6101341992412},
	              {"location": "120.2046680169938,30.28850343562196","locatetime": int(round(time.time()*1000)-6000),"speed": 18.97357237362089,"direction": 315.8951737119376},
              {"location": "120.20454170703302,30.288633248970527","locatetime": int(round(time.time()*1000)-3000),"speed": 26.900502832686886,"direction": 326.6376454640722},
               {"location": "120.2043813062812,30.288876003095854","locatetime": int(round(time.time()*1000)),"speed": 16.53413777707916,"direction": 311.5074068393496}]
        }
        allure.attach("用例参数", "{0}".format(playload))
        #y一次性上传100个点
        # for i in range(len(self.track_data())):
        #     playload = {
        #         "sid": sid,
        #         "tid": tid,
        #         "trid": trid,
        #         "points": [
        #             {
        #                 "location": self.track_data()[i]["location"],
        #
        #                 "locatetime": self.track_data()[i]["locatetime"],
        #                 "speed": self.track_data()[i]["speed"],
        #                 "direction": self.track_data()[i]["direction"],
        #                 "height": self.track_data()[i]["height"],
        #                 "accuracy": self.track_data()[i]["accuracy"]
        #             }
        #         ]
        #     }
        host = self.public_data()["params"]["host"]
        url = f"{host}/v1/track/point/upload?key={key}"

        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        print(r)

        return r

    def search_track(self):
        #trid = self.creat_track()["data"]["trid"]
        key = self.public_data()["params"]["key"]
        sid = self.search_services()["data"]["results"][0]["sid"]

        tid = self.search_termnial()["data"]["results"][0]["tid"]

        endtime=int(time.time())    #将时间戳格式转换成int

        host = self.public_data()["params"]["host"]
        url = f"{host}/v1/track/terminal/trsearch?key={key}&sid={sid}&tid={tid}&starttime=1638201600000&endtime={endtime}"

        ir = BaseApi()

        r = ir.run_method(url=url, method='get')



        return r

    def terminal_lastpoint(self):  #实时查询终端位置接口
        key = self.public_data()["params"]["key"]
        sid = self.search_services()["data"]["results"][0]["sid"]

        tid = self.search_termnial()["data"]["results"][0]["tid"]
        host = self.public_data()["params"]["host"]
        url = f"{host}/v1/track/terminal/lastpoint?key={key}&sid={sid}&tid={tid}&correction="

        ir = BaseApi()

        r = ir.run_method(url=url, method='get')



        return r


    def search_KEY(self):
        key = self.public_data()["params"]["key"]
        sid = self.search_services()["data"]["results"][0]["sid"]

        tid = self.search_termnial()["data"]["results"][0]["tid"]
        host = self.public_data()["params"]["host"]
        url = f"{host}/v1/track/terminal/search?key={key}"
        playload = {

            "sid": sid,
            "keywords": "终端",
            "filter": None,
            "sortrule": "",
            "page": 1,
            "pagesize": 100

        }
        allure.attach("用例参数", "{0}".format(playload))
        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')



        return r

    def aroundsearch(self):
        key = self.public_data()["params"]["key"]
        sid = self.search_services()["data"]["results"][0]["sid"]
        host = self.public_data()["params"]["host"]

        url = f"{host}/v1/track/terminal/aroundsearch?key={key}"
        playload = {
            "sid": sid,
            "center": "120.186036,30.248899",
            "radius": "200",
            "page": 6,
            "pagesize": 1
        }
        allure.attach("用例参数", "{0}".format(playload))
        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')



        return r

    def districtsearch(self):
        key = self.public_data()["params"]["key"]
        sid = self.search_services()["data"]["results"][0]["sid"]

        host = self.public_data()["params"]["host"]
        url = f"{host}/v1/track/terminal/districtsearch?key={key}"
        playload = {

            "sid": sid,
            "keywords": "浙江",
            "filter": None,
            "sortrule": None,
            "page": 1,
            "pagesize": 50
        }
        allure.attach("用例参数", "{0}".format(playload))

        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')



        return r

    def polygonsearch(self):
        key = self.public_data()["params"]["key"]
        sid = self.search_services()["data"]["results"][0]["sid"]

        host = self.public_data()["params"]["host"]

        url = f"{host}/v1/track/terminal/polygonsearch?key={key}"
        playload = {
            "sid": sid,
            "polygon": "120.295589,30.17264;120.432414,30.234708;120.621316,30.153123",
            "filter": "",
            "sortrule": "",
            "page": None,
            "pagesize": None
        }
        ir = BaseApi()
        allure.attach("用例参数", "{0}".format(playload))

        r = ir.run_method(url=url, json=playload, method='post')



        return r


if __name__ == '__main__':
    a = Services()

   # a.creat_services(playload={"name": 189, "desc": 555})
    #a.search_services()
    #a.update_service()
    # a.delete_service()
    #a.cearte_termianl()
   # a.search_termnial()
    # a.var()
    # a.update_terminal()
    # a.delete_terminal()
    # a.creat_track()
    a.track_upload()
    # a.track_data()
    #a.geofence_data()
    #a.search_track()
    # a.search_KEY()
# a.aroundsearch
    #a.districtsearch()
# a.polygonsearch()
# a.read_yaml()
# a.public_data()
