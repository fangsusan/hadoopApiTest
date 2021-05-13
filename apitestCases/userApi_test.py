import pytest
import allure
from pageApi.userPage import userPage

@allure.feature('Witserver 用户管理接口模块 测试')
class Testuser:
    """ WitServer 用户管理接口  测试"""
    def setup(self):
        self.userPage = userPage()
        self.userId = 46914125908955136
        self.roleId = 46923964773060608
        self.roleIds = [46923964773060608,46958389690912768]

    def teardown(self):
        self.userPage.batchDeleteRole(userId=self.userId, roleIds=self.roleIds)

    @allure.story("获取所有用户 正例")
    def test_getUsers(self):
        """ 获取所有用户 正例"""
        result = self.userPage.getUsers()
        assert result['status'] == 200
        assert result['data'] != 0

    @allure.story('添加用户信息 正例')
    @pytest.mark.parametrize("password,salt,username,pageSize,pageNum",[("123789","salt","fyj001",1,10)])
    def test_insert(self,password,salt,username,pageSize,pageNum):
        """ 添加用户信息 正例"""
        with allure.step('添加用户信息'):
            result = self.userPage.insert(password=password,salt=salt,username=username)
        id = result['data']['id']
        with allure.step('检查是否存在，并删除'):

            try:
                self.userPage.findByName(name=username,pageSize=pageSize,pageNum=pageNum)
            finally:
                self.userPage.deleteUser(id=id)
        with allure.step("校验结果"):
            allure.attach('期望结果', '验证通过')
            assert result['status'] == 200


    @allure.story("获取用户总数 正例")
    def test_countAll(self):
        """ 获取用户总数 正例"""
        result = self.userPage.countAll()
        assert result['status'] == 200
        assert result['data'] != 0

    @allure.story("根据用户名称获取用户总数 正例")
    @pytest.mark.parametrize("name",[("18768466309")])
    def test_countByName(self,name):
        """ 根据用户名称获取用户总数 正例"""
        result = self.userPage.countByName(name=name)
        print(result)
        assert result['status'] == 200
        assert result['data'] != 0


    @allure.story("根据用户名称获取用户列表 正例")
    @pytest.mark.parametrize("name,pageSize,pageNum", [("meilanzi",1,10)])
    def test_findByName(self, name,pageSize,pageNum):
        """ 根据用户名称获取用户列表 正例"""
        result = self.userPage.findByName(name=name,pageSize=pageSize,pageNum=pageNum)
        print(result)
        assert result['status'] == 200
        assert result['data']['name'] ==name


    @allure.story("获取用户所有组织 正例")
    @pytest.mark.parametrize("userId",[(46914125908955136)])
    def test_getOrganizations(self,userId):
        """ 获取用户所有组织 正例"""
        result = self.userPage.getOrganizations(userId=userId)
        print(result)
        assert result['status'] == 200
        assert result['data'] != 0


    @allure.story("获取用户列表 正例")
    @pytest.mark.parametrize("pageSize,pageNum",[(1,10)])
    def test_findPage(self,pageSize, pageNum):
        """ 获取用户列表 正例"""
        result = self.userPage.findPage(pageSize=pageSize, pageNum=pageNum)
        print(result)
        assert result['status'] == 200


    @allure.story("获取用户信息 正例")
    @pytest.mark.parametrize("id",[("42172949280604160")])
    def test_getUser(self,id):
        """ 获取用户信息 正例"""
        result = self.userPage.getUser(id=id)
        print(result)
        assert result['status'] == 200

    @allure.story("更新用户信息 正例")
    @pytest.mark.parametrize("id,name,password", [("42172949280604160","meilanzi new",123456)])
    def test_updateUser(self,id,name,password):
        """ 更新用户信息 正例"""
        result = self.userPage.updateUser(id=id,name=name,password=password)
        print(result)
        assert result['status'] == 200


    @allure.story("删除用户信息 正例")
    @pytest.mark.parametrize("username,salt,password,pageSize,pageNum", [("meilanfyj", "meilnew","1987654",1,10)])
    def test_deleteUser(self,username,salt,password,pageSize,pageNum):
        """ 删除用户信息 正例"""
        try:
            self.userPage.findByName(name=username,pageSize=pageSize,pageNum=pageNum)
        finally:
            pre = self.userPage.insert(password=password,salt=salt,username=username)
            print(pre)
            id = pre['data']['id']
            print(pre['data']['salt'])
        result = self.userPage.deleteUser(id=id)
        assert result['status'] == 200


    @allure.story("获取用户所有权限 正例")
    @pytest.mark.parametrize("userId",[(46914125908955136)])
    def test_getPermissions(self,userId):
        """获取用户所有权限 正例"""
        result = self.userPage.getPermissions(userId=userId)
        assert result['status'] == 200

    @allure.story("获取用户所有角色 正例")
    @pytest.mark.parametrize("userId",[(46914125908955136)])
    def test_getRoles(self,userId):
        """获取用户所有角色 正例"""
        result = self.userPage.getRoles(userId=userId)
        assert result['status'] == 200

    @allure.story("批量添加用户角色 正例")
    def test_batchInsertRole(self):
        """批量添加用户角色 正例"""
        result = self.userPage.batchInsertRole(userId=self.userId,roleIds=self.roleIds)
        assert result['status'] == 200

    @allure.story("删除用户下的一批角色 正例")
    def test_batchDeleteRole(self):
        """ 删除用户下的一批角色  正例"""
        result = self.userPage.batchDeleteRole(userId=self.userId,roleIds=self.roleIds)
        assert result['status'] == 200


    @allure.story("删除用户下的所有角色 正例")
    def test_deleteAllRole(self):
        """ 删除用户下的所有角色 正例 """
        try:
            self.userPage.batchInsertRole(userId=self.userId,roleIds=self.roleIds)
        finally:
            result = self.userPage.deleteAllRole(userId=self.userId)
        assert result['status'] == 200


    @allure.story("添加一个用户角色 正例")
    def test_insertRole(self):
        """ 添加一个用户角色 正例"""
        result = self.userPage.insertRole(userId=self.userId,roleId=self.roleId)
        print(result)
        assert result['status'] == 200


    @allure.story("删除用户下的某个角色 正例")
    def test_deleteRole(self):
        """删除用户下的某个角色 正例"""
        try:
            self.userPage.insertRole(userId=self.userId,roleId=self.roleId)
        finally:
            result = self.userPage.deleteRole(userId=self.userId,roleId=self.roleId)
        assert result['status'] == 200



