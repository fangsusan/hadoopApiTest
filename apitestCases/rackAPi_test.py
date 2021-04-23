import pytest

from pageApi.tackPage import TackPage


class Testrack():

    def setup(self):
        self.tackPage = TackPage()

    def teardown(self):
        pass

    def test_getracks(self):
        """ 获取所有机架  正例"""
        result = self.tackPage.getRacks()

        print(result)
        assert result["status"] == 200

    @pytest.mark.parametrize("name,siteId",[("meilanzi001","123456789"),("meilanzi002","12345678")])
    def test_addrack(self,name,siteId):
        """ 添加机架  正例"""
        result = self.tackPage.addRacks(name=name,siteId=siteId)
        id = result["data"]["id"]
        try:
            self.tackPage.getRackByName(name=name)
        finally:
            self.tackPage.deleteRack(id=id)
        print(result)
        assert result["status"] == 200
        assert result["data"]["name"] == name
        assert result["data"]["siteId"] == siteId

    def test_getrackcount(self):
        """根据条件name获取站点总数  正例"""
        name = "meilanzi"
        result = self.tackPage.getRackCount(name=name)
        assert result["status"] == 200


    def test_getrackByName(self):
        """ 根据名称获取机架   正例"""
        name = "meilanzi"
        result = self.tackPage.getRackByName(name=name)
        assert result["status"] == 200
        assert result['data']["name"] == name

    def test_queryRacks(self):
        """ 根据name获取机架列表(模糊查询)   正例"""
        name = "meilanzi"
        result = self.tackPage.getRackByName(name=name)
        assert result["status"] == 200
        assert result['data']["name"] == name


    def test_queryRackPage(self):
        """ 根据条件获取机架列表(模糊)   正例"""
        name = "meilanzi"
        pageSize = 1
        pageNum = 1
        result = self.tackPage.queryRackPage(pageNum=pageNum,pageSize=pageSize,name=name)
        assert result["status"] == 200
        assert result['data']["list"][0]["name"] == name

    def test_getrackById(self):
        """ 根据id获取机架   正例"""
        name = "meilanzi"
        pre = self.tackPage.getRackByName(name=name)
        id = pre["data"]["id"]
        result = self.tackPage.getRackById(id=id)
        assert result["status"] == 200
        assert result['data']["id"] == id


    def test_updateack(self,):
        """ 更新机架   正例"""
        updatename = "meilanzi"
        id = "40383865759477760"
        result = self.tackPage.updaterack(id=id,name=updatename)
        assert result["status"] == 200
        # assert result['data']["name"] == updatename

    @pytest.mark.parametrize("name,siteId", [("meilanzi001", "123456789"), ("meilanzi002", "12345678")])
    def test_deleteRack(self,name,siteId):
        """ 删除机架   正例"""
        try:
            self.tackPage.getRackByName(name=name)
        finally:
            pre = self.tackPage.addRacks(name=name,siteId=siteId)
            id = pre["data"]["id"]

        result = self.tackPage.deleteRack(id=id)
        assert result["status"] == 200



