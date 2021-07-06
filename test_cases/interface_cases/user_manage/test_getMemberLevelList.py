# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_getMemberLevelList")
def test_getMemberLevelList():
    payload1 = {
        "accessToken": config.TOKEN

    }
    headers ={
        "Content-Type":"application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/shopping-cms-api/member/getMemberLevelList', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_getMemberLevelList')


if __name__ == "__main__":

    pytest.main(['-s','test_getMemberLevelList.py'])
