# -*- coding: utf-8 -*-
import requests
import pytest
import os,sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
@pytest.fixture(scope='session')
def test_getToken():
    Token='eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MjM3NDgzMzgsImlhdCI6MTYyMzc0NjUzOCwianRpIjoiYzFmNTBjMzE1YzE5NGM2MzgwOGNlNDBiZTZmZDgyM2QiLCJzdWIiOiJiYWlsaW5neXUifQ.RXCnCxir95kUqCLtjhlBPFWnATGcn-9RYA5Z4gBeMfrqu6wKh14pVcKeHBt9fZEhRAhb97i1MjhR8PLSXS0ScIuVOJMzYw8YLpoXtl1wJv9gDBdn_DvYIaQXIVVn4urnLNkk9QdiWjkj-vj-EGUQCV6EiKT0TE1UXnH4Yyfby3Xxpw_9H60UEUiT6yzscW0_tsvetATtarUp4ffLn8gEzAnocS-dbZ47VjT5dT67EvDXFgmjKccWvvt9evf9KAh6iyz1PJOcp2LTcMD5vr3qWZ3eUywRgS_QmmpIdlWy78yCp-nKx1xD0dd8jbOJOB6INAwFcfdKfvDfSdiyS8DFyg'
    return Token
#test5
# def main():
#     tk = test_getToken()
#     print (tk)
#
#
# if __name__ == "__main__":
#     main()
