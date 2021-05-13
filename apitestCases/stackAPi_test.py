import allure
import pytest

from pageApi.stackPage import StackPage

@allure.feature("技术栈管理接口 ")
class TestStack:
    """ 技术栈管理接口"""
    def setup(self):
        self.StackPage = StackPage()

    def teardown(self):
        pass

    @allure.story("获取所有技术栈 Api")
    def test_getStacks(self):
        """获取所有技术栈接口"""
        result = self.StackPage.getStacks()
        print(result)
        assert result["status"] == 200

    @allure.story("根据hostname获取技术栈列表 Api")
    @pytest.mark.parametrize("name,version",[("fang0006","1.2")])
    def test_queryStacks(self,name,version):
        """根据hostname获取技术栈列表 正例 """
        result = self.StackPage.queryStacks(hostname=name,version=version)

        print(result)
        assert result["status"] == 200
        # assert result["data"]["name"] == name

    @allure.story("添加技术栈 Api")
    @pytest.mark.parametrize("name,version",[("fang0006","1.2")])
    def test_addStack(self,name,version):
        """添加技术栈   正例"""
        result = self.StackPage.addStack(name=name,version=version)
        print(result)
        id = result['data']['id']
        try:
            self.StackPage.getStackByid(id=id)
        finally:
            self.StackPage.deleteStack(id=id)
        assert result["status"] == 200

    @allure.story("按条件id获取技术栈总数 Api")
    @pytest.mark.parametrize("id",[("40009538216144896")])
    def test_queryStackCount(self,id):
        """ 按条件id获取技术栈总数 正例"""

        result = self.StackPage.queryStackCount(id=id)
        assert result["status"] == 200
        # assert result['data'] != 0

    @allure.story("按page页码查询询技术栈总数 Api")
    @pytest.mark.parametrize("pageNum,pageSize,name",[(1,5,"fang0002")])
    def test_queryStacksPage(self,pageNum,pageSize,name):
        """ 按page页码查询询技术栈总数    正例"""

        result = self.StackPage.queryStacksPage(pageNum=pageNum,pageSize=pageSize,name=name)
        print(result)
        assert result["status"] == 200
        # assert result['data']['list'][0]["name"] == name

    @allure.story("按ID获取技术栈 Api")
    @pytest.mark.parametrize("id",[("40009538216144896")])
    def test_getStackByid(self,id):
        """ 按ID获取技术栈   正例"""

        result = self.StackPage.getStackByid(id=id)
        print(result)
        assert result["status"] == 200
        # assert result['data']["id"] == id

    @allure.story("更新技术栈 Api")
    @pytest.mark.parametrize("id,name",[("40009538216144896","fyj001")])
    def test_updateStack(self,name,id):
        """ 更新技术栈  正例"""

        result = self.StackPage.updateStack(name=name,id=id)
        print(result)
        assert result["status"] == 200

    @allure.story("根据id删除技术栈 Api")
    @pytest.mark.parametrize("name,version",[("fang0006","1.2")])
    def test_deleteStack(self,name,version):
        """  根据id删除技术栈 """
        try:
            self.StackPage.queryStacks(hostname=name,version=version)
        finally:
            pre = self.StackPage.addStack(name=name,version=version)
            id = pre['data']['id']

        result = self.StackPage.deleteStack(id=id)
        assert result["status"] == 200

    @allure.story("根据Id获取技术栈详情 Api")
    @pytest.mark.parametrize("id", [("47008490782216192")])
    def test_getStackDetaiByid(self,id):
        """ 根据Id获取技术栈详情 """
        result = self.StackPage.getStackDetaiByid(id=id)
        print(result)
        assert result["status"] == 200



