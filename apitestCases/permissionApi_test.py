import allure
import pytest

from pageApi.permissonPage import permissionPage

@allure.feature("WitServer 权限管理接口test")
class TestPermission:
    """  WitServer 权限管理接口test"""
    def setup(self):
        self.permissionPage = permissionPage()

    @allure.story("添加权限信息Api")
    @pytest.mark.parametrize("resourceId,tag",[("10002","001")])
    def test_insertPermission(self,resourceId,tag):
        """ 添加权限信息 正例"""
        result = self.permissionPage.insertPermission(resourceId=resourceId,tag=tag)
        id = result['data']['id']
        try:
            self.permissionPage.getPermission(id=id)
        finally:
            self.permissionPage.deletePermission(id=id)
        assert result['status'] == 200
        assert result['data']['tag'] == tag

    @allure.story("获取权限总数Api")
    def test_countAll(self):
        """ 获取权限总数 正例"""
        result = self.permissionPage.countAll()
        assert result['status'] == 200
        assert result['data'] != 0

    @allure.story("根据权限名称获取权限总数Api")
    @pytest.mark.parametrize("tag",[("1")])
    def test_countByTag(self,tag):
        """ 根据权限名称获取权限总数  正例"""
        result = self.permissionPage.countByTag(tag=tag)
        assert result['status'] == 200
        # assert result['data'] != 0

    @allure.story("获取权限列表Api")
    @pytest.mark.parametrize("pageNum,pageSize",[(1,4)])
    def test_findPage(self,pageNum,pageSize):
        """ 获取权限列表 正例"""
        result = self.permissionPage.findPage(pageSize=pageSize,pageNum=pageNum)
        assert result['status'] == 200
        assert result['data'] != 0

    @allure.story("根据权限名称获取权限列表Api")
    @pytest.mark.parametrize("tag,pageNum,pageSize", [("1",1, 4)])
    def test_findByTag(self,tag,pageNum, pageSize):
        """ 根据权限名称获取权限列表 正例"""
        result = self.permissionPage.findByTag(tag=tag,pageSize=pageSize, pageNum=pageNum)
        assert result['status'] == 200
        assert result['data'] != 0

    @allure.story("获取权限信息Api")
    @pytest.mark.parametrize("id", [("42214243981869056")])
    def test_getPermission(self,id):
        """ 获取权限信息 正例"""
        result = self.permissionPage.getPermission(id=id)
        assert result['status'] == 200
        # assert result['data'] != 0

    @allure.story("更新权限信息Api")
    @pytest.mark.parametrize("id,tag", [("42214243981869056","1002",)])
    def test_updatePermission(self,id,tag):
        """ 更新权限信息 正例"""
        result = self.permissionPage.updatePermission(id=id,tag=tag)
        assert result['status'] == 200


    @allure.story("删除权限信息Api")
    @pytest.mark.parametrize("resourceId,tag,pageSize,pageNum",[("10002","001",1,10)])
    def test_deletePermission(self,resourceId,tag,pageSize,pageNum):
        """ 删除权限信息 正例"""
        try:
            self.permissionPage.findByTag(tag=tag,pageSize=pageSize,pageNum=pageNum)
        finally:
            pre = self.permissionPage.insertPermission(resourceId=resourceId, tag=tag)
            print(pre)
            id = pre['data']['id']
        result = self.permissionPage.deletePermission(id=id)
        assert result['status'] == 200

