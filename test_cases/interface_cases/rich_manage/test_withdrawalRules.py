# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_withdrawalRules")
def test_withdrawalRules():
    payload1 = {
        'accessToken':config.TOKEN,
        "content": {
                    'maxAmount':299,
                    'minAmount': 1,
                    'withdrawalInstructions':"1、财蛋满500才可发起提现，每日限一次；\r\n2、只可提现以元为单位的整数金额，每月最高提现额度：500元，月内超过500的金额按20%上税（系统代扣）；\r\n3、提现到账时间：提现成功后一般将在1-3个工作日到账；如逾期未到账，请查询银行卡出入账明细和个人中心余额是否有退回；\r\n4、为保障您的财产安全只能使用本人身份证登记的银行卡。"
                    }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/shopping-cms-api/withdrawal/withdrawalRules', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_withdrawalRules')


if __name__ == "__main__":

    pytest.main(['-s','test_withdrawalRules.py'])
