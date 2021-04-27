import pytest

from pageApi.userPage import userPage


class Testuser:
    """ WitServer 用户管理接口  测试"""
    def setup(self):
        self.userPage = userPage()

    def teardown(self):
        pass

