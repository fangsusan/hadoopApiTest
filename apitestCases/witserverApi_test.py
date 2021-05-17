import pytest
import allure
from pageApi.witServerPage import witServerPage

@allure.feature('witserver 管理接口模块 测试')
class Testwitserver:
    """ WitServer管理接口  测试"""
    def setup(self):
        self.witServerPage = witServerPage()

    @allure.story('获取WitServer服务器列表   正例')
    @pytest.mark.parametrize("pageNum,pageSize",[(1,4)])
    def test_findPage(self,pageNum,pageSize):
        """获取WitServer服务器列表   正例 """
        result = self.witServerPage.findPage(pageNum=pageNum,pageSize=pageSize)
        print(result)
        assert result['status'] == 200
        assert result['data'] != 0
