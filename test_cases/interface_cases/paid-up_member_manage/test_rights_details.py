# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil

@allure.step("接口test_rights_details")
@pytest.mark.parametrize("memberId,expect_result",[(224087069438238720,200),(224087131799150592,200),(224087194227171328,200),(224086997673697280,200),(224086997673697250,200)])
def test_rights_details(memberId,expect_result):
    payload1 = {
        'accessToken':config.TOKEN,
        'content': {
                        'memberId':memberId
                    }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/shopping-cms-api/rights/details', data=payload1,headers=headers)

    As = AssertUtil()
    As.assert_code(r1.json()['code'],expect_result,'test_rights_details')

if __name__ == "__main__":

    pytest.main(['-s','test_rights_details.py'])
