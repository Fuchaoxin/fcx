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
       
        @allure.step("接口test_insertBottomIconItem")
        def test_insertBottomIconItem(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                                'active': 'false',
                                'icon2x': "https://oss.caizidao.com.cn/rpdt/navBottom_manage/icon/162501739296498X98.png",
                                'icon3x': "https://oss.caizidao.com.cn/rpdt/navBottom_manage/icon/1625017404154147X147.png",
                                'icon4x': "https://oss.caizidao.com.cn/rpdt/navBottom_manage/icon/1625017412218196X196.png",
                                'imgKey': "vlog",
                                'name': "test1111111111111111",
                                'platform': "adr",
                                'selected': 'false',
                                'type': "icon"
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/bottomIcon/insertBottomIconItem', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'insertBottomIconItem')

        @allure.step("接口test_getBottomIconList")
        def test_getBottomIconList(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "page": {"pageNum": 1, "pageSize": 20},
                "content": {"imgKey": "",
                            "name": "",
                            "platform": "",
                            "type": "icon"
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
                "content": {
                    'active': 'false',
                    'icon2x': "https://oss.caizidao.com.cn/rpdt/navBottom_manage/icon/162501739296498X98.png",
                    'icon3x': "https://oss.caizidao.com.cn/rpdt/navBottom_manage/icon/1625017404154147X147.png",
                    'icon4x': "https://oss.caizidao.com.cn/rpdt/navBottom_manage/icon/1625017412218196X196.png",
                    'imgKey': "vlog",
                    'id': value,
                    'name': "test1111111111112222",
                    'platform': "adr",
                    'selected': 'false',
                    'type': "icon"
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

        @allure.step("接口test_updateBottonIconSwitch")
        def test_updateBottonIconSwitch(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'active': 'true',
                    'id': value,
                    'type': 'icon'
                }
            }
            print(payload1)
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/bottomIcon/updateBottonIconSwitch', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'updateBottonIconSwitch')

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
    pytest.main(['-s', 'test_add_edit_deleteBottomIconItem'])
