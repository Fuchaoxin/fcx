# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_addNotes")
def test_addNotes():
    payload1 = {
        'accessToken':config.TOKEN,
        "content": {
                    'courseIdList': ["117219239647121408"],
                    'notesContent': "11111111111111111111111111111111111111",
                    'recordTime': "2021-07-26T01:59:21.000Z",
                    'source': "2",
                    'title': "1111111111111111111",
                    'userId': "30e731a3-1eaa-4a7b-a477-958e7120425a"
                    }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/cms-api/edu//notes/addNotes', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_addNotes')


if __name__ == "__main__":

    pytest.main(['-s','test_addNotes.py'])
