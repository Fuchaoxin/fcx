# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_virtualCoin_manualExpenses")
def test_virtualCoin_manualExpenses():
    payload1 = {
        "accessToken": config.TOKEN,
        "content": {'expensesType': 1, 'amount': 1, 'userIds': ["0815c4c9-d45b-427e-8742-b0dae5974546"],'reason': "测试"}
    }
    headers ={
        "Content-Type":"application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/shopping-cms-api/virtualCoin/manualExpenses', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_virtualCoin_manualExpenses')


if __name__ == "__main__":

    pytest.main(['-s','test_virtualCoin_manualExpenses.py'])
