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
        
        @allure.step("接口test_insert")
        def test_insert(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                                'userIdList': ["203efab1-864e-41d2-a2f1-60ca3691d7d8"]
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/kol/insert', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'insert')

        @allure.step("接口test_kol_findKolList")
        def test_kol_findKolList(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "page": {"pageNum": 0, "pageSize": 20,'total': 0},
                "content": {'creater': "",
                            'userId': ""
                            }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/kol/findKolList', data=payload1, headers=headers)
            global value
            value = r1.json()['content']['list'][0]['userId']
            return (value)

        @allure.step("接口test_delete")
        def test_delete(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'userId': value
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/kol/delete', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'delete')


if __name__ == "__main__":
    pytest.main(['-s', 'test_add_edit_deleteKol'])
