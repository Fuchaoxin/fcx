# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_virtualCoin_getExpensesPage")
def test_virtualCoin_getExpensesPage():
    payload1 = {
        'accessToken':config.TOKEN,
        "page":{"pageNum": 1,"pageSize":20},
        "content": {
                    "status": "",
                    "operator": ""
                    }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/shopping-cms-api/virtualCoin/getExpensesPage', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_virtualCoin_getExpensesPage')


if __name__ == "__main__":

    pytest.main(['-s','test_virtualCoin_getExpensesPage.py'])
