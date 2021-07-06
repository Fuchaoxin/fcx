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
#@pytest.mark.usefixture("test_getToken")
class TestCase():
        value=1

        @allure.step("接口test_addLaunchPageInfo")
        def test_addLaunchPageInfo(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                    'imageUrl': "https://oss.caizidao.com.cn/rpdt/advertising/StartPageImg/16244330108121125X2436.png",
                    'launchPageName': "test启动页"
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/launchPage/addLaunchPageInfo', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'addLaunchPageInfo')

        @allure.step("接口test_selLaunchPageList")
        def test_selLaunchPageList(self):
            payload1 = {
                "accessToken": config.TOKEN,
                "page": {"pageNum": 1, "pageSize": 20},
                "content": {"creator": None,
                            "endCreateTime": None,
                            "launchPageName": None,
                            "launchPageStatus": 0,
                            "startCreateTime": None}
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/launchPage/selLaunchPageList', data=payload1,
                               headers=headers)
            global value
            value = r1.json()['content']['list'][0]['launchPageId']
            return (value)

        @allure.step("接口test_updateLaunchPageInfo")
        def test_updateLaunchPageInfo(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                    'imageUrl': "https://oss.caizidao.com.cn/rpdt/advertising/StartPageImg/16244330108121125X2436.png",
                    'launchPageId': value,
                    'launchPageName': "test启动页"+str(random.randint(0,9999))
                            }
            }
            print(payload1)
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/launchPage/updateLaunchPageInfo', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'test_updateLaunchPageInfo')

        @allure.step("接口test_useLaunchPageById")
        def test_useLaunchPageById(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {'launchPageId':value}
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/launchPage/useLaunchPageById', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'useLaunchPageById')


if __name__ == "__main__":
    pytest.main(['-s', 'test_add_edit_closeLaunchPage'])
