# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from base import config
import json
from base.AssertUtil import AssertUtil
@allure.step("接口test_updateBasicSetting")
def test_updateBasicSetting():
    payload1 = {
        "accessToken": config.TOKEN,
        "content": {
            'model': {
                'clear': 'false',
                'clearRule': 3,
                'dailyLimit': 0,
                'deductionAmount': 100,
                'deductionInstructions': "1、100财蛋抵扣1元人民币，每单可用财蛋100%抵扣订单金额；\n2、消费时可使用财蛋的数量是100的整数倍；\n3、如果拥有的财蛋数量小于100个，则不可在结算页或收银台使用财蛋支付；\n4、用户退换货后，需扣除相应的财蛋，如账户财蛋已使用，则商品退款金额扣除相应现金；\n5、为保证您的资产安全，即日起，财蛋支付功能仅限实名认证用户使用。",
                'deductionRatio': 100,
                'instructions': "1、虚拟币仅可在财咨道app内使用；\r\n2、虚拟币可直接用于支付财咨道内的消费订单；\r\n3、虚拟币可以提现；\r\n4、用户获得但未使用的虚拟币，将在下一个自然年底过期作废；\r\n5、使用虚拟币支付的订单发生退货时，如虚拟币退回时已过有效期，则直接进行作废，不再返回",
                'protection': "1",
                'shoppingThreshold': 1,
                'withdrawalThreshold': 500
            },

            'taskItems': [
            {
            'amount': "99999999",
            'amountList': None,
            'coinAndYuan': None,
            'enabled': 'true',
            'introduction': "每日限领5次，审核通过后立得",
            'limitAmount': 4,
            'status': 0,
            'taskId': 1009,
            'taskName': '发布视频',
            'taskTypeId': 4
            },
            {
            'amount': None,
            'amountList': None,
            'coinAndYuan': {'coins': 1, 'yuan': 1},
            'enabled': 'true',
            'introduction': "每消费2元立得2个财蛋",
            'limitAmount': None,
            'status': "0",
            'taskId': 1010,
            'taskName': "购买视频",
            'taskTypeId': 3},
            {
            'amount': "3",
            'amountList': None,
            'coinAndYuan': None,
            'enabled': 'true',
            'introduction': "关注用户",
            'limitAmount': "3",
            'status': "0",
            'taskId': 1011,
            'taskName': "关注用户",
            'taskTypeId': 14},
            {
            'amount': "7",
            'amountList': None,
            'coinAndYuan': None,
            'enabled': 'true',
            'introduction': "评论点赞",
            'limitAmount': "7",
            'status': "0",
            'taskId': 1012,
            'taskName': "点赞",
            'taskTypeId': 15},
             {
            'amount': None,
            'amountList': [2, 10, 5, 3, 10, 22, 44],
            'coinAndYuan': None,
            'enabled': 'true',
            'introduction': "连续签到7天",
            'limitAmount': None,
            'status': "0",
            'taskId': 1013,
            'taskName': "签到",
            'taskTypeId': 16},
             {
            'amount': "9",
            'amountList': None,
            'coinAndYuan': None,
            'enabled': 'true',
            'introduction': "首次绑定手机号",
            'limitAmount': "1",
            'status': "0",
            'taskId': 1031,
            'taskName': "手机号验证",
            'taskTypeId': 31},
            {
            'amount': "678",
            'amountList': None,
            'coinAndYuan': None,
            'enabled': 'true',
            'introduction': "完善实名身份信息",
            'limitAmount': "1",
            'status': "0",
            'taskId': 1032,
            'taskName': "身份信息（实名）",
            'taskTypeId': 32},
            {
            'amount': "8",
            'amountList': None,
            'coinAndYuan': None,
            'enabled': 'true',
            'introduction': "首次上传头像",
            'limitAmount': "1",
            'status': "0",
            'taskId': 1033,
            'taskName': "上传头像111",
            'taskTypeId': 33}
            ,{
            'amount': "4",
            'amountList': None,
            'coinAndYuan': None,
            'enabled': 'true',
            'introduction': "首次修改昵称",
            'limitAmount': "1",
            'status': "0",
            'taskId': 1034,
            'taskName': "修改昵称",
            'taskTypeId': 34}
            , {
            'amount': "44",
            'amountList': None,
            'coinAndYuan': None,
            'enabled': 'true',
            'introduction': "首次完善个人签名",
            'limitAmount': "1",
            'status': "0",
            'taskId': 1035,
            'taskName': "完善个人签名",
            'taskTypeId': 35}
            , {
            'amount': "90",
            'amountList': None,
            'coinAndYuan': None,
            'enabled': 'true',
            'introduction': "填写地区",
            'limitAmount': "1",
            'status': "0",
            'taskId': 1036,
            'taskName': "填写地区",
            'taskTypeId': 36}
            ,{
            'amount': "5",
            'amountList': None,
            'coinAndYuan': None,
            'enabled': 'true',
            'introduction': "首次填写生日",
            'limitAmount': "1",
            'status': "0",
            'taskId': 1037,
            'taskName': "填写生日",
            'taskTypeId': 37}
            ,{
            'amount': "45",
            'amountList': None,
            'coinAndYuan': None,
            'enabled': 'true',
            'introduction': "首次填写工作信息",
            'limitAmount': "1",
            'status': "0",
            'taskId': 1038,
            'taskName': "填写工作信息",
            'taskTypeId': 38}]
        }
    }
    headers ={
        "Content-Type":"application/json"
    }
    payload1 = json.dumps(payload1)
    r1 = requests.post(url=config.Pre_Url+'/shopping-cms-api/virtualCoin/updateBasicSettings', data=payload1,headers=headers)
    As = AssertUtil()
    As.assert_code(r1.json()['code'], 200,'test_updateBasicSetting')


if __name__ == "__main__":

    pytest.main(['-s','test_updateBasicSetting.py'])



