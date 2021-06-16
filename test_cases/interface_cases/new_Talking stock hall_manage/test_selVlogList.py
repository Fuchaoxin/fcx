# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_selVlogList")
def test_selVlogList(test_getToken):
    payload1 = {
        'accessToken':test_getToken,
        "page":{"pageNum": 1,"pageSize":20},
        "content": {
            'account': 'null',
            'beginTime': 'null',
            'endTime': 'null',
            'examineStatus': 'null',
            'labelVOList': 'null',
            'mediaType': 'null',
            'payStatus': 'null',
            'title': 'null',
            'topic': "",
            'words': 'null'
        }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/cms-api/vlogTask/selVlogList', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_selVlogList')


if __name__ == "__main__":
    test_selVlogList()
    pytest.main(['-s','test_selVlogList.py'])
