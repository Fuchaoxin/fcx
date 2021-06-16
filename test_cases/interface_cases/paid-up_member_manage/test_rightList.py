# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_rightList")
def test_rightList(test_getToken):
    payload1 = {
        'accessToken':test_getToken
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/shopping-cms-api/rights/list', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_rightList')


if __name__ == "__main__":
    test_rightList()
    pytest.main(['-s','test_rightList.py'])
