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
#@pytest.mark.usefixture("test_getToken")
class TestCase():
        value=1

        @allure.step("接口test_addMaterialInfo")
        def test_addMaterialInfo(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                    'activityType': "",
                    'appType': "1",
                    'jumpLink': "llczd://www.services.czd.com.cn/m/vlog/index",
                    'linkPopInfo': {
                    'downloadButton': None,
                    'imageClickEffect': None,
                    'linkPopImageUrl': ""},
                    'linkType': "1",
                    'materialDescribe': "APP位置-讲股堂-讲股堂主页",
                    'materialName': "test1111111111111111",
                    'materialSonList': [{
                    'imageUrl': "https://oss.caizidao.com.cn/rpdt/advertising/materialImg/162442879065772.png",
                    'materialType': 4 }]
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/material/addMaterialInfo', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'test_addMaterialInfo')

        @allure.step("接口test_selMaterialList")
        def test_selMaterialList(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "page":{"pageNum": 1,"pageSize":20},
                "content": {'creator': None,
                            'endCreateTime': None,
                            'materialName': None,
                            'startCreateTime': None
                            }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/material/selMaterialList', data=payload1,headers=headers)

            global value
            value= r1.json()['content']['list'][0]['materialCode']
            return (value)

        @allure.step("接口test_updateMaterialInfo")
        def test_updateMaterialInfo(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                    'activityType': "",
                    'appType': "1",
                    'jumpLink': "llczd://www.services.czd.com.cn/m/vlog/index",
                    'linkPopInfo': {
                    'downloadButton': None,
                    'imageClickEffect': None,
                    'linkPopImageUrl': ""},
                    'linkType': "1",
                    'materialCode': value,
                    'materialDescribe': "APP位置-讲股堂-讲股堂主页",
                    'materialName': "test1111111111112222",
                    'materialSonList': [{
                    'imageUrl': "https://oss.caizidao.com.cn/rpdt/advertising/materialImg/162442879065772.png",
                    'materialType': 4 }]
                            }
            }
            print(payload1)
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/material/updateMaterialInfo', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'test_updateMaterialInfo')

        @allure.step("接口test_delMaterialInfoByCode")
        def test_delMaterialInfoByCode(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {'materialCode':value}
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/material/delMaterialInfoByCode', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'delMaterialInfoByCode')


if __name__ == "__main__":
    pytest.main(['-s', 'test_add_edit_deleteMaterial'])
