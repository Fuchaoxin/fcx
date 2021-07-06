# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_getIconCateList")
def test_getIconCateList():
    payload1 = {
        "accessToken": config.TOKEN

    }
    headers ={
        "Content-Type":"application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/cms-api/iconManage/getIconCateList', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_getIconCateList')


if __name__ == "__main__":

    pytest.main(['-s','test_getIconCateList.py'])
