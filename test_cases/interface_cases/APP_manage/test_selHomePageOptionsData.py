# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_selHomePageOptionsData")
def test_selHomePageOptionsData():
    payload1 = {
        'accessToken':config.TOKEN

    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/cms-api/infoManage/selHomePageOptionsData', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_selHomePageOptionsData')

if __name__ == "__main__":
    test_selHomePageOptionsData()
    pytest.main(['-s','test_selHomePageOptionsData.py'])
