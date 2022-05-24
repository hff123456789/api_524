import random

import allure
import pytest
import yaml

from API_test.base_page import BaseApi
from API_test.services import Services


class TestDebug:
    @allure.feature("服务")
    @allure.story("查询服务")
    @allure.title("新增服务参数校验")
    @pytest.mark.parametrize("playload", yaml.safe_load(open("name_data.yaml", encoding="utf-8")))
    def test_creat_services(self,playload):

        errcode=playload["errcode"]
        errmsg=playload["errmsg"]
        r1=Services().search_services()
        len1=len(r1["data"]["results"])
       # print(len1)
        if len1 > 14:
            Services().delete_service()
            r = Services().creat_services(playload)
        else:
            r=Services().creat_services(playload)

        assert r["errcode"]==errcode
        assert r["errmsg"]==errmsg

    @allure.feature("服务")
    @allure.story("查询服务")
    @allure.title("新增服务最大值校验")
    def test_services_max(self):
        r1 = Services().search_services()
        len1 = len(r1["data"]["results"])
        name = f"服务{random.randint(111119, 999999)}"
        if len1<=15:
             r=Services().creat_services(playload={"name": name, "desc": "test123"})
             assert r['errcode']==21118
             assert r['errmsg'] in "超过service最大数量15"





    @allure.feature("服务")
    @allure.story("查询服务")
    def test_search_service(self):
       r= Services().search_services()
       print(r)

    @allure.feature("服务")
    @allure.story("删除服务")
    @allure.title("删除服务成功")
    def test_delete_service(self):
        r1 = Services().search_services()
        len1 = len(r1["data"]["results"])
        if len1>2:

            r = Services().delete_service()
        else:
            name = f"tongtong{random.randint(111119, 999999)}"
            Services().creat_services(playload={"name":name,"desc":"test123"})
            r=Services().delete_service()
        assert r['errcode']==0

    @allure.feature("服务")
    @allure.story("修改服务服务")
    @allure.title("修改服务成功")
    def test_update_service(self):
        r1 = Services().search_services()
        len1 = len(r1["data"]["results"])
        if len1 == 0:
            name = f"tongtong{random.randint(111119, 999999)}"
            Services().creat_services(playload={"nam":name,"desc":77777})

        r=Services().update_service()
        print(r)
        assert r['errcode']==0

    @allure.feature("服务")
    @allure.story("修改服务服务")
    @allure.title("修改服务失败-重名")
    def test_update_service(self):
        r1 = Services().search_services()
        len1 = len(r1["data"]["results"])
        if len1 == 0:
           r1= Services().creat_services()

        r = Services().update_service(playload=[{"name":159,"desc":126},{"name":159,"desc":855}])
        print(r)
        assert r['errcode'] == 0




    @allure.feature("终端")
    @allure.story("创建终端")
    def test_creat_termianl(self):
        r=Services().cearte_termianl()
        len1=r["data"]["count"]

        r=Services().cearte_termianl()
        print("通过")
        assert r["errcode"] == 0

    @allure.feature("终端")
    @allure.title("查询终端")
    def test_search_TERM(self):
        r=Services().search_termnial()
        print(r)
        assert r["errcode"] == 0

    def test_search_service1(self):

        for i in range(1,11):
           r=Services().search_services()

           Services().cearte_termianl()
           Services().search_track()
           Services().track_upload()
           Services().update_terminal()



           Services().search_KEY()
           Services().polygonsearch()
           Services().aroundsearch()
           #Services().delete_service()
           print(i)
         #print(len(r["data"]["results"]))


    @allure.feature("搜索终端")
    @allure.title("关键字查找终端")
    def test_keysearch(self):

        r = Services().search_KEY()

        assert r["errcode"]==0

    def test_districtsearc(self):
        key = Services().public_data()["params"]["key"]
        sid = Services().search_services()["data"]["results"][0]["sid"]


        url = f"http://test-trapi.langgemap/v1/track/terminal/districtsearc?key={key}"
        playload ={

               "sid":10334,
               "keywords":"浙江",
               "filter":"name=a",
              "sortrule":"name:asc",
              "page":1,
              "pagesize":50
}
        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        print(r)

        return r
if __name__=='__main__':
    pytest.main()



