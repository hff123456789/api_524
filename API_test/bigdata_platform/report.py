import pytest
import yaml

import random
import string

from autotest_api.base_page.base_api import BaseApi


class Report(BaseApi):

    def sso_login(self):
        url = "http://test-sso.langgemap/langgemap-sso/account/login"
        playload = {"userName": "Feifei.Hong1@geely.com",
                    "password": "E8EF02C821C7C7AFC4906DF255F97D70",
                    "serviceUrl": "sso"
                    }

        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        # print(type(r))
        token = r["data"]["token"]
        print(token)

        return token

    def login(self):
        url = "http://test-bigdata-manager.langgemap/bigdata-platform/account/login"
        token = self.sso_login()

        playload = {
            "token": token
        }
        header = {"version": "1",
                  "env": "dev-k8s",
                  "appkey": "788628",
                  "nonce": "1231fsvnaj qsi1jb je12 ckjxc",
                  "Accept": "application/json, text/plain, */*",
                  "timestamp": "1650442597800",
                  "LG-TraceID": "API documents",
                  "sign": "f1bf7cfd2a8d91d90152f2853a916c9b",
                  "No-Sign": "QvSpMB3meNKw",
                  "Content-Type": "application/json;charset=UTF-8",
                  "Connection": "keep-alive"}

        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, method='post')

        token1 = r["data"]["token"]

        #print(token1)
        return token1


    def creat_task(self):
        url = 'http://test-bigdata-manager.langgemap/bigdata-platform/report-task/add'
        name = f"发送报告任务{random.randint(111119, 999999)}"
        token = self.login()
        header = {
                  "accessToken": token}
        playload = {"name": name,
                    "addressId": 6,
                    "type": 0, "cron": "0 0/1 * * * ?",
                    "testAddressId": 23, "testCron": "0 0/1 * * * ?",
                    "template": "${time:yyyyMMdd|-1}"}

        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, headers=header, method='post')

        # print(type(r))
        #print(r)

        return r

    def task_list(self):
        token = self.login()
        url = "http://test-bigdata-manager.langgemap/bigdata-platform/report-task/select"
        header = {
                  "accessToken": token,
                  }
        playload = {"pageNo": 1, "pageSize": 20}
        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, headers=header, method='post')
        id = r["data"]["records"][1]["id"]
        print(r)
        return r

    def offline(self):
        url = "http://test-bigdata-manager.langgemap/bigdata-platform/report-task/offline"
        token = self.login()

        id = self.task_list()[1]
        header = {"version": "1",
                  "env": "dev-k8s",
                  "appkey": "788628",

                  "method": "bigdataPlatform.index.reportTask.add",
                  "nonce": "1231fsvnaj qsi1jb je12 ckjxc",
                  "Accept": "application/json, text/plain, */*",
                  "timestamp": "1650442597800",
                  "LG-TraceID": "API documents",
                  "sign": "f1bf7cfd2a8d91d90152f2853a916c9b",
                  "accessToken": "zx4bmr9a6775rs1i",
                  "Connection": "keep-alive",
                  "No-Sign": "QvSpMB3meNKw",
                  "sso-token": token}
        playload = {"id": id, "status":0}
        ir = BaseApi()

        r = ir.run_method(url=url, json=playload, headers=header, method='post')
        #print(r, id)
        return r


if __name__ == '__main__':
    a = Report()
   # a.creat_task()
   # a.offline()
    #a.login()
    #a.sso_login()
    a.task_list()
