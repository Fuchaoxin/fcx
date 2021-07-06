# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
from test_cases.interface_cases import conftest
import time
import random
import random
import random
#@pytest.mark.usefixture("test_getToken")
class TestCase():
        value=1
      
        @allure.step("接口test_getBottomIconList")
        def test_getBottomIconList(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "page": {"pageNum": 1, "pageSize": 20},
                "content": {
                                'name': "",
                                'platform': "",
                                'type': "bg"
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/bottomIcon/getBottomIconList', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'getBottomIconList')

        @allure.step("接口test_insertBottomIconItem")
        def test_insertBottomIconItem(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "page": {"pageNum": 1, "pageSize": 20},
                "content": {
                    'active': 'false',
                    'bg2x': "https://oss.caizidao.com.cn/rpdt/navBottom_manage/background/162501975520352X78.png",
                    'bg3x': "https://oss.caizidao.com.cn/rpdt/navBottom_manage/background/162501976437878X147.png",
                    'bg4x': "https://oss.caizidao.com.cn/rpdt/navBottom_manage/background/1625019775411104X196.png",
                    'homepage': "https://oss.caizidao.com.cn/rpdt/navBottom_manage/background/1625019745299750X720.png",
                    'imgKey': "",
                    'name': "11111111111111111111",
                    'platform': "ios",
                    'sd2x': "https://oss.caizidao.com.cn/rpdt/navBottom_manage/shadow/162501978391352X22.png",
                    'sd3x': "https://oss.caizidao.com.cn/rpdt/navBottom_manage/shadow/162501979359478X33.png",
                    'sd4x': "https://oss.caizidao.com.cn/rpdt/navBottom_manage/shadow/1625019803707104X44.png",
                    'type': "bg"
                            }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/bottomIcon/insertBottomIconItem', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'insertBottomIconItem')

        @allure.step("接口test_getBottomIconList")
        def test_getBottomIconList(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "page": {"pageNum": 1, "pageSize": 20},
                "content": {
                    'name': "",
                    'platform': "",
                    'type': "bg"
                }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/bottomIcon/getBottomIconList', data=payload1,
                               headers=headers)
            global value
            value = r1.json()['content']['list'][0]['id']
            return (value)

        @allure.step("接口test_updateBottomIconItem")
        def test_updateBottomIconItem(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "page": {"pageNum": 1, "pageSize": 20},
                "content": {
                    'active': 'false',
                    'bg2x': "https://oss.caizidao.com.cn/rpdt/navBottom_manage/background/162501975520352X78.png",
                    'bg3x': "https://oss.caizidao.com.cn/rpdt/navBottom_manage/background/162501976437878X147.png",
                    'bg4x': "https://oss.caizidao.com.cn/rpdt/navBottom_manage/background/1625019775411104X196.png",
                    'homepage': "https://oss.caizidao.com.cn/rpdt/navBottom_manage/background/1625019745299750X720.png",
                    'imgKey': "",
                    'id': value,
                    'name': "11111111111111111222",
                    'platform': "ios",
                    'sd2x': "https://oss.caizidao.com.cn/rpdt/navBottom_manage/shadow/162501978391352X22.png",
                    'sd3x': "https://oss.caizidao.com.cn/rpdt/navBottom_manage/shadow/162501979359478X33.png",
                    'sd4x': "https://oss.caizidao.com.cn/rpdt/navBottom_manage/shadow/1625019803707104X44.png",
                    'type': "bg"
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/bottomIcon/updateBottomIconItem', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'updateBottomIconItem')

        @allure.step("接口test_delBottomIconByIds")
        def test_delBottomIconByIds(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {

                    'deleteIds': [value]

                }
            }
            print(payload1)
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/bottomIcon/delBottomIconByIds', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'delBottomIconByIds')


if __name__ == "__main__":
    pytest.main(['-s', 'test_add_edit_deleteLabelbg'])
