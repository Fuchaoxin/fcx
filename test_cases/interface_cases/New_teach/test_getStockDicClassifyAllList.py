# -*- coding: utf-8 -*-
import requests
import pytest
import allure
import json
from base import config
from base.AssertUtil import AssertUtil
@allure.step("接口test_getStockDicClassifyAllList")
def test_getStockDicClassifyAllList(test_getToken):
    payload1 = {
        "accessToken": test_getToken

    }
    headers ={
        "Content-Type":"application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/cms-api/stockDicManage/getStockDicClassifyAllList', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_getStockDicClassifyAllList')


if __name__ == "__main__":
    test_getStockDicClassifyAllList()
    pytest.main(['-s','test_getStockDicClassifyAllList.py'])
