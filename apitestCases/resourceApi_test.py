import allure
import pytest

from pageApi.resourcePage import ResourcePage

@allure.feature("资源管理接口")
class Testresource:
    """ 资源管理接口 """
    def setup(self):
        self.ResourcePage = ResourcePage()

    def teardown(self):
        pass

    @allure.story("根据获取所有资源 Api")
    def test_getResources(self):
        """ 根据获取所有资源 正例"""
        r = self.ResourcePage.getResources()
        assert r['status'] == 200

    @allure.story("根据条件获取资源列表 Api")
    @pytest.mark.parametrize("name",[("Wit")])
    def test_queryResources(self,name):
        """根据条件获取资源列表  正例"""
        r = self.ResourcePage.queryResources(name=name)
        print(r)
        assert r['status'] == 200
        assert r['data'][0]['name'] == name

    @allure.story("添加资源 Api")
    @pytest.mark.parametrize("name",[("meila1nzi")])
    def test_addResource(self,name):
        """添加资源  正例"""
        r = self.ResourcePage.addResource(name=name)
        print(r)
        assert r['status'] == 200
        # assert r['data'][0]['name'] == name

    @allure.story("根据条件获取资源总数 Api")
    @pytest.mark.parametrize("name",[("WIT")])
    def test_queryResourcesCount(self,name):
        """根据条件获取资源总数  正例"""
        r = self.ResourcePage.queryResourcesCount(name=name)
        assert r['status'] == 200
        assert r['data'] != 0

    @allure.story("根据条件获取一页资源 Api")
    @pytest.mark.parametrize("pageSize,pageNum",[(1,1),(1,5)])
    def test_queryResourcesPage(self,pageSize,pageNum):
        """根据条件获取一页资源   正例"""
        r =self.ResourcePage.queryResourcesPage(pageSize=pageSize,pageNum=pageNum)
        print(r)
        assert r['status'] == 200
        assert r['data']['total'] != 0

    @allure.story("上传资源文件 Api")
    def test_uploadResource(self):
        """上传资源文件 正例 """
        pass

    @allure.story("根据ID获取资源 Api")
    @pytest.mark.parametrize("id",[("39649245858377728")])
    def test_getResourceById(self,id):
        """根据ID获取资源 正例 """
        r = self.ResourcePage.getResourceById(id=id)
        assert r['status'] == 200
        # assert r['data']['id'] == id

    @allure.story("根据ID获取资源 Api")
    @pytest.mark.parametrize("id,name", [("39649245858377728","meilanzi")])
    def test_updateResource(self, id,name):
        """根据ID获取资源 正例"""
        r = self.ResourcePage.updateResource(id=id,name=name)
        assert r['status'] == 200

    @allure.story("根据ID删除资源 Api")
    @pytest.mark.parametrize("name", [("meilanzi")])
    def test_deleteResource(self,name):
        """根据ID删除资源  正例"""
        try:
            self.ResourcePage.queryResources(name=name)
        finally:
            pre = self.ResourcePage.addResource(name=name)
            id = pre['data']['id']
        r = self.ResourcePage.deleteResource(id=id)
        assert r['status'] == 200


