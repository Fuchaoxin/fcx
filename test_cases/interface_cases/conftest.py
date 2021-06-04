# -*- coding: utf-8 -*-
import requests
import pytest
@pytest.fixture(scope='session')
def test_getToken():
    Token='eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MjI2MjY2ODcsImlhdCI6MTYyMjYyNDg4NywianRpIjoiMmVjZmY1NTM5ZDMwNDA2NmFmYWQxODQ4ZjhkZjk5ZjUiLCJzdWIiOiJiYWlsaW5neXUifQ.t6OHe9fxlgarAmKkfsRKgPxhezuA9ffPUFh9H5AZT1jcD7a2lmeZZyuq23_uUZZwUi_dz_8v0PPd_fzgLDncPY_Lq5OePJtS9_uSw_8N-GV0Ljlh9yirrrSzHAC9V4lOZMeokUp1D0DcUprjhmKOV5TudaqskF7CG_NHFFP0r6u8S6vscuCO4-M61UY7E2Q4th9GUyeKiw1IUcKGe4sCr8oJQFBSCe0QOXorp6-kI9O7IGw5IFn31eejGAqsC33atJKzOXza6B59k0ie2Apz0K33krnMoeafc3A7YYxLP1yxoPHzcPPmngFvQ50xZ8xjw6nTR635YBFk9YaivlAj0A'
    return Token

# def main():
#     tk = test_getToken()
#     print (tk)
#
#
# if __name__ == "__main__":
#     main()
