# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_virtualCoin_getClearCoinRules")
def test_virtualCoin_getClearCoinRules(test_getToken):
    payload1 = {
        "accessToken": test_getToken

    }
    headers ={
        "Content-Type":"application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/shopping-cms-api/virtualCoin/getClearCoinRules', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_virtualCoin_getClearCoinRules')


if __name__ == "__main__":
    test_virtualCoin_getClearCoinRules()
    pytest.main(['-s','test_virtualCoin_getClearCoinRules.py'])
