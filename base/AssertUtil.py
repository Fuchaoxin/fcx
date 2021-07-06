import json
from base.log import logger

log=logger()

class AssertUtil():
    def __init__(self):
        pass

    def assert_code(self,code,expect_code,def_name):
        try:
            assert code == expect_code
            log.info("%s : actual code=expect code=%s",def_name,code)
            return True
        except:
            log.info("%s : actual code:%s,expect code:%s ",def_name,code, expect_code)
            raise

    def assert_body(self,body,expect_body,def_name):
        try:
            assert body == expect_body
            log.info("%s : actual body=expect body=%s",def_name,body)
            return True
        except:
            log.info("%s :actual body:%s,expect body:%s ",def_name,body, expect_body)
            raise

    def assert_in_body(self,body,expect_body,def_name):
        try:
            body = json.dumps(body)
            assert expect_body in body
            log.info("%s :actual body=expect body=%s",def_name, body)
            return True
        except:
            log.info("%s :body is failed,actual body:%s,expect body:%s ",def_name,body, expect_body)
            raise


