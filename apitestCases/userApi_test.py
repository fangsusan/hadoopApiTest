import pytest

from pageApi.userPage import userPage


class Testuser:
    """ WitServer 用户管理接口  测试"""
    def setup(self):
        self.userPage = userPage()

    def teardown(self):
        pass

    @pytest.mark.parametrize("password,salt,username,pageSize,pageNum",[("123789","salt","fyj001",1,10)])
    def test_insert(self,password,salt,username,pageSize,pageNum):
        """ 添加用户信息 正例"""

        result = self.userPage.insert(password=password,salt=salt,username=username)
        id = result['data']['id']
        try:
            self.userPage.findByName(name=username,pageSize=pageSize,pageNum=pageNum)
        finally:
            self.userPage.deleteUser(id=id)
        assert result['status'] == 200


    def test_countAll(self):
        """ 获取用户总数 正例"""
        result = self.userPage.countAll()
        assert result['status'] == 200
        assert result['data'] != 0

    @pytest.mark.parametrize("name",[("meilanzi")])
    def test_countByName(self,name):
        """ 根据用户名称获取用户总数 正例"""
        result = self.userPage.countByName(name=name)
        print(result)
        assert result['status'] == 200
        assert result['data'] != 0

    @pytest.mark.parametrize("name,pageSize,pageNum", [("meilanzi",1,10)])
    def test_findByName(self, name,pageSize,pageNum):
        """ 根据用户名称获取用户列表 正例"""
        result = self.userPage.findByName(name=name,pageSize=pageSize,pageNum=pageNum)
        print(result)
        assert result['status'] == 200
        assert result['data']['name'] ==name

    @pytest.mark.parametrize("pageSize,pageNum",[(1,10)])
    def test_findPage(self,pageSize, pageNum):
        """ 获取用户列表 正例"""
        result = self.userPage.findPage(pageSize=pageSize, pageNum=pageNum)
        print(result)
        assert result['status'] == 200

    @pytest.mark.parametrize("id",[("42172949280604160")])
    def test_getUser(self,id):
        """ 获取用户信息 正例"""
        result = self.userPage.getUser(id=id)
        print(result)
        assert result['status'] == 200

    @pytest.mark.parametrize("id,name", [("42172949280604160","meilanzi new")])
    def test_updateUser(self,id,name):
        """ 更新用户信息 正例"""
        result = self.userPage.updateUser(id=id,name=name)
        print(result)
        assert result['status'] == 200
        assert result['data']['name'] == name

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



#     批量操作待写




