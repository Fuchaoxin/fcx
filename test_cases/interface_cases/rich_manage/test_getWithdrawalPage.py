# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_getWithdrawalPage")
@pytest.mark.parametrize("endTime,startTime,userId,status,expect_result",[(None,None,None,None,200),("2021-03-01 23:59:59","2021-02-01 00:00:00","24dee3bf-b1c4-4f24-bf7b-19e20e4e126e",1,200),("2021-03-01 23:59:59","2021-02-01 00:00:00","24dee3bf-b1c4-4f24-bf7b-19e20e4e126e",0,200),("2021-03-01 23:59:59","2021-02-01 00:00:00","24dee3bf-b1c4-4f24-bf7b-19e20e4e126e",2,200),("2021-03-01 23:59:59","2021-02-01 00:00:00","24dee3bf-b1c4-4f24-bf7b-19e20e4e126e",3,200)])
def test_getWithdrawalPage(test_getToken,endTime,startTime,userId,status,expect_result):
    payload1 = {
        'accessToken':test_getToken,
        "page":{"pageNum": 1,"pageSize":20},
        "content": {
                    'endTime': endTime,
                    'startTime': startTime,
                    'status': status,
                    'userId':userId
                    }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/shopping-cms-api/withdrawal/getWithdrawalPage', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_getWithdrawalPage')


if __name__ == "__main__":
    test_getWithdrawalPage()
    pytest.main(['-s','test_getWithdrawalPage.py'])
