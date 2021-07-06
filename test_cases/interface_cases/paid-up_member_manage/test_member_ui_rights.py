# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil

@allure.step("接口member_ui_rights")
@pytest.mark.parametrize("rightsDescription,rightsId,expect_result",[("早晚盘推送",1,200),("免费解锁邀请返利",10,200),("免费解锁人工诊股",2,200),("免费解锁AI诊股",227360371624820736,200),("免费解锁开户优惠",227512405401452544,200),("畅想付费视频",229540678701694976,200),("保险赠送",3,200),("投顾课程",4,200),("名师面对面",5,200),("尊享身份标识",6,200),("专享主页皮肤",7,200),("昵称特效",8,200),("付费资讯",9,200)])
def test_member_ui_rights(rightsDescription,rightsId,expect_result):
    payload1 = {
        'accessToken':config.TOKEN,
        'content': {
                        'images':["http://oss.caizidao.com.cn/rpdt/member_manage/5.png","http://oss.caizidao.com.cn/rpdt/member_manage/1.png","https://oss.caizidao.com.cn/rpdt/member_manage/480X.png"],
                        'memberCodes':["1000003", "1000004", "1000005"],
                        'rightsDescription':rightsDescription,
                        'rightsIcon':None,
                        'rightsId':rightsId,
                        'rightsSubtitle':"优享会员以上可享"
                    }
    }
    headers = {
        "Content-Type": "application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/shopping-cms-api/member/ui/rights', data=payload1,headers=headers)

    As = AssertUtil()
    As.assert_code(r1.json()['code'],expect_result,'test_member_ui_rights')

if __name__ == "__main__":

    pytest.main(['-s','test_member_ui_rights.py'])
