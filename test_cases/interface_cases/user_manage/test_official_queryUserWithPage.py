# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_official_queryUserWithPage")
def test_official_queryUserWithPage():
    payload1 = {
        'accessToken':config.TOKEN,
        "page":{"pageNum": 1,"pageSize":20},
        "content": {
                    'account': None,
                    'isKol': None,
                    'isLecturer': None,
                    'labourUnionId': None,
                    'memberId': None,
                    'mobileAuthenticated': None,
                    'newUserStatus': None,
                    'nickName': None,
                    'paymentSettings': None,
                    'status': None
                    }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/cms-api/official/queryUserWithPage', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_official_queryUserWithPage')

if __name__ == "__main__":

    pytest.main(['-s','test_official_queryUserWithPage.py'])
