# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_kol_findSelectUserType")
def test_kol_findSelectUserType():
    payload1 = {
        'accessToken':config.TOKEN,
        "content": {"page":{"pageNum": 0,"pageSize":20},
                    'userTypeValueList': [3, 4]
                    }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/cms-api/kol/findSelectUserType', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_kol_findSelectUserType')


if __name__ == "__main__":

    pytest.main(['-s','test_kol_findSelectUserType.py'])
