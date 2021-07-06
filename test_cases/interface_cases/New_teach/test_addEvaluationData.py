# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_addEvaluationData")
def test_addEvaluationData():
    payload1 = {
        'accessToken':config.TOKEN,
        "content": {
                    'content': "好方法减几分何九华",
                    'courseIdList': ["117219239647121408"],
                    'endTime': "2024-07-31 10:44:41",
                    'idsource': "2",
                    'score': 5,
                    'startTime': "2021-07-13 10:44:38",
                    'userId': "0815c4c9-d45b-427e-8742-b0dae5974546"
                    }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/cms-api/edu/evaluation/addEvaluationData', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_addEvaluationData')


if __name__ == "__main__":
    pytest.main(['-s','test_addEvaluationData.py'])
