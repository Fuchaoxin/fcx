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

class TestCase():
        value=1
       
        @allure.step("接口test_addBanner")
        def test_addBanner(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                                'bannerImg': "https://oss.caizidao.com.cn/rpdt/banner_image/710X320.png",
                                'creater': "bailingyu",
                                'creatorName': "bailingyu",
                                'enable': 'false',
                                'imageType': "default",
                                'isDeleted': 'false',
                                'resId': 12416,
                                'resType': 1,
                                'sortNum': 1
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/banner/addBanner', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 1,'addBanner')

        @allure.step("接口test_getBannerList")
        def test_getBannerList(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "page": {"pageNum": 1, "pageSize": 20},
                "content": {}
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/banner/getBannerList', data=payload1, headers=headers)
            global value
            value = r1.json()['content']['list'][0]['id']
            return (value)


        @allure.step("接口test_editBanner")
        def test_editBanner(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'bannerImg': "https://oss.caizidao.com.cn/rpdt/banner_image/710X320.png",
                    'enable': 'false',
                    'id': value,
                    'imageType': "default",
                    'isDeleted': 'false',
                    'name': "",
                    'resId': 12413,
                    'resSrc': None,
                    'resType': 1,
                    'sortNum': 1
                            }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/banner/editBanner', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'editBanner')

        @allure.step("接口test_editBanner")
        def test_editBanner(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                            'enable': 'true',
                            'id': value
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/banner/editBanner', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'editBanner')

        @allure.step("接口test_editBanner")
        def test_editBanner(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'isDeleted': 'true',
                    'id': value
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/banner/editBanner', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'editBanner')


if __name__ == "__main__":
    pytest.main(['-s', 'test_add_edit_deleteBanner'])
