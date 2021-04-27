import pytest

from pageApi.witServerPage import witServerPage


class Testwitserver:
    """ WitServer管理接口  测试"""
    def setup(self):
        self.witServerPage = witServerPage()


    @pytest.mark.parametrize("pageNum,pageSize",[(1,4)])
    def test_findPage(self,pageNum,pageSize):
        """获取WitServer服务器列表   正例 """
        result = self.witServerPage.findPage(pageNum=pageNum,pageSize=pageSize)
        print(result)
        assert result['status'] == 200
        assert result['data'] != 0
