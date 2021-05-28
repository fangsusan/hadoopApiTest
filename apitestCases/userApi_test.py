import pytest
import allure
from pageApi.userPage import userPage
from common.randomUserinfo import random_name, random_phone, random_password


@allure.feature('Witserver 用户管理接口模块 测试')
class Testuser:
    """ WitServer 用户管理接口  测试"""

    def setup_class(self):
        self.userPage = userPage()
        self.userId = 46914125908955136
        self.roleId = 46923964773060608
        self.roleIds = [46923964773060608,46958389690912768]

    def teardown_class(self):
        self.userPage.batchDeleteRole(self.userId, self.roleIds)

    @pytest.mark.parametrize("username,password",[("fangy",111111)])
    def test_login(self,username,password):
        """ 登录 正例"""
        result = self.userPage.login(username=username,password=password)
        assert result['data']['name'] == username

    @allure.story("获取所有用户 正例")
    def test_getUsers(self):
        """ 获取所有用户 正例"""
        result = self.userPage.getUsers()
        print(result)
        assert result['status'] == 200
        assert result['data'] != 0

    @allure.story('添加用户信息 正例')
    def test_insert(self):
        """ 添加用户信息admin登录 正例"""
        result = self.userPage.insert(name=random_name(8),phone=random_phone(11), email="2222@qq.com", password=random_password(6), username=random_name(9))
        print(result)
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


    @allure.story("根据用户名称获取用户列表 正例")
    @pytest.mark.parametrize("name,pageSize,pageNum", [("fangy",1,10)])
    def test_findByName(self,name,pageSize,pageNum):
        """ 根据用户名称获取用户列表 正例"""
        result = self.userPage.findByName(name=name,pageSize=pageSize,pageNum=pageNum)
        print(result)
        assert result['status'] == 200
        assert result['data']['list'][0]['name'] == name

    @allure.story("获取用户所有组织 正例")
    @pytest.mark.parametrize("userId",[(46914125908955136)])
    def test_getOrganizations(self,userId):
        """ 获取用户所有组织 正例"""
        result = self.userPage.getOrganizations(userId)
        print(result)
        assert result['status'] == 200
        assert result['data'] != 0


    @allure.story("获取用户列表 正例")
    @pytest.mark.parametrize("pageSize,pageNum",[(1,10)])
    def test_findPage(self,pageSize, pageNum):
        """ 获取用户列表 正例"""
        result = self.userPage.findPage(pageSize,pageNum)
        print(result)
        assert result['status'] == 200

    @allure.story("用户修改密码 正例")
    def test_changePassword(self):
        """ 修改密码 用户修改密码"""
        try:
            result = self.userPage.changePwd(username="fangy",password=random_password(7))
        finally:
            self.userPage.adminchangePwd(username="fangy",password="111111")
        print(result)
        assert result['status'] == 200

    @allure.story("管理员修改其他用户密码 正例")
    def test_changeOtherUserpwd(self):
        """管理员修改其他用户密码 正例"""
        result = self.userPage.adminchangePwd(username="fangy",password="111111")
        assert result['status'] == 200

    @allure.story("获取用户信息 正例")
    @pytest.mark.parametrize("id",[("42172949280604160")])
    def test_getUser(self,id):
        """ 获取用户信息 正例"""
        result = self.userPage.getUser(id=id)
        print(result)
        assert result['status'] == 200

    @allure.story("更新用户信息 正例")
    # @pytest.mark.parametrize("id,realname,phone,email", [("50527843863515136","fangj",18768466308,"123456789@qq.com")])
    def test_updateUser(self):
        """ 更新用户信息 正例"""
        pre = self.userPage.insert(name=random_name(9),phone=random_phone(11),email="1234@qq.com",username=random_name(11),password=123456)
        print(pre)
        id = pre['data']['id']
        result = self.userPage.updateUser(id=id,realname=random_name(8),phone=random_phone(11),email="11111@qq.com")
        print(result)
        assert result['status'] == 200

    @allure.story(" status：0禁用/ 1 启用用户 正例")
    @pytest.mark.parametrize("id,status",[(50534537125449728,0),(50534537125449728,1)])
    def test_changeUserStatus(self,id,status):
        """ status：0禁用/ 1 启用用户 正例"""
        result = self.userPage.changeUserStatus(id,status)
        print(result)
        assert result['status'] == 200

    @allure.story("获取用户所有权限 正例")
    @pytest.mark.parametrize("userId",[(46914125908955136)])
    def test_getPermissions(self,userId):
        """获取用户所有权限 正例"""
        result = self.userPage.getPermissions(userId)
        assert result['status'] == 200

    @allure.story("获取用户所有角色 正例")
    @pytest.mark.parametrize("userId",[(46914125908955136)])
    def test_getRoles(self,userId):
        """获取用户所有角色 正例"""
        result = self.userPage.getRoles(userId)
        assert result['status'] == 200

    @allure.story("批量添加用户角色 正例")
    def test_batchInsertRole(self):
        """批量添加用户角色 正例"""
        result = self.userPage.batchInsertRole(self.userId,self.roleIds)
        assert result['status'] == 200

    @allure.story("删除用户下的一批角色 正例")
    def test_batchDeleteRole(self):
        """ 删除用户下的一批角色  正例"""
        result = self.userPage.batchDeleteRole(self.userId,self.roleIds)
        assert result['status'] == 200

    @allure.story("删除用户下的所有角色 正例")
    def test_deleteAllRole(self):
        """ 删除用户下的所有角色 正例 """
        try:
            self.userPage.batchInsertRole(self.userId,self.roleIds)
        finally:
            result = self.userPage.deleteAllRole(self.userId)
        assert result['status'] == 200

    @allure.story("添加一个用户角色 正例")
    def test_insertRole(self):
        """ 添加一个用户角色 正例"""
        result = self.userPage.insertRole(self.userId,self.roleId)
        print(result)
        assert result['status'] == 200

    @allure.story("删除用户下的某个角色 正例")
    def test_deleteRole(self):
        """删除用户下的某个角色 正例"""
        try:
            self.userPage.insertRole(self.userId,self.roleId)
        finally:
            result = self.userPage.deleteRole(self.userId,self.roleId)
        assert result['status'] == 200



