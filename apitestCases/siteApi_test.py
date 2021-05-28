import allure
import pytest

from pageApi.sitePage import SitePage

@allure.feature("站点管理接口")
class TestSite():
    """ 站点管理接口"""
    def setup_class(self):
        self.SitePage = SitePage()

    def teardown_class(self):
        pass

    @allure.story("获取所有站点 Api")
    def test_getsites(self):
        """获取所有站点 正例"""
        result = self.SitePage.getsites()
        print(result)
        assert  result["status"] == 200

    @allure.story("添加站点 Api")
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

    @allure.story("根据条件name获取站点总数 Api")
    def test_getsitecount(self):
        """根据条件name获取站点总数 正例"""
        name = 'f1'
        result = self.SitePage.getsitecount(name=name)
        print(result)
        assert result["status"] == 200
        # assert result["data"] == 1

    @allure.story("根据名称获取站点 Api")
    def test_getsiteByName(self):
        """根据名称获取站点   正例"""
        name = "f1"
        result = self.SitePage.getSiteByName(name=name)
        print(result)
        assert result["status"] == 200
        # assert result['data']['name'] == name

    @allure.story("根据条件获取站点列表（模糊查询） Api")
    def test_querySitePage(self):
        """根据条件获取站点列表（模糊查询）  正例"""
        pageNum = 1
        pageSize = 1
        name = "f1"
        result = self.SitePage.querySitePage(pageNum=pageNum,pageSize=pageSize,name=name)
        print(result)
        assert result["status"] == 200
        # assert result['data']['firstPage'] == 1

    @allure.story("根据条件获取站点列表（模糊查询） Api")
    def test_querySites(self):
        """根据条件获取站点列表（模糊查询） 正例 """
        name = "f"
        result = self.SitePage.querySites(name=name)
        print(result)
        assert result["status"] == 200


    @allure.story("根据ID获取站点 Api")
    @pytest.mark.parametrize("id",[("35405768819740672"),("39293745987858432")])
    def test_getsiteById(self,id):
        """ 根据ID获取站点 正例"""
        # id = "35405768819740672"
        result = self.SitePage.getSiteById(id=id)
        print(result)
        assert result["status"] == 200
        # assert result['data']['id'] == id

    @allure.story("更新站点 Api")
    def test_updatesite(self):
        """更新站点  正例"""

        pre = self.SitePage.addsite(name="fang001")
        print(pre)
        id = pre['data']['id']
        result = self.SitePage.updatesite(id=id,name="meilanzi")
        try:
            self.SitePage.getSiteById(id=id)
        finally:
            self.SitePage.deleteSite(id=id)
        assert result["status"] == 200

    @allure.story("删除站点 Api")
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
















