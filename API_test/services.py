import pytest
import yaml

from API_test.base_page import BaseApi

import random
import string


class Services(BaseApi):

    # def read_yaml():
    # with open("../data/data.yaml", encoding="utf-8") as f:
    # print(f.read())
    # a = yaml.safe_load(f)
    # return a

    def track_data(self):
        with open('track_data.yaml', 'r') as f:
            data = yaml.safe_load(f)

            return data
    def public_data(self):
        with open('common_data.yaml', 'r') as f:
            data_key = yaml.safe_load(f)
            return data_key


  #  def var(self):
       # vars = ''.join(random.sample(string.ascii_letters + string.digits, 20))
       # print(vars)


    def creat_services(self,playload:dict):
        key = self.public_data()["params"]["key"]
        host = self.public_data()["params"]["host"]
        url = f"{host}/v1/track/service/add?key={key}"

        # 改变name的值
        name=playload.get("name")
        if "#name#"==name:
            name=f"tongtong{random.randint(111119,999999)}"
        playload['name']=name
        print(playload)
        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        # print(type(r))
        print(r)

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
        playload = {"key": "666f511920b14707ae549a85379684e9"}

        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        # print(type(r))
        print(r)
        # results = r["data"]["results"]
        # print(results)

        return r

    def update_service(self):
        name=f"被修改的服务{random.randint(111119,999999)}"
        r=self.search_services()
        if len(r["data"]["results"])==0:
            self.creat_services()
        sid = self.search_services()["data"]["results"][0]["sid"]
        key = self.public_data()["params"]["key"]
        host = self.public_data()["params"]["host"]
        url = f"{host}/v1/track/service/update?key={key}"
        playload = {
            "sid": sid,
            "name": name,
            "desc": None}

        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        # print(type(r))
        print(r)

        return r

    def delete_service(self):

        results = self.search_services()["data"]["results"]
        if len(results) == 0:
            self.creat_services()
        sid = self.search_services()["data"]["results"][-1]["sid"]
        key = self.public_data()["params"]["key"]
        host = self.public_data()["params"]["host"]
        url = f"{host}/v1/track/service/delete?key={key}"
        playload = {
            "sid": sid}

        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        # print(type(r))
        print(r)
        return r

    def cearte_termianl(self):
        results = self.search_services()["data"]["results"]
        if len(results) == 0:
            self.creat_services()
        sid = self.search_services()["data"]["results"][0]["sid"]
        key = self.public_data()["params"]["key"]
        host = self.public_data()["params"]["host"]
        url = f"{host}/v1/track/terminal/add?key={key}"

        playload = {
            "sid": sid,
            "name": ''.join(random.sample(string.ascii_letters + string.digits, 20)),
            "desc": ''.join(random.sample(string.ascii_letters + string.digits, 20))

        }

        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        # print(type(r))
        print(r)
        return r

    def search_termnial(self):
        results = self.search_services()["data"]["results"]
        if len(results) == 0:
            self.creat_services()
        sid = self.search_services()["data"]["results"][0]["sid"]
        key = self.public_data()["params"]["key"]
        host = self.public_data()["params"]["host"]
        url = f"{host}/v1/track/terminal/list?key={key}"
        playload = {
            "sid": sid,
            "tid": None,
            "name": None,
            "page": 1

        }

        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        # print(type(r))
        print(r)
        return r

    def update_terminal(self):
        results = self.search_services()["data"]["results"]
        if len(results) == 0:
            self.creat_services()
        sid = self.search_services()["data"]["results"][0]["sid"]
        count=self.search_termnial()["data"]["count"]
        if count==0:
            self.cearte_termianl()
        tid = self.search_termnial()["data"]["results"][0]["tid"]
        key = self.public_data()["params"]["key"]
        host = self.public_data()["params"]["host"]
        url = f"{host}/v1/track/terminal/update?key={key}"

        playload = {
            "sid": sid,
            "tid": tid,
            "desc": "修改终端12346"
        }

        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        # print(type(r))
        print(r)
        return r

    def delete_terminal(self):
        results = self.search_services()["data"]["results"]
        if len(results) == 0:
            self.creat_services()
        sid = self.search_services()["data"]["results"][0]["sid"]
        count = self.search_termnial()["data"]["count"]
        if count == 0:
            self.cearte_termianl()
        tid = self.search_termnial()["data"]["results"][0]["tid"]
        key = self.public_data()["params"]["key"]
        host = self.public_data()["params"]["host"]
        url = f"{host}/v1/track/terminal/delete?key={key}"

        playload = {
            "sid": sid,
            "tid": tid,

        }

        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        # print(type(r))
        print(r)
        return r

    def creat_track(self):
        results = self.search_services()["data"]["results"]
        if len(results) == 0:
            self.creat_services()
        sid = self.search_services()["data"]["results"][0]["sid"]
        count = self.search_termnial()["data"]["count"]
        if count == 0:
            self.cearte_termianl()
        tid = self.search_termnial()["data"]["results"][0]["tid"]
        key = self.public_data()["params"]["key"]
        host = self.public_data()["params"]["host"]
        url = f"{host}/v1/track/trace/add?key={key}"

        playload = {
            "sid": sid,
            "tid": tid,
            "trname": "轨迹123"

        }

        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        # print(type(r))
        print(r)
        return r

    def track_upload(self):
        trid = self.creat_track()["data"]["trid"]
        sid = self.search_services()["data"]["results"][0]["sid"]

        tid = self.search_termnial()["data"]["results"][0]["tid"]
        key = self.public_data()["params"]["key"]
        for i in range(len(self.track_data())):
            playload = {
                "sid": sid,
                "tid": tid,
                "trid": trid,
                "points": [
                    {
                        "location": self.track_data()[i]["location"],

                        "locatetime": self.track_data()[i]["locatetime"],
                        "speed": self.track_data()[i]["speed"],
                        "direction": self.track_data()[i]["direction"],
                        "height": self.track_data()[i]["height"],
                        "accuracy": self.track_data()[i]["accuracy"]
                    }
                ]
            }
            host = self.public_data()["params"]["host"]
            url =f"{host}/v1/track/point/upload?key={key}"

            ir = BaseApi()

            r = ir.run_method(url=url, json=playload, method='post')

            # print(type(r))
            print(sid, tid, trid)

            print(i)
            print(r)
        return r

    def search_track(self):
        key = self.public_data()["params"]["key"]
        sid = self.search_services()["data"]["results"][0]["sid"]

        tid = self.search_termnial()["data"]["results"][0]["tid"]
        host = self.public_data()["params"]["host"]
        url = f"{host}/v1/track/terminal/trsearch?key={key}"
        playload = {

            "sid": sid,
            "tid": tid,
            "ispoints": 1,
            "page": 1,
            "pagesize": 50,
            "starttime": 1638201600000


        }
        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='get')

        print(r)

        return r


    def search_KEY(self):
        key = self.public_data()["params"]["key"]
        sid = self.search_services()["data"]["results"][0]["sid"]

        tid = self.search_termnial()["data"]["results"][0]["tid"]
        host = self.public_data()["params"]["host"]
        url = f"{host}/v1/track/terminal/search?key={key}"
        playload = {

           "sid":sid,
         "keywords":"终端",
        "filter":None,
       "sortrule":"",
       "page":1,
        "pagesize":100

         }
        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        print(r)

        return r
    def aroundsearch(self):
        key = self.public_data()["params"]["key"]
        sid = self.search_services()["data"]["results"][0]["sid"]

        host = self.public_data()["params"]["host"]
        url = f"{host}/v1/track/terminal/aroundsearch?key={key}"
        playload = {
           "sid":sid,
            "center":"120.186036,30.248899",
           "radius":"200",
              "page":6,
           "pagesize":1
          }
        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        print(r)

        return r
    def districtsearc(self):
        key = self.public_data()["params"]["key"]
        sid = self.search_services()["data"]["results"][0]["sid"]

        host = self.public_data()["params"]["host"]
        url = f"{host}/v1/track/terminal/districtsearc?key={key}"
        playload ={

                  "sid":sid,
                  "keywords":"浙江",
                  "filter":None,
                  "sortrule":None,
                  "page":1,
                  "pagesize":50
            }
        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        print(r)

        return r
    def polygonsearch(self):
        key = self.public_data()["params"]["key"]
        sid = self.search_services()["data"]["results"][0]["sid"]

        host = self.public_data()["params"]["host"]
        url = f"{host}/v1/track/terminal/polygonsearch?key={key}"
        playload = {
                    "sid":sid,
                   "polygon":"120.295589,30.17264;120.432414,30.234708;120.621316,30.153123",
                 "filter":"",
              "sortrule":"",
               "page":None,
                 "pagesize":None
             }
        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        print(r)

        return r


if __name__ == '__main__':
    a = Services()
    #a.creat_services()
    #a.search_services()
    a.update_service()
    #a.delete_service()
    #a.cearte_termianl()
    #a.search_termnial()
    # a.var()
    #a.update_terminal()
    #a.delete_terminal()
    #a.creat_track()
    #a.track_upload()
    #a.track_data()
    #a.search_track()
    #a.search_KEY()
   # a.aroundsearch
   # a.districtsearc()
    #a.polygonsearch()