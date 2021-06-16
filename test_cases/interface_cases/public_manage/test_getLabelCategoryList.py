# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_getLabelCategoryList")
def test_getLabelCategoryList(test_getToken):
    payload1 = {
        "accessToken": test_getToken,
        "content": {"labelId": "null",
        "labelLevel": 1,
        "labelName": "",
        "userName": "bailingyu"}
    }
    headers ={
        "Content-Type":"application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/cms-api/labelCategoryManage/getLabelCategoryList', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_getLabelCategoryList')


if __name__ == "__main__":
    test_getLabelCategoryList()
    pytest.main(['-s','test_getLabelCategoryList.py'])
