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

class TestCase():
        value=1
        value1=1
        
        @allure.step("接口test_addOrUpdHomePageManage")
        def test_addOrUpdHomePageManage(self):
            payload1 = {
                        'accessToken':config.TOKEN,
                        'content': {
                                    'homePageAdvertisings': [
                                    {
                                    'iconUri': "",
                                    'iconUrl': "",
                                    'lickAccount1': {
                                                        'account': "10005573",
                                                        'countryCode': "86",
                                                        'imageUrl': "http://oss.caizidao.com.cn/pdt/head_portrait/ab53d2da-e4a9-4cb6-a182-411ca82fa3f8/1595914913810.jpeg",
                                                        'isKol': 0,
                                                        'labourUnionId': None,
                                                        'labourUnionName': None,
                                                        'lecturerHeadImg': None,
                                                        'lecturerId': None,
                                                        'mobile': "185****4157",
                                                        'nickName': "小财米_CP4157",
                                                        'realName': None,
                                                        'tipName': "小财米_CP4157",
                                                        'userId': "93bfbfe4-5cf8-4e02-a113-0bcf1d2c0abf",
                                                        'userInfoId': 8069,
                                                        'userType': 3
                                                    },
                                    'lickAccount2': {
                                                        'account': "10000848",
                                                        'countryCode': "86",
                                                        'imageUrl': "http://thirdqq.qlogo.cn/g?b=oidb&k=OJFCadPFUeNODia7SY4aYyA&s=40&t=1554978927",
                                                        'isKol': 0,
                                                        'labourUnionId': None,
                                                        'labourUnionName': None,
                                                        'lecturerHeadImg': None,
                                                        'lecturerId': 3679,
                                                        'mobile': "135****3107",
                                                        'nickName': "Daisy",
                                                        'realName': "高超",
                                                        'tipName': "Daisy",
                                                        'userId': "94c62ab1-80a0-4a68-a1b5-aa1009a8eccd",
                                                        'userInfoId': 8193,
                                                        'userType': 3
                                                    },
                                    'lickAccount3': {
                                                        'account': "10009685",
                                                        'countryCode': "86",
                                                        'imageUrl': "http://thirdqq.qlogo.cn/g?b=oidb&k=CFfXLHWLBhqYunudEkX0ibg&s=40&t=1555531102",
                                                        'isKol': 0,
                                                        'labourUnionId': None,
                                                        'labourUnionName': None,
                                                        'lecturerHeadImg': None,
                                                        'lecturerId': None,
                                                        'mobile': "182****5020",
                                                        'nickName': "Cc",
                                                        'realName': None,
                                                        'tipName': "Cc",
                                                        'userId': "fac9ad02-afa4-4920-b859-75e09381975d",
                                                        'userInfoId': 7969,
                                                        'userType': 3
                                                    },
                                    'rankPersuserDataListon': [],
                                    'rankingName': "1234567899",
                                    'sortNum': "",
                                    'type': "1",
                                    'userDataList': [{
                                                        'account': "10005573",
                                                        'imageUrl': "http://oss.caizidao.com.cn/pdt/head_portrait/ab53d2da-e4a9-4cb6-a182-411ca82fa3f8/1595914913810.jpeg",
                                                        'nickName': "小财米_CP4157"},
                                                      {
                                                      'account': "10000848",
                                                      'imageUrl': "http://thirdqq.qlogo.cn/g?b=oidb&k=OJFCadPFUeNODia7SY4aYyA&s=40&t=1554978927",
                                                      'nickName': "Daisy"},
                                                      {
                                                      'account': "10009685",
                                                      'imageUrl': "http://thirdqq.qlogo.cn/g?b=oidb&k=CFfXLHWLBhqYunudEkX0ibg&s=40&t=1555531102",
                                                      'nickName': "Cc"}],
                                    'userIdMore': "93bfbfe4-5cf8-4e02-a113-0bcf1d2c0abf,94c62ab1-80a0-4a68-a1b5-aa1009a8eccd,fac9ad02-afa4-4920-b859-75e09381975d",
                                    'userIds': ""}],
                                    'homePageOptions': [
                                                        {
                                                        'iconUri': "llczd://www.linlong.com/m/quota/techSearch?indicators=%5B%7B%22id%22:%22K%22,%22name%22:%22K%E7%BA%BF%22%7D,%7B%22name%22:%22%E6%88%90%E4%BA%A4%E9%87%8F%22,%22id%22:%22VOL%22%7D,%7B%22name%22:%22%E5%B9%B3%E6%BB%91%E5%BC%82%E5%90%8C%E7%A7%BB%E5%8A%A8%E5%B9%B3%E5%9D%87%E7%BA%BF%22,%22id%22:%22MACD%22%7D%5D",
                                                        'iconUrl': "http://oss.caizidao.com.cn/uat/appManage_iconImg/%E6%8A%80%E6%9C%AF%E5%88%86%E6%9E%90.png",
                                                        'optionName': "技术分析",
                                                        'sortNum': None},
                                                        {
                                                        'iconUri': "llczd://xxxx/m/quota/diagnosisstock",
                                                        'iconUrl': "http://oss.caizidao.com.cn/uat/appManage_iconImg/AI%E8%AF%8A%E8%82%A1.png",
                                                        'optionName': "AI诊股",
                                                        'sortNum': None},
                                                        {
                                                        'iconUri': "https://www.jinjiwo.com/accountcenter/static/app/download.html?open=browser&llcjdpx=%7Ct_%E9%87%91%E5%9F%BA%E7%AA%9D%7Clb_1%7C",
                                                        'iconUrl': "http://oss.caizidao.com.cn/uat/appManage_iconImg/%E5%9F%BA%E9%87%91.png",
                                                        'optionName': "基金",
                                                        'sortNum': None},
                                                        {
                                                        'iconUri': "https://rpdtservice.caizidao.com.cn/order/noviceCeremony/inviteFriends?llcjdpx=|t_",
                                                        'iconUrl': "http://oss.caizidao.com.cn/uat/appManage_iconImg/%E9%82%80%E8%AF%B7%E6%9C%89%E7%A4%BC.png",
                                                        'optionName': "邀请有礼",
                                                        'sortNum': None},
                                                        {
                                                        'description': "APP位置-我的-消息中心页",
                                                        'iconUri': "llczd://www.services.czd.com.cn/m/mine/message",
                                                        'iconUrl': "https://oss.caizidao.com.cn/rpdt/appManage_iconImg/160X160.png",
                                                        'optionName': "12345"}
                                    ],
                                    'recordName': "1111111111"
            }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/infoManage/addOrUpdHomePageManage', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'test_addOrUpdHomePageManage')

        @allure.step("接口test_selHomePageManageList")
        def test_selHomePageManageList(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "page": {"pageNum": 1, "pageSize": 20}
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/infoManage/selHomePageManageList', data=payload1,
                               headers=headers)
            global value
            value=r1.json()['content']['list'][0]['recordId']
            global value1
            value1 = r1.json()['content']['list'][1]['recordId']
            return(value)
            return(value1)

        @allure.step("接口test_addOrUpdHomePageManage")
        def test_addOrUpdHomePageManage(self):
            payload1 = {
                'accessToken': config.TOKEN,
                'content': {
                    'homePageAdvertisings': [
                        {
                            'iconUri': "",
                            'iconUrl': "",
                            'lickAccount1': {
                                'account': "10005573",
                                'countryCode': "86",
                                'imageUrl': "http://oss.caizidao.com.cn/pdt/head_portrait/ab53d2da-e4a9-4cb6-a182-411ca82fa3f8/1595914913810.jpeg",
                                'isKol': 0,
                                'labourUnionId': None,
                                'labourUnionName': None,
                                'lecturerHeadImg': None,
                                'lecturerId': None,
                                'mobile': "185****4157",
                                'nickName': "小财米_CP4157",
                                'realName': None,
                                'tipName': "小财米_CP4157",
                                'userId': "93bfbfe4-5cf8-4e02-a113-0bcf1d2c0abf",
                                'userInfoId': 8069,
                                'userType': 3
                            },
                            'lickAccount2': {
                                'account': "10000848",
                                'countryCode': "86",
                                'imageUrl': "http://thirdqq.qlogo.cn/g?b=oidb&k=OJFCadPFUeNODia7SY4aYyA&s=40&t=1554978927",
                                'isKol': 0,
                                'labourUnionId': None,
                                'labourUnionName': None,
                                'lecturerHeadImg': None,
                                'lecturerId': 3679,
                                'mobile': "135****3107",
                                'nickName': "Daisy",
                                'realName': "高超",
                                'tipName': "Daisy",
                                'userId': "94c62ab1-80a0-4a68-a1b5-aa1009a8eccd",
                                'userInfoId': 8193,
                                'userType': 3
                            },
                            'lickAccount3': {
                                'account': "10009685",
                                'countryCode': "86",
                                'imageUrl': "http://thirdqq.qlogo.cn/g?b=oidb&k=CFfXLHWLBhqYunudEkX0ibg&s=40&t=1555531102",
                                'isKol': 0,
                                'labourUnionId': None,
                                'labourUnionName': None,
                                'lecturerHeadImg': None,
                                'lecturerId': None,
                                'mobile': "182****5020",
                                'nickName': "Cc",
                                'realName': None,
                                'tipName': "Cc",
                                'userId': "fac9ad02-afa4-4920-b859-75e09381975d",
                                'userInfoId': 7969,
                                'userType': 3
                            },
                            'rankPersuserDataListon': [],
                            'rankingName': "1234567899",
                            'sortNum': "",
                            'type': "1",
                            'userDataList': [{
                                'account': "10005573",
                                'imageUrl': "http://oss.caizidao.com.cn/pdt/head_portrait/ab53d2da-e4a9-4cb6-a182-411ca82fa3f8/1595914913810.jpeg",
                                'nickName': "小财米_CP4157"},
                                {
                                    'account': "10000848",
                                    'imageUrl': "http://thirdqq.qlogo.cn/g?b=oidb&k=OJFCadPFUeNODia7SY4aYyA&s=40&t=1554978927",
                                    'nickName': "Daisy"},
                                {
                                    'account': "10009685",
                                    'imageUrl': "http://thirdqq.qlogo.cn/g?b=oidb&k=CFfXLHWLBhqYunudEkX0ibg&s=40&t=1555531102",
                                    'nickName': "Cc"}],
                            'userIdMore': "93bfbfe4-5cf8-4e02-a113-0bcf1d2c0abf,94c62ab1-80a0-4a68-a1b5-aa1009a8eccd,fac9ad02-afa4-4920-b859-75e09381975d",
                            'userIds': ""}],
                    'homePageOptions': [
                        {
                            'iconUri': "llczd://www.linlong.com/m/quota/techSearch?indicators=%5B%7B%22id%22:%22K%22,%22name%22:%22K%E7%BA%BF%22%7D,%7B%22name%22:%22%E6%88%90%E4%BA%A4%E9%87%8F%22,%22id%22:%22VOL%22%7D,%7B%22name%22:%22%E5%B9%B3%E6%BB%91%E5%BC%82%E5%90%8C%E7%A7%BB%E5%8A%A8%E5%B9%B3%E5%9D%87%E7%BA%BF%22,%22id%22:%22MACD%22%7D%5D",
                            'iconUrl': "http://oss.caizidao.com.cn/uat/appManage_iconImg/%E6%8A%80%E6%9C%AF%E5%88%86%E6%9E%90.png",
                            'optionName': "技术分析",
                            'sortNum': None},
                        {
                            'iconUri': "llczd://xxxx/m/quota/diagnosisstock",
                            'iconUrl': "http://oss.caizidao.com.cn/uat/appManage_iconImg/AI%E8%AF%8A%E8%82%A1.png",
                            'optionName': "AI诊股",
                            'sortNum': None},
                        {
                            'iconUri': "https://www.jinjiwo.com/accountcenter/static/app/download.html?open=browser&llcjdpx=%7Ct_%E9%87%91%E5%9F%BA%E7%AA%9D%7Clb_1%7C",
                            'iconUrl': "http://oss.caizidao.com.cn/uat/appManage_iconImg/%E5%9F%BA%E9%87%91.png",
                            'optionName': "基金",
                            'sortNum': None},
                        {
                            'iconUri': "https://rpdtservice.caizidao.com.cn/order/noviceCeremony/inviteFriends?llcjdpx=|t_",
                            'iconUrl': "http://oss.caizidao.com.cn/uat/appManage_iconImg/%E9%82%80%E8%AF%B7%E6%9C%89%E7%A4%BC.png",
                            'optionName': "邀请有礼",
                            'sortNum': None},
                        {
                            'description': "APP位置-我的-消息中心页",
                            'iconUri': "llczd://www.services.czd.com.cn/m/mine/message",
                            'iconUrl': "https://oss.caizidao.com.cn/rpdt/appManage_iconImg/160X160.png",
                            'optionName': "12345"}
                    ],
                    'recordId': value,
                    'recordName': "111111222"
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/infoManage/addOrUpdHomePageManage', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'test_addOrUpdHomePageManage')

        @allure.step("接口test_updReleaseHomePageManage")
        def test_updReleaseHomePageManage(self):
            payload1 = {
                'accessToken': config.TOKEN,
                'content':value
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/infoManage/updReleaseHomePageManage', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'test_updReleaseHomePageManage')


        @allure.step("接口test_delHomePageManage")
        def test_delHomePageManage(self):
                payload1 = {
                            'accessToken': config.TOKEN,
                            "content": [value1]
                }
                headers = {
                            "Content-Type": "application/json"
                            }
                payload1 = json.dumps(payload1)
                r1 = requests.post(url=config.Pre_Url + '/cms-api/infoManage/delHomePageManage', data=payload1,
                               headers=headers)
                As = AssertUtil()
                As.assert_code(r1.json()['code'], 200, 'delHomePageManage')

if __name__ == "__main__":
    pytest.main(['-s', 'test_add_edit_delete_publishHomePage'])
