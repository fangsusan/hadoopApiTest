import pytest
import allure
from pageApi.organizationPage import organizationPage

@allure.feature("WitServer组织管理接口 模块测试")
class Testorganization:
    """ WitServer 组织管理接口"""

    def setup(self):
        self.organizationPage = organizationPage()

    def teardown(self):
        pass

    @allure.story('获取所有组织Api')
    def test_getOrganizations(self):
        """ 获取所有组织 正例 """
        result = self.organizationPage.getOrganizations()
        assert result['status'] == 200
        assert result['data'] != 0

    @allure.story('添加组织信息Api')
    @pytest.mark.parametrize("name",[("meilanzi")])
    def test_insert(self,name):
        """ 添加组织信息 正例 """
        try:
            result = self.organizationPage.insert(name=name)
            id = result['data']['id']
        finally:
            self.organizationPage.deleteOrganization(id=id)

        assert result['status'] == 200
        assert result['data']['name'] == name

    @allure.story('获取组织总数Api')
    def test_countAll(self):
        """ 获取组织总数 正例 """
        result = self.organizationPage.countAll()
        assert result['status'] == 200
        assert result['data'] != 0

    @allure.story('根据组织名称获取组织总数Api')
    @pytest.mark.parametrize("name",[("orgaization")])
    def test_countByName(self,name):
        """根据组织名称获取组织总数  正例 """
        result = self.organizationPage.countByName(name=name)
        print(result)
        assert result['status'] == 200
        assert result['data'] != 0

    @allure.story('根据组织名称获取组织列表Api')
    @pytest.mark.parametrize("name,pageNum,pageSize",[("orgaization",1,10)])
    def test_findByName(self,name,pageNum,pageSize):
        """ 根据组织名称获取组织列表 正例 """
        result = self.organizationPage.findByName(name=name,pageSize=pageSize,pageNum=pageNum)
        print(result)
        assert result['status'] == 200
        assert result['data'] != 0

    @allure.story('获取组织列表Api')
    @pytest.mark.parametrize("pageNum,pageSize",[(1,10)])
    def test_findPage(self,pageNum,pageSize):
        """ 获取组织列表 正例 """
        result = self.organizationPage.findPage(pageNum=pageNum,pageSize=pageSize)
        assert result['status'] == 200
        assert result['data'] != 0

    @allure.story('获取组织所有用户Api')
    @pytest.mark.parametrize("organizationId",[(47699223470166016)])
    def test_getUsers(self,organizationId):
        """ 获取组织所有用户 正例 """
        result = self.organizationPage.getUsers(organizationId=organizationId)
        assert result['status'] == 200
        assert result['data'] != 0


    @allure.story('根据ID获取组织信息Api')
    @pytest.mark.parametrize("id",[(47699223470166016)])
    def test_getOranization(self,id):
        """ 根据ID获取组织信息  正例 """
        result = self.organizationPage.getOranization(id=id)
        assert result['status'] == 200
        assert result['data'] != 0


    @pytest.mark.parametrize("name,id",[("fy22j","47699012110798848")])
    def test_updateOrganization(self,name,id):
        """ 更新组织信息 正例 """
        result = self.organizationPage.updateOrganization(name=name,id=id)
        print(result)
        assert result['status'] == 200

    @pytest.mark.parametrize("name",[("fy22j11")])
    def test_deleteOrganization(self,name):
        """删除组织信息 """
        try:
            pre = self.organizationPage.insert(name=name)
            print(pre)
            id = pre['data']['id']
        finally:
            result = self.organizationPage.deleteOrganization(id=id)
        assert result['status'] == 200


    @pytest.mark.parametrize("organizationId,userId",[(47699097032871936,47697031921160192)])
    def test_insertUser(self,organizationId,userId):
        """ 添加一个组织用户 """
        try:
            result = self.organizationPage.insertUser(organizationId=organizationId,userId=userId)
        finally:
            self.organizationPage.deleteUser(organizationId=organizationId, userId=userId)
        print(result)
        assert result['status'] == 200

    @pytest.mark.parametrize("organizationId,userId",[(47699097032871936,47697031921160192)])
    def test_deleteUser(self,organizationId,userId):
        """ 删除一个组织用户 """
        try:
            self.organizationPage.insertUser(organizationId=organizationId,userId=userId)
        finally:
            result = self.organizationPage.deleteUser(organizationId=organizationId,userId=userId)
        assert result['status'] == 200

    def test_batchDeleteUser(self):
        """ 删除组织下的一批用户 """
        organizationId = 47699097032871936
        userIds = [47697031921160192, 47697042574692352]
        try:
            self.organizationPage.batchInsertUser(organizationId=organizationId, userIds=userIds)
        finally:
            result = self.organizationPage.batchDeleteUser(organizationId=organizationId, userIds=userIds)
        assert result['status'] == 200

    def test_batchInsertUser(self):
        """ 批量添加组织用户 """
        organizationId = 47699097032871936
        userIds = [47697031921160192,47697042574692352]
        try:
            result = self.organizationPage.batchInsertUser(organizationId=organizationId, userIds=userIds)
        finally:
            self.organizationPage.batchDeleteUser(organizationId=organizationId, userIds=userIds)
        assert result['status'] == 200

    @pytest.mark.parametrize("organizationId,userId",[(47694498385383424,47697031921160192)])
    def test_deleteAllUser(self,organizationId,userId):
        """删除组织下的所有用户 """
        try:
            self.organizationPage.insertUser(organizationId=organizationId,userId=userId)
        finally:
            result = self.organizationPage.deleteAllUser(organizationId=organizationId)
        assert result['status'] == 200
