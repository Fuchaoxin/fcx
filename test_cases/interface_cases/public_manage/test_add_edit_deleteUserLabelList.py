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
      
        @allure.step("接口test_addNewLabel")
        def test_addNewLabel(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                                'cateId': "1",
                                'name': "111111",
                                'type': 2
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/newGuidelines/addNewLabel', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'addNewLabel')

        @allure.step("接口test_selSecondaryList")
        def test_selSecondaryList(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "page": {"pageNum": 1, "pageSize": 20},
                "content": {"cateId": "",
                            "name": ""
                            }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/newGuidelines/selSecondaryList', data=payload1,
                               headers=headers)
            global value
            value = r1.json()['content']['list'][0]['id']
            return (value)


        @allure.step("接口test_delNewGuidelines")
        def test_delNewGuidelines(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'ids': [value],
                    'type': 2
                }
            }
            print(payload1)
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/newGuidelines/delNewGuidelines', data=payload1, headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'delNewGuidelines')

if __name__ == "__main__":
    pytest.main(['-s', 'test_add_edit_deleteUserLabelList'])
