import pytest

from pageApi.sitePage import SitePage

class TestSite():
    def setup(self):
        self.SitePage = SitePage()

    def teardown(self):
        pass

    def test_getsites(self):
        """获取所有站点 正例"""
        result = self.SitePage.getsites()
        print(result)
        assert  result["status"] == 200

    def test_addsite(self):
        """添加站点， name=fang001 正例"""
        name = "fang001"
        result = self.SitePage.addsite(name=name)
        print(result)
        id = result['data']['id']
        try:
            self.SitePage.getSiteById(id=id)
        finally:
            self.SitePage.deleteSite(id=id)

        assert  result["status"] == 200
        assert  result['data']['name'] == "fang001"


    def test_getsitecount(self):
        """根据条件name获取站点总数 正例"""
        name = 'f1'
        result = self.SitePage.getsitecount(name=name)
        print(result)
        assert result["status"] == 200
        assert result["data"] == 1


    def test_getsiteByName(self):
        """根据名称获取站点   正例"""
        name = "f1"
        result = self.SitePage.getSiteByName(name=name)
        print(result)
        assert result["status"] == 200
        assert result['data']['name'] == name

    def test_querySitePage(self):
        """根据条件获取站点列表（模糊查询）  正例"""
        pageNum = 1
        pageSize = 1
        name = "f1"
        result = self.SitePage.querySitePage(pageNum=pageNum,pageSize=pageSize,name=name)
        print(result)
        assert result["status"] == 200
        assert result['data']['firstPage'] == 1

    def test_querySites(self):
        """根据条件获取站点列表（模糊查询） 正例 """
        name = "f"
        result = self.SitePage.querySites(name=name)
        print(result)
        assert result["status"] == 200

    @pytest.mark.parametrize("id",[("35405768819740672"),("39293745987858432")])
    def test_getsiteById(self,id):
        """ 根据ID获取站点 正例"""
        # id = "35405768819740672"
        result = self.SitePage.getSiteById(id=id)
        print(result)
        assert result["status"] == 200
        assert result['data']['id'] == id

    def test_updatesite(self):
        """更新站点  正例"""
        updatename = "meilanzi"
        id = "39664501213114368"
        result = self.SitePage.updatesite(id=id,name=updatename)
        print(result)
        assert result["status"] == 200


    def test_deletesite(self):
        """删除站点  正例"""
        name = "meilanzi"
        try:
            self.SitePage.getSiteByName(name=name)
        finally:
            r = self.SitePage.addsite(name=name)
            id = r["data"]["id"]

        result = self.SitePage.deleteSite(id=id)
        print(result)
        assert result["status"] == 200
















