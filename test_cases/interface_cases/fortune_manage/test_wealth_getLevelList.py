# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_wealth_getLevelList")
def test_wealth_getLevelList(test_getToken):
    payload1 = {
        "accessToken": test_getToken

    }
    headers ={
        "Content-Type":"application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/shopping-cms-api/wealth/getLevelList', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_wealth_getLevelList')


if __name__ == "__main__":
    test_wealth_getLevelList()
    pytest.main(['-s','test_wealth_getLevelList.py'])
