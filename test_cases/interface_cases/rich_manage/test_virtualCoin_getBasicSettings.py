# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_virtualCoin_getBasicSettings")
def test_virtualCoin_getBasicSettings(test_getToken):
    payload1 = {
        "accessToken": test_getToken

    }
    headers ={
        "Content-Type":"application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/shopping-cms-api/virtualCoin/getBasicSettings', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_virtualCoin_getBasicSettings')


if __name__ == "__main__":
    test_virtualCoin_getBasicSettings()
    pytest.main(['-s','test_virtualCoin_getBasicSettings.py'])
