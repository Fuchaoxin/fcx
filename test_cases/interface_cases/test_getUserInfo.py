# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil


@allure.step("接口test_getUserInfo")
def test_getUserInfo():
    payload1 = {
        'accessToken':config.TOKEN,
        'content':{
            'accessToken': config.TOKEN
        }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/cms-api/staff/getUserInfo', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_getUserInfo')


if __name__ == "__main__":
    test_getUserInfo()
    pytest.main(['-s','test_getUserInfo.py'])
