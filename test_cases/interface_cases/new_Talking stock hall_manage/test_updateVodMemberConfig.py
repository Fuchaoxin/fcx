# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_updateVodMemberConfig")
def test_updateVodMemberConfig():
    payload1 = {
        "accessToken":config.TOKEN,
        "content": {
                'unit': "C",
                'validity': "5"
        }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1=json.dumps(payload1)
    r1 = requests.post(url= config.Pre_Url+'/cms-api/vlogTask/updateVodMemberConfig', data=payload1,headers=headers)

    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_updateVodMemberConfig')


if __name__ == "__main__":
    pytest.main(['-s','test_updateVodMemberConfig.py'])
