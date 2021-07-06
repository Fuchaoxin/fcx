# -*- coding: utf-8 -*-
import requests
import pytest
import allure
import json
from base import config
from base.AssertUtil import AssertUtil
@allure.step("接口test_getNotesList")
def test_getNotesList():
    payload1 = {
        'accessToken':config.TOKEN,
        "page":{"pageNum": 0,"pageSize":20},
        "content": {
                    "auditState": "null",
                    "chapterId": "null",
                    "isShow": "null",
                    "notesUpdateStartTime": "null",
                    "notesUpdatesEndTime": "null",
                    "schoolId": "null",
                    "source": "null",
                    "vedioName": ""
                    }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/cms-api/edu/notes/getNotesList', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_getNotesList')


if __name__ == "__main__":

    pytest.main(['-s','test_getNotesList.py'])
