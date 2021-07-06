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
import random
import random

class TestCase():
        value=1
        value1=1
        
        @allure.step("接口test_add")
        def test_add(self):
            payload1 = {
                'accessToken':config.TOKEN,
                "content": {
                                'configId': None,
                                'configName': "1111111111",
                                'uiConfig': {
                                    'fragmentList': [
                                    {
                                    'imgUrl': "https://oss.caizidao.com.cn/uat/invest_viewIcon/tjone.png",
                                    'subTitle': "每天学习可以获得积分",
                                    'title': "每日一课111111",
                                    'type': "1"},
                                    {
                                    'imgUrl': "https://oss.caizidao.com.cn/uat/invest_viewIcon/tjDict.png",
                                    'subTitle': "每天进步一点点",
                                    'title': "证券辞典",
                                    'type': "2"},
                                    {
                                    'imgUrl': "https://oss.caizidao.com.cn/uat/invest_viewIcon/tjXTJP.png",
                                    'subTitle': "学过的人这么说",
                                    'title': "名师荟萃",
                                    'type': "5"},
                                    {
                                    'imgUrl': "https://oss.caizidao.com.cn/uat/invest_viewIcon/tjXTJP.png",
                                    'subTitle': "专业课程祝你稳步成功",
                                    'title': "学堂精品",
                                    'type': "3"},
                                    {
                                    'imgUrl': "https://oss.caizidao.com.cn/uat/invest_viewIcon/tjXTJP.png",
                                    'subTitle': "学过的人这么说",
                                    'title': "优评好课",
                                    'type': "4"},
                                    {
                                    'imgUrl': "https://oss.caizidao.com.cn/uat/invest_viewIcon/tjXTJP.png",
                                    'subTitle': "资深名师传授股市秘籍",
                                    'title': "名师课",
                                    'type': "6"}],
                                    'iconList': [{
                                    'icon': "https://oss.caizidao.com.cn/cms/%E9%87%91%E5%88%9A-%E8%AF%BE%E5%A0%82%402x.png",
                                    'name': "麟龙课堂",
                                    'uri': "https://rpdtservice.caizidao.com.cn/order/videoList?llcjdpx=%7Ct_%E9%BA%9F%E9%BE%99%E7%BB%8F%E5%85%B8%E8%AF%BE%7Clb_0%7C"},
                                    {
                                    'icon': "https://oss.caizidao.com.cn/rpdt/invest_educat/dictorykingLive.png",
                                    'name': "互动直播",
                                    'uri': "llczd://xxxxx/m/edu/live?channelId=60ebfbae-3088-483d-91c7-458848bfb92b"},
                                    {
                                    'icon': "https://oss.caizidao.com.cn/rpdt/invest_viewIcon/%E9%87%91%E5%88%9A-%E6%AF%8F%E6%97%A5%E4%B8%80%E8%AF%BE%402x.png",
                                    'name': "每日一课",
                                    'uri': "llczd://xxxx/m/edu/dailyCourse"},
                                    {
                                    'icon': "https://oss.caizidao.com.cn/rpdt/invest_viewIcon/%E9%87%91%E5%88%9A-%E8%82%A1%E7%A5%A8%402x.png",
                                    'name': "股票学堂",
                                    'uri': "llczd://xxxx/m/edu/school?id=117295988217090048"},
                                    {
                                    'icon': "https://oss.caizidao.com.cn/rpdt/invest_viewIcon/%E9%87%91%E5%88%9A-%E5%9F%BA%E9%87%91%402x.png",
                                    'name': "基金学堂",
                                    'uri': "llczd://xxxx/m/edu/school?id=117296168383418368"},
                                    {
                                    'icon': "https://oss.caizidao.com.cn/rpdt/invest_viewIcon/%E9%87%91%E5%88%9A-%E6%9C%9F%E8%B4%A7%402x.png",
                                    'name': "期货学堂",
                                    'uri': "llczd://xxxx/m/edu/school?id=166587402784215040"},
                                    {
                                    'icon': "https://oss.caizidao.com.cn/rpdt/invest_viewIcon/%E9%87%91%E5%88%9A-%E9%BB%84%E9%87%91%402x.png",
                                    'name': "黄金学堂",
                                    'uri': "llczd://xxxx/m/edu/school?id=117296318283649024"},
                                    {
                                    'icon': "https://oss.caizidao.com.cn/rpdt/invest_viewIcon/%E9%87%91%E5%88%9A-%E5%A4%96%E6%B1%87%402x.png",
                                    'name': "外汇学堂",
                                    'uri': "llczd://xxxx/m/edu/school?id=117296404740837376"},
                                    {
                                    'icon': "https://oss.caizidao.com.cn/rpdt/invest_viewIcon/%E9%87%91%E5%88%9A-%E4%BF%9D%E9%99%A9%402x.png",
                                    'name': "保险学堂",
                                    'uri': "llczd://xxxx/m/edu/school?id=117296545887555584"},
                                    {
                                    'icon': "https://oss.caizidao.com.cn/rpdt/invest_viewIcon/%E9%87%91%E5%88%9A-%E7%90%86%E8%B4%A2%402x.png",
                                    'name': "理财学堂",
                                    'uri': "llczd://xxxx/m/edu/school?id=117296613596205056"},
                                    {
                                    'icon': "https://oss.caizidao.com.cn/rpdt/invest_viewIcon/%E9%87%91%E5%88%9A-%E5%85%A8%E9%83%A8%402x.png",
                                    'name': "全部视频",
                                    'uri': "llczd://xxxx/m/edu/allCourse"},
                                    {
                                    'icon': "https://oss.caizidao.com.cn/rpdt/invest_viewIcon/%E9%87%91%E5%88%9A-%E5%90%8D%E5%B8%88%402x.png",
                                    'name': "名师荟萃",
                                    'uri': "llczd://cms/m/edu/lecturerList"},
                                    {
                                    'icon': "https://oss.caizidao.com.cn/pdt/invest_viewIcon/famous_teacher.png",
                                    'name': "名师课",
                                    'uri': "llczd://cms/m/edu/lecturerList"}]}
                            }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url+'/cms-api/edu/ui/add', data=payload1,headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200,'addUI')

        @allure.step("接口test_edu_getList")
        def test_edu_getList(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "page": {"pageNum": 1, "pageSize": 20}
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/edu/ui/getList', data=payload1, headers=headers)
            print(r1.json())
            global value
            value = r1.json()['content']['list'][0]['configId']
            return (value)


        @allure.step("接口test_update")
        def test_update(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'configId': value,
                    'configName': "1111111111",
                    'uiConfig': {
                        'fragmentList': [
                            {
                                'imgUrl': "https://oss.caizidao.com.cn/uat/invest_viewIcon/tjone.png",
                                'subTitle': "每天学习可以获得积分",
                                'title': "每日一课111222",
                                'type': "1"},
                            {
                                'imgUrl': "https://oss.caizidao.com.cn/uat/invest_viewIcon/tjDict.png",
                                'subTitle': "每天进步一点点",
                                'title': "证券辞典",
                                'type': "2"},
                            {
                                'imgUrl': "https://oss.caizidao.com.cn/uat/invest_viewIcon/tjXTJP.png",
                                'subTitle': "学过的人这么说",
                                'title': "名师荟萃",
                                'type': "5"},
                            {
                                'imgUrl': "https://oss.caizidao.com.cn/uat/invest_viewIcon/tjXTJP.png",
                                'subTitle': "专业课程祝你稳步成功",
                                'title': "学堂精品",
                                'type': "3"},
                            {
                                'imgUrl': "https://oss.caizidao.com.cn/uat/invest_viewIcon/tjXTJP.png",
                                'subTitle': "学过的人这么说",
                                'title': "优评好课",
                                'type': "4"},
                            {
                                'imgUrl': "https://oss.caizidao.com.cn/uat/invest_viewIcon/tjXTJP.png",
                                'subTitle': "资深名师传授股市秘籍",
                                'title': "名师课",
                                'type': "6"}],
                        'iconList': [{
                            'icon': "https://oss.caizidao.com.cn/cms/%E9%87%91%E5%88%9A-%E8%AF%BE%E5%A0%82%402x.png",
                            'name': "麟龙课堂",
                            'uri': "https://rpdtservice.caizidao.com.cn/order/videoList?llcjdpx=%7Ct_%E9%BA%9F%E9%BE%99%E7%BB%8F%E5%85%B8%E8%AF%BE%7Clb_0%7C"},
                            {
                                'icon': "https://oss.caizidao.com.cn/rpdt/invest_educat/dictorykingLive.png",
                                'name': "互动直播",
                                'uri': "llczd://xxxxx/m/edu/live?channelId=60ebfbae-3088-483d-91c7-458848bfb92b"},
                            {
                                'icon': "https://oss.caizidao.com.cn/rpdt/invest_viewIcon/%E9%87%91%E5%88%9A-%E6%AF%8F%E6%97%A5%E4%B8%80%E8%AF%BE%402x.png",
                                'name': "每日一课",
                                'uri': "llczd://xxxx/m/edu/dailyCourse"},
                            {
                                'icon': "https://oss.caizidao.com.cn/rpdt/invest_viewIcon/%E9%87%91%E5%88%9A-%E8%82%A1%E7%A5%A8%402x.png",
                                'name': "股票学堂",
                                'uri': "llczd://xxxx/m/edu/school?id=117295988217090048"},
                            {
                                'icon': "https://oss.caizidao.com.cn/rpdt/invest_viewIcon/%E9%87%91%E5%88%9A-%E5%9F%BA%E9%87%91%402x.png",
                                'name': "基金学堂",
                                'uri': "llczd://xxxx/m/edu/school?id=117296168383418368"},
                            {
                                'icon': "https://oss.caizidao.com.cn/rpdt/invest_viewIcon/%E9%87%91%E5%88%9A-%E6%9C%9F%E8%B4%A7%402x.png",
                                'name': "期货学堂",
                                'uri': "llczd://xxxx/m/edu/school?id=166587402784215040"},
                            {
                                'icon': "https://oss.caizidao.com.cn/rpdt/invest_viewIcon/%E9%87%91%E5%88%9A-%E9%BB%84%E9%87%91%402x.png",
                                'name': "黄金学堂",
                                'uri': "llczd://xxxx/m/edu/school?id=117296318283649024"},
                            {
                                'icon': "https://oss.caizidao.com.cn/rpdt/invest_viewIcon/%E9%87%91%E5%88%9A-%E5%A4%96%E6%B1%87%402x.png",
                                'name': "外汇学堂",
                                'uri': "llczd://xxxx/m/edu/school?id=117296404740837376"},
                            {
                                'icon': "https://oss.caizidao.com.cn/rpdt/invest_viewIcon/%E9%87%91%E5%88%9A-%E4%BF%9D%E9%99%A9%402x.png",
                                'name': "保险学堂",
                                'uri': "llczd://xxxx/m/edu/school?id=117296545887555584"},
                            {
                                'icon': "https://oss.caizidao.com.cn/rpdt/invest_viewIcon/%E9%87%91%E5%88%9A-%E7%90%86%E8%B4%A2%402x.png",
                                'name': "理财学堂",
                                'uri': "llczd://xxxx/m/edu/school?id=117296613596205056"},
                            {
                                'icon': "https://oss.caizidao.com.cn/rpdt/invest_viewIcon/%E9%87%91%E5%88%9A-%E5%85%A8%E9%83%A8%402x.png",
                                'name': "全部视频",
                                'uri': "llczd://xxxx/m/edu/allCourse"},
                            {
                                'icon': "https://oss.caizidao.com.cn/rpdt/invest_viewIcon/%E9%87%91%E5%88%9A-%E5%90%8D%E5%B8%88%402x.png",
                                'name': "名师荟萃",
                                'uri': "llczd://cms/m/edu/lecturerList"},
                            {
                                'icon': "https://oss.caizidao.com.cn/pdt/invest_viewIcon/famous_teacher.png",
                                'name': "名师课",
                                'uri': "llczd://cms/m/edu/lecturerList"}]}
                }
            }

            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/edu/ui/update', data=payload1, headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'update')

        @allure.step("接口test_publish")
        def test_publish(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'configId': value
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/edu/ui/publish', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'publish')

        @allure.step("接口test_edu_getList1")
        def test_edu_getList1(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "page": {"pageNum": 1, "pageSize": 20}
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/edu/ui/getList', data=payload1, headers=headers)
            global value1
            value1 = r1.json()['content']['list'][1]['configId']
            return (value1)

        @allure.step("接口test_delete")
        def test_delete(self):
            payload1 = {
                'accessToken': config.TOKEN,
                "content": {
                    'configId': value1
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            payload1 = json.dumps(payload1)
            r1 = requests.post(url=config.Pre_Url + '/cms-api/edu/ui/delete', data=payload1,
                               headers=headers)
            As = AssertUtil()
            As.assert_code(r1.json()['code'], 200, 'delete')


if __name__ == "__main__":
    pytest.main(['-s', 'test_add_edit_deleteUI'])
