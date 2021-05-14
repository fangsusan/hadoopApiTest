import allure
import pytest

from pageApi.actionPage import ActionPage


@allure.feature("行为管理接口模块")
class TestAction:
    """ 行为管理接口模块"""
    def setup(self):
        self.ActionPage =ActionPage()

    def teardown(self):
        pass

    @allure.story("获取所有行为信息 Api")
    def test_getActions(self):
        """获取所有行为信息  正例"""
        result = self.ActionPage.getActions()
        print(result)
        assert result['status'] == 200
        assert result['data']  != 0

    @allure.story("终止操作 Api")
    def test_abortAction(self):
        """终止操作"""
        pass

    @allure.story("根据条件获取信息列表 Api")
    @pytest.mark.parametrize("pageSize,pageNum",[(1,2)])
    def test_queryActionPage(self,pageSize,pageNum):
        """根据条件获取信息列表  正例"""
        result = self.ActionPage.queryActionPage(pageSize=pageSize,pageNum=pageNum)

        print(result)
        assert result['status'] == 200
        assert result['data'] != 0

    @allure.story("根据条件获取信息列表 Api")
    @pytest.mark.parametrize("name", [("meilanzi")])
    def test_queryActions(self,name):
        """根据条件获取信息列表 正例"""
        result = self.ActionPage.queryActions(name=name)
        print(result)
        assert result['status'] == 200
        assert result['data'] != 0

    @allure.story("根据条件获取信息列表 Api")
    @pytest.mark.parametrize("pageNum,pageSize", [(1,8)])
    def test_queryStagesPage(self,pageNum,pageSize):
        """根据条件获取信息列表  正例"""
        result = self.ActionPage.queryActionPage(pageSize=pageSize,pageNum=pageNum)
        print(result)
        assert result['status'] == 200
        assert result['data'] != 0

    @allure.story("获取所有行为的阶段信息 Api")
    def test_queryStages(self):
        """获取所有行为的阶段信息  正例"""
        result = self.ActionPage.queryStages()
        print(result)
        assert result['status'] == 200
        assert result['data'] != 0

    @allure.story("获取行为信息表 Api")
    @pytest.mark.parametrize("stageId", [("47018524182335488")])
    def test_getStageById(self,stageId):
        """获取行为信息表：tb_action_stage  正例"""
        result = self.ActionPage.getStageById(stageId=stageId)
        print(result)
        assert result['status'] == 200
        assert result['data']['id'] == stageId

    @allure.story("根据条件获取信息列表 Api")
    @pytest.mark.parametrize("pageNum,pageSize", [(1,8)])
    def test_queryTasksPage(self,pageNum,pageSize):
        """根据条件获取信息列表 正例"""
        result = self.ActionPage.queryTasksPage(pageSize=pageSize,pageNum=pageNum)
        print(result)
        assert result['status'] == 200
        assert result['data'] != 0

    @allure.story("获取所有行为的阶段信息 Api")
    def test_queryTasks(self):
        """获取所有行为的阶段信息 正例"""
        result = self.ActionPage.queryTasks()
        print(result)
        assert result['status'] == 200
        assert result['data'] != 0

    @allure.story("获取行为信息 Api")
    @pytest.mark.parametrize("taskId", [('1617860227267')])
    def test_getTaskById(self,taskId):
        """获取行为信息   正例"""
        result = self.ActionPage.getTaskById(taskId=taskId)
        print(result)
        assert result['status'] == 200
        # assert result['data']['id'] ==taskId

    @allure.story("更新行为信息 Api")
    @pytest.mark.parametrize("taskId,name,status", [('1617860227267','fyj001',1)])
    def test_updateTask(self,taskId,name,status):
        """更新行为信息 正例"""
        result = self.ActionPage.updateTask(taskId=taskId,name=name,status=status)
        print(result)
        assert result['status'] == 200


    @allure.story("测试Task返回结果 Api")
    def test_testActionTaskResponse(self):
        """测试Task返回结果"""
        result = self.ActionPage.testActionTaskResponse()
        assert result['status'] == 200

    @allure.story("获取行为信息 Api")
    @pytest.mark.parametrize("taskId", [('1617860227267')])
    def test_getActionById(self,taskId):
        """获取行为信息   正例"""
        result = self.ActionPage.getActionById(taskId=taskId)
        assert result['status'] == 200
        assert result['data'] != 0
        # assert result['data']['id'] == taskId

