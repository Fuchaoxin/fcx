# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil

@allure.step("接口test_getIncomeExpensesPage")
def test_getIncomeExpensesPage(test_getToken):
    payload1 = {
        'accessToken':test_getToken,
        "page":{"pageNum": 1,"pageSize":20},
        "content": {
                    "status": "",
                    "phone": ""
                    }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/shopping-cms-api/virtualCoin/getIncomeExpensesPage', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_getIncomeExpensesPage')


if __name__ == "__main__":
    test_getIncomeExpensesPage()
    pytest.main(['-s','test_getIncomeExpensesPage.py'])