# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_dailyLessonList")
def test_dailyLessonList(test_getToken):
    payload1 = {
        'accessToken':test_getToken,
        "page":{"pageNum": 0,"pageSize":999},
        "content": {
                    "endTime": 1625443199999,
                    "startTime": 1622419200000
                    }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/cms-api/edu/dailyLesson/dailyLessonList', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_dailyLessonList')


if __name__ == "__main__":
    test_dailyLessonList()
    pytest.main(['-s','test_dailyLessonList.py'])
