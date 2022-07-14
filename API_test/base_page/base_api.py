encoding = "utf-8"
import json

import requests


class BaseApi(object):

    def post_method(self, url, data=None, json=None, headers=None):

        if headers is not None:
            r = requests.post(url, data=data, json=json, headers=headers)
        else:
            r = requests.post(url, data=data, json=json)

        if str(r) == "<Response [200]>":
            return r.json()
        else:
            return r.text

    def get_method(self, url, data=None, json=None, headers=None):

        if headers is not None:
            r = requests.get(url, params=data, json=json, headers=headers)
        else:
            r = requests.get(url, params=data, json=json)
        if str(r) == "<Response [200]>":
            return r.json()
        return r.text

    def run_method(self, method, url, data=None, json=None, headers=None):
        if method == 'get' or method == 'GET':
            r = self.get_method(url, data, json, headers)
        elif method == 'post' or method == 'POST':
            r = self.post_method(url, data, json, headers)

        else:
            r = "你的请求方式不正确！"

        # return r, json.dumps(r, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ':'))
        return r

# ensure_ascii：默认值True，如果dict内含有non-ASCII的字符，则会类似\uXXXX的显示数据，设置成False后，就能正常显示。

# indent：应该是一个非负的整型，如果是0，或者为空，则一行显示数据，否则会换行且按照indent的数量显示前面的空白，这样打印出来的json数据也叫pretty-printed json。

# separators：分隔符，实际上是(item_separator, dict_separator)的一个元组，默认的就是(‘,’,’:’)；这表示dictionary内keys之间用“,”隔开，而KEY和value之间用“：”隔开。

# encoding：默认是UTF-8，设置json数据的编码方式。

# sort_keys：将数据根据keys的值进行排序。

