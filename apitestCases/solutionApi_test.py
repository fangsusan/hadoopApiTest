import allure
import pytest

from pageApi.solutionPage import solutionPage

@allure.feature("solution管理接口")
class TestsolutionPage:
    """ solution管理接口 测试"""

    def setup(self):
        self.solutionPage = solutionPage()

    @allure.story("根据获取所有solution")
    def test_getSolutions(self):
        """ 根据获取所有solution"""
        result = self.solutionPage.getSolutions()
        print(result)
        assert result['status'] == 200

    @allure.story("根据条件获取solution列表")
    @pytest.mark.parametrize("name",[("witfang")])
    def test_querySolutions(self,name):
        """根据条件获取solution列表 正例"""
        result = self.solutionPage.querySolutions(name=name)
        print(result)
        assert result['status'] == 200

    @allure.story("根据条件获取solution列表")
    @pytest.mark.parametrize("name,version", [("witjing","1.0")])
    def test_addSolution(self, name,version):
        """根据条件获取solution列表 正例"""
        result = self.solutionPage.addSolution(name=name,version=version)
        print(result)
        newid = result['data']['id']
        try:
            self.solutionPage.getSolutionById(id=newid)
        finally:
            self.solutionPage.deleteSolution(id=newid)
        assert result['status'] == 200

    @allure.story("根据条件获取solution总数")
    @pytest.mark.parametrize("name,version", [("witfang","1.0")])
    def test_querySolutionsCount(self,name,version):
        """根据条件获取solution总数"""
        result = self.solutionPage.querySolutionsCount(name=name,version=version)
        print(result)
        assert result['status'] == 200


    @allure.story("根据条件获取solution列表")
    @pytest.mark.parametrize("pageNum,pageSize,name,version",[(1,5,"witfang","1.0")])
    def test_querySolutionsPage(self,pageNum,pageSize,name,version):
        """根据条件获取solution列表"""
        result =self.solutionPage.querySolutionsPage(pageSize=pageSize,pageNum=pageNum,name=name,version=version)
        print(result)
        assert result['status'] == 200

    @allure.story("更新solution")
    @pytest.mark.parametrize("id",[("53058309376200704")])
    def test_getSolutionById(self,id):
        """ 根据ID获取solution"""
        result = self.solutionPage.getSolutionById(id=id)
        print(result)
        assert result['status'] == 200

    @allure.story("更新solution")

    def test_updateSolution(self):
        """ 更新solution """
        pre = self.solutionPage.addSolution(name="witfang1",version="1.0")
        print(pre)
        newid = pre['data']['id']
        result = self.solutionPage.updateSolution(name="updataname",version="version",id=newid)
        print(result)
        try:
            self.solutionPage.getSolutionById(id=newid)
        finally:
            self.solutionPage.deleteSolution(id=newid)
        assert result['status'] == 200


    @allure.story("根据id删除solution")
    @pytest.mark.parametrize("name,version", [("witjing", "1.0")])
    def test_deleteSolution(self,name,version):
        """ 根据id删除solution """
        pre = self.solutionPage.addSolution(name=name,version=version)
        id = pre['data']['id']
        try:
            self.solutionPage.getSolutionById(id=id)
        finally:
            result = self.solutionPage.deleteSolution(id=id)
        assert result['status'] == 200

    @allure.story("根据ID获取solution详情")
    @pytest.mark.parametrize("id",[("53058309376200704")])
    def test_getSolutionDetailById(self,id):
        """ 根据ID获取solution详情"""
        result = self.solutionPage.getSolutionDetailById(solutionId=id)
        assert result['status'] == 500

