# -*- coding: utf-8 -*-
import requests
import pytest
@pytest.fixture(scope='session')
def test_getToken():
    Token='eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MjMxNDA1NDksImlhdCI6MTYyMzEzODc0OSwianRpIjoiYjU5NzhiZDhlMWI2NGQ5NjgxMWZmYzA2NWM0MmU0YTgiLCJzdWIiOiJiYWlsaW5neXUifQ.pmHuPDUZpAokXGXokGUsirFQ4LVS7v8IiC3n8RtNooU_vPVvPbvge3UCoVH6mMoFD7bQCLO3A0ooNo5t7Bh4-87iZPA595wj4jxe-DpbWHgrvOeNj3x_mm2GWMIitSDgV-HshT7PgEsrlGkOQbSfoUtGMl5liaiUcAMWNb-tdHxYa5_iE_d67CGKaHXqTYpOL_qKLRh_H599Ge7zaBGFLbfKiUNgC8jyMB6Xq4LuC0bOKd1TlPds_CPZVlnBATjZABEherliBDNPsoP0Yw651yjm2ffBTNiGZ6Tfb7hqwvn1YYHEGfftVhUPUI738WZJHixhtN2V9XrIPWOCZ6HzNA'
    return Token
#test4
# def main():
#     tk = test_getToken()
#     print (tk)
#
#
# if __name__ == "__main__":
#     main()
