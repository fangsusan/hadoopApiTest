import pytest
from pageApi.rackPage import RackPage


class TestStack:
    def setup(self):
        self.RackPage = RackPage()

    def test_getRacks(self):
        """获取所有机架  正例"""
        result = self.RackPage.getRacks()
        assert result['status'] == 200

    @pytest.mark.parametrize("siteId,name",[("123455","meilanzi001")])
    def test_addRacks(self,siteId,name):
        """添加机架 siteId,name 必填  正例"""
        result = self.RackPage.addRacks(siteId=siteId,name=name)
        id = result['data']['id']
        try:
            self.RackPage.getRackByName(name=name)
        finally:
            self.RackPage.deleteRack(id=id)
        assert result['status'] == 200
        assert result['data']['name'] == name


    @pytest.mark.parametrize("name",[("meilanzi")])
    def test_getRackCount(self,name):
        """根据条件获取站点总数   正例"""
        result = self.RackPage.getRackCount(name=name)
        print(result)
        assert result['status'] == 200
        assert result['data'] != 0

    @pytest.mark.parametrize("name",[("meilanzi")])
    def test_getRackByName(self,name):
        """根据名称获取机架"""
        result = self.RackPage.getRackByName(name=name)
        print(result)
        assert result['status'] == 200
        assert result['data']['name']  == name


    @pytest.mark.parametrize("pageNum,pageSize,name",[(1,2,"meilanzi")])
    def test_queryRackPage(self,pageNum,pageSize,name):
        """根据条件获取机架列表(模糊)  正例"""
        result = self.RackPage.queryRackPage(pageNum=pageNum,pageSize=pageSize,name=name)
        print(result)
        assert result['status'] == 200
        assert result['data']['list'][0]['name'] == name

    @pytest.mark.parametrize("name",[("meilanzi")])
    def test_queryRacks(self,name):
        """根据条件获取机架列表(模糊查询) 正例"""
        result = self.RackPage.queryRacks(name=name)
        print(result)
        assert result['status'] == 200
        assert result['data'][0]['name'] == name


    @pytest.mark.parametrize("id",[("39665475319246848")])
    def test_getRackById(self,id):
        """根据ID获取机架   正例"""
        result = self.RackPage.getRackById(id=id)
        print(result)
        assert result['status'] == 200
        assert result['data']['id'] == id

    @pytest.mark.parametrize("id,name",[("40383822117744640","fyj002")])
    def test_updaterack(self,id,name):
        """更新机架   正例"""
        result = self.RackPage.updaterack(name=name,id=id)
        print(result)
        assert result['status'] == 200

    @pytest.mark.parametrize("siteId,name",[("123455","meilanzi001")])
    def test_deleteRack(self,siteId,name):
        """删除机架  正例 """
        try:
            self.RackPage.getRackByName(name=name)
        finally:
            result = self.RackPage.addRacks(siteId=siteId, name=name)
            id = result['data']['id']

        result = self.RackPage.deleteRack(id=id)
        print(result)
        assert result['status'] == 200






