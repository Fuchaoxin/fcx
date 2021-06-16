# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_material_getList")
def test_material_getList(test_getToken):
    payload1 = {
        'accessToken':test_getToken,
        'pageNum': 0,
        'pageSize': 20,
        'txt': ""
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization":"false"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/cms-api/material/getList', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_material_getList')

if __name__ == "__main__":
    test_material_getList()
    pytest.main(['-s','test_material_getList.py'])
