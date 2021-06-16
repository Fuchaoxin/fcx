# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_findSelectSpecial")
def test_findSelectSpecial(test_getToken):
    payload1 = {
        'accessToken':test_getToken
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/ssax-cls-cms-api/special/findSelectSpecial', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_findSelectSpecial')


if __name__ == "__main__":
    test_findSelectSpecial()
    pytest.main(['-s','test_findSelectSpecial.py'])
