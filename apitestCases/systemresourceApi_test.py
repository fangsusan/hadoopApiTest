import allure
import pytest

from pageApi.systemResourcePage import systemResourcePage

@allure.feature("WitServer系统资源管理模块")
class TestSystemResource:
    """ WitServer系统资源管理接口 test"""
    def setup(self):
        self.systemResourcePage = systemResourcePage()

    def teardown(self):
        pass

    @allure.story("获取所有资源Api")
    def test_getResources(self):
        """ 获取所有资源 """
        result = self.systemResourcePage.getResources()
        print(result)
        assert result['status'] == 200
        assert result['data'] != 0

    @allure.story("添加系统资源信息Api")
    @pytest.mark.parametrize("name,pageNum,pageSize",[("meilanzi005",1,10)])
    def test_insertSystemresource(self,name,pageNum,pageSize):
        """ 添加系统资源信息 正例"""
        result = self.systemResourcePage.insertSystemresource(name=name)
        print(result)
        id = result['data']['id']
        try:
            self.systemResourcePage.findByName(name=name,pageNum=pageNum,pageSize=pageSize)
        finally:
            self.systemResourcePage.deleteystemResource(id=id)
        assert result['status'] == 200

    @allure.story("获取资源总数Api")
    def test_countAll(self):
        """ 获取资源总数 正例"""
        result = self.systemResourcePage.countAll()
        print(result)
        assert result['status'] == 200

    @allure.story("根据资源名称获取资源总数Api")
    @pytest.mark.parametrize("name",[("meilanzi")])
    def test_countByName(self,name):
        """ 根据资源名称获取资源总数 正例"""
        result = self.systemResourcePage.countByName(name=name)
        print(result)
        assert result['status'] == 200
        # assert result['data'] != 0


    @allure.story("根据资源类型获取资源总数Api")
    @pytest.mark.parametrize("type", [("MENU")])
    def test_countByType(self,type):
        """ 根据资源类型获取资源总数 正例"""
        result = self.systemResourcePage.countByType(type=type)
        print(result)
        assert result['status'] == 200
        # assert result['data'] != 0

    @allure.story("根据资源名称获取资源列表Api")
    @pytest.mark.parametrize("name,pageNum,pageSize", [("meilanzi",1,10)])
    def test_findByName(self,name,pageNum,pageSize):
        """ 根据资源名称获取资源列表 正例"""
        result = self.systemResourcePage.findByName(name=name,pageNum=pageNum,pageSize=pageSize)
        print(result)
        assert result['status'] == 200
        assert result['data'] != 0

    @allure.story("获取资源列表Api")
    @pytest.mark.parametrize("pageNum,pageSize", [(1, 10)])
    def test_findPage(self, pageNum, pageSize):
        """ 获取资源列表 正例"""
        result = self.systemResourcePage.findPage(pageNum=pageNum, pageSize=pageSize)
        print(result)
        assert result['status'] == 200
        assert result['data'] != 0

    @allure.story("根据资源类型获取资源列表Api")
    @pytest.mark.parametrize("type,pageNum,pageSize", [("MENU",1, 10)])
    def test_findByType(self,type, pageNum, pageSize):
        """ 根据资源类型获取资源列表 正例"""
        result = self.systemResourcePage.findByType(type=type,pageNum=pageNum, pageSize=pageSize)
        print(result)
        assert result['status'] == 200
        assert result['data'] != 0

    @allure.story("获取资源信息Api")
    @pytest.mark.parametrize("id", [("30323911845490688")])
    def test_getSystemResource(self,id):
        """ 获取资源信息 正例"""
        result = self.systemResourcePage.getSystemResource(id=id)
        print(result)
        assert result['status'] == 200
        # assert result['data'] != 0

    @allure.story("更新资源信息Api")
    @pytest.mark.parametrize("id,name", [("41523729510973440","meilanzi009")])
    def test_updateSystemResource(self, id,name):
        """ 更新资源信息 正例"""
        result = self.systemResourcePage.updateSystemResource(id=id,name=name)
        print(result)
        assert result['status'] == 200

    @allure.story("更新资源信息Api")
    @pytest.mark.parametrize("name,pageNum,pageSize", [("meilanzi009",1,10)])
    def test_deleteystemResource(self,name,pageNum,pageSize):
        """ 更新资源信息 正例"""

        try:
            self.systemResourcePage.findByName(name=name, pageNum=pageNum, pageSize=pageSize)
        finally:
            pre = self.systemResourcePage.insertSystemresource(name=name)
            print(pre)
            id = pre['data']['id']
        result = self.systemResourcePage.deleteystemResource(id=id)
        print(result)
        assert result['status'] == 200





