# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
from test_cases.interface_cases import conftest
import time
import random


@allure.step("接口test_addTopicData")
def test_addTopicData():
    payload1 = {
        'accessToken': config.TOKEN,
        "content": {
                        'id': None,
                        'stockIds': [],
                        'topicBackground': "https://oss.caizidao.com.cn/rpdt/topic_banner_image/1625034038268750X800.png",
                        'topicDescribe': "11111111111111111111111111111111111111111111111111111111111",
                        'topicImage': "https://oss.caizidao.com.cn/rpdt/topic_image/1625034011009200X200.png",
                        'topicName': "test"+str(random.randint(11111,9999999)),
                        'topicStyleId': 4
                    }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url + '/cms-api/topicTask/addTopicData', data=payload1,
                       headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200, 'addTopicData')

if __name__ == "__main__":
    pytest.main(['-s', 'test_addTopicData'])
