# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_template_getJobs")
def test_template_getJobs():
    payload1 = {
        'accessToken':config.TOKEN,
        'appId': "cms",
        'enable': 1,
        'operator': "",
        'pageNum': 1,
        'pageSize': 20,
        'status': None,
        'tagType': None,
        'targetUser': [],
        'uid': None
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "false"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/cms-api/template/getJobs', data=payload1,headers=headers)

    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_template_getJobs')


if __name__ == "__main__":

    pytest.main(['-s','test_template_getJobs.py'])
