# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_school_getList")
def test_school_getList():
    payload1 = {
        'accessToken':config.TOKEN,
        "content": {"schoolName": "",
                    "schoolType": "A"
                    }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url= config.Pre_Url+'/cms-api/edu/school/getList', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_school_getList')


if __name__ == "__main__":

    pytest.main(['-s','test_school_getList.py'])
