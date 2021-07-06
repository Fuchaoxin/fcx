# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_fuzzyQueryUser")
def test_fuzzyQueryUser():
    payload1 = {
        'accessToken':config.TOKEN,
        "page":{"pageNum": 0,"pageSize":0},
        "content": {
                    'keyword': "小财米_EO5571 10006332",
                    'userStatus': 0
                    }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/cms-api/user/fuzzyQueryUser', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_fuzzyQueryUser')


if __name__ == "__main__":

    pytest.main(['-s','test_fuzzyQueryUser.py'])
