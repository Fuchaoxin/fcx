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

class TestCase():
        value=1
      
        @allure.step("接口test_material_save")
        def test_material_save(self):
            payload1 = {
                        'accessToken':config.TOKEN,
                        'material':{
                        "content": ["https://oss.caizidao.com.cn/rpdt/pushMaterial/710X400.png"],
                        'name': "MMMM123",
                        'type': 1
                        }
            }

            headers = {
                "Content-Type": "application/json",
                'Authorization':'false'
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/material/save', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'material_save')

        @allure.step("接口test_material_getList")
        def test_material_getList(self):
            payload1 = {
                'accessToken': config.TOKEN,
                'pageNum': 0,
                'pageSize': 20,
                'txt': ""
            }
            headers = {
                "Content-Type": "application/json",
                "Authorization": "false"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/material/getList', data=payload1, headers=headers)
            global value
            value= r1.json()['content']['list'][0]['id']

            return(value)

        @allure.step("接口test_material_getMaterial")
        def test_material_getMaterial(self):
            payload1 = {
                'accessToken': config.TOKEN,
                'ids': value

            }

            headers = {
                "Content-Type": "application/json",
                'Authorization':'false'
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/material/getMaterial', data=payload1, headers=headers)

            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'material_getMaterial')

        @allure.step("接口test_material_save1")
        def test_material_save1(self):
            payload1 = {
                'accessToken': config.TOKEN,
                'material': {
                             "content": ["https://oss.caizidao.com.cn/rpdt/pushMaterial/710X400.png"],
                             'name': "11725",
                             'type': 1,
                             'createTime': 1624349563841,
                             'enable': 1,
                             'id': value,
                             'modifyTime': None,
                             'operator': "mengying1"
                }
            }

            headers = {
                "Content-Type": "application/json",
                'Authorization':'false'
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/material/save', data=payload1, headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'material_save')


        @allure.step("接口test_material_del")
        def test_material_del(self):
                payload1 = {
                            'accessToken': config.TOKEN,
                            'ids': value

                }
                headers = {
                            "Content-Type": "application/json",
                            'Authorization':'false'
                            }
                payload1 = json.dumps(payload1)
                r1 = requests.post(url=config.Pre_Url + '/cms-api/material/del', data=payload1,
                               headers=headers)
                As = AssertUtil()
                As.assert_code(r1.json()['code'], 200, 'material_del')

if __name__ == "__main__":
    pytest.main(['-s', 'test_add_view_deleteMaterial'])
