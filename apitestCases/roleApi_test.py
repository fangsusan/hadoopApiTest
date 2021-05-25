import allure
import pytest

from pageApi.rolePage import rolePage

@allure.feature("WitServer角色管理模块")
class Testrole:
    """ WitServer角色管理接口 """
    def setup(self):
        self.rolePage = rolePage()

    def teardown(self):
        pass

    @allure.story("添加角色信息Api")
    @pytest.mark.parametrize('name,pageSize,pageNum',[("fang",1,100)])
    def test_insertrole(self,name,pageSize,pageNum):
        """添加角色信息 正例 """
        result = self.rolePage.insertrole(name=name)
        id = result['data']['id']
        try:
            self.rolePage.findByName(name=name,pageSize=pageSize,pageNum=pageNum)
        finally:
            self.rolePage.deleteRole(id=id)
        assert result['status'] == 200


    @allure.story("获取角色总数Api")
    def test_countAll(self):
        """ 获取角色总数 """
        result = self.rolePage.countAll()
        print(result)
        assert result['status'] == 200
        assert result['data'] != 0


    @allure.story("根据角色名称获取角色总数Api")
    @pytest.mark.parametrize('name',[("leader")])
    def test_countByName(self,name):
        """ 根据角色名称获取角色总数 """
        result = self.rolePage.countByName(name=name)
        print(result)
        assert result['status'] == 200
        assert result['data'] != 0

    @allure.story("根据角色名称获取角色列表Api")
    @pytest.mark.parametrize('name,pageNum,pageSize',[("leader",1,100)])
    def test_findByName(self,name,pageNum,pageSize):
        """ 根据角色名称获取角色列表 """
        result = self.rolePage.findByName(name=name,pageNum=pageNum,pageSize=pageSize)
        print(result)
        assert result['status'] == 200
        assert result['data']['list'] is not []

    @allure.story("获取角色列表Api")
    @pytest.mark.parametrize('pageNum,pageSize',[(1,100)])
    def test_findPage(self,pageNum,pageSize):
        """ 获取角色列表 """
        result = self.rolePage.findPage(pageSize=pageSize,pageNum=pageNum)
        assert result['status'] == 200
        assert result['data']['list'] is not []

    @allure.story("获取角色所有用户Api")
    @pytest.mark.parametrize('roleId',[(46923964773060608)])
    def test_getUsers(self,roleId):
        """ 获取角色所有用户"""
        result = self.rolePage.getUsers(roleId=roleId)
        print(result)
        assert result['status'] == 200
        assert result['data'] is not []

    @allure.story("获取角色信息Api")
    @pytest.mark.parametrize("id",[(46923964773060608)])
    def test_getRole(self,id):
        """ 获取角色信息 """
        result = self.rolePage.getRole(id=id)
        print(result)
        assert result['status'] == 200
        assert result['data'] is not []

    @allure.story("更新角色信息Api")
    @pytest.mark.parametrize("id,name",[(46923964773060608,"fffff")])
    def test_updateRole(self,id,name):
        """ 更新角色信息 """
        result = self.rolePage.updateRole(id=id,name=name)
        print(result)
        assert result['status'] == 200

    @allure.story("删除角色信息Api")
    @pytest.mark.parametrize('name,pageSize,pageNum',[("fang",1,100)])
    def test_deleteRole(self,name,pageSize,pageNum):
        """ 删除角色信息  正例 """
        try:
            self.rolePage.findByName(name=name, pageSize=pageSize, pageNum=pageNum)
        finally:
            pre = self.rolePage.insertrole(name=name)
            id = pre['data']['id']
        result = self.rolePage.deleteRole(id=id)
        assert result['status'] == 200

    @allure.story("获取角色所有权限Api")
    @pytest.mark.parametrize('roleId',[("46923964773060608")])
    def test_getPermissions(self,roleId):
        """ 获取角色所有权限"""
        result = self.rolePage.getPermissions(roleId=roleId)
        print(result)
        assert result['status'] == 200
        assert result['data'][0]['roleId'] == roleId

    @allure.story("删除角色下的一批权限Api")
    def test_batchDeletePermission(self):
        """ 删除角色下的一批权限 """
        permissionIds = [46923964773060608,46923964773060608]
        roleId = 46923964773060608
        result = self.rolePage.batchDeletePermission(permissionIds=permissionIds,roleId=roleId)
        assert result['status'] == 200


    @allure.story("批量添加角色权限Api")
    def test_batchInsertPermission(self):
        """批量添加角色权限 """
        permissionIds = [46961828034531328,47699566329352192]
        roleId = 46923964773060608
        try:
            result = self.rolePage.batchInsertPermission(permissionIds=permissionIds,roleId=roleId)
        finally:
            self.rolePage.batchDeletePermission(permissionIds=permissionIds,roleId=roleId)
        assert result['status'] == 200

    @allure.story("删除角色下的所有权限Api")
    def test_deleteAllPermission(self):
        """ 删除角色下的所有权限"""
        permissionIds = [46961828034531328, 47699566329352192]
        roleId = 46923964773060608
        try:
            self.rolePage.batchInsertPermission(permissionIds=permissionIds,roleId=roleId)
        finally:
            result = self.rolePage.batchDeletePermission(permissionIds=permissionIds, roleId=roleId)
        assert result['status'] == 200


    @allure.story("添加一个角色权限Api")
    @pytest.mark.parametrize("permissionIds,roleId",[(47699566329352192,46923964773060608)])
    def test_insertPermission(self,permissionIds,roleId):
        """添加一个角色权限 """
        try:
            result = self.rolePage.insertPermission(permissionIds=permissionIds,roleId=roleId)
            print(result)
        finally:
            self.rolePage.deletePermission(permissionIds=permissionIds, roleId=roleId)
        assert result['status'] == 200


    @allure.story("删除角色下的某个权限Api")
    @pytest.mark.parametrize("permissionIds,roleId",[(47699566329352192,46923964773060608)])
    def test_deletePermission(self,permissionIds,roleId):
        """ 删除角色下的某个权限 """
        result = self.rolePage.deletePermission(permissionIds=permissionIds,roleId=roleId)
        print(result)
        assert result['status'] == 200

    @allure.story("删除角色下的一批用户Api")
    def test_batchDeleteUser(self):
        """删除角色下的一批用户 """
        roleId = 47698094036373504
        userIds = [47696973842632704,47697000992362496]
        try:
            self.rolePage.batchInsertUser(roleId=roleId,userIds=userIds)
        finally:
            result = self.rolePage.batchDeleteUser(roleId=roleId, userIds=userIds)
        assert result['status'] == 200

    @allure.story("批量添加角色用户Api")
    def test_batchInsertUser(self):
        """批量添加角色用户 """
        roleId = 47698094036373504
        userIds = [47696973842632704,47697000992362496]
        try:
            result = self.rolePage.batchInsertUser(roleId=roleId,userIds=userIds)
        finally:
            self.rolePage.batchDeleteUser(roleId=roleId, userIds=userIds)
        assert result['status'] == 200

    @allure.story("删除角色下的所有用户Api")
    def test_deleteAllUser(self):
        """ 删除角色下的所有用户 """
        roleId = 47698094036373504
        result = self.rolePage.deleteAllUser(roleId=roleId)
        assert result['status'] == 200

    @allure.story("添加一个角色用户Api")
    @pytest.mark.parametrize("roleId,userIds",[(47699566329352192,46923964773060608)])
    def test_insertUser(self,roleId,userIds):
        """ 添加一个角色用户 """
        result = self.rolePage.insertUser(roleId=roleId,userIds=userIds)
        print(result)
        assert result['status'] == 200

    @allure.story("删除角色下的某个用户Api")
    @pytest.mark.parametrize("roleId,userIds",[(47699566329352192,46923964773060608)])
    def test_deleteUser(self,roleId,userIds):
        """ 删除角色下的某个用户 """
        result = self.rolePage.deleteUser(roleId=roleId,userIds=userIds)
        print(result)
        assert result['status'] == 200
