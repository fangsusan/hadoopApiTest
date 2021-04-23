import pytest
import requests
from pageApi.stackPage import StackPage

class TestStack:
    def setup_class(self):
        self.StackPage = StackPage()

    def test_getStack(self):
        """ 测试获取所有技术栈信息  正例"""
        r = self.StackPage.getStacks()
        assert r["status"] == 200

    @pytest.mark.parametrize("hostname,version",[("fang002",1.0)])
    def test_queryStacks(self,hostname,version):
        """ 测试按name查询技术栈   正例"""
        r = self.StackPage.queryStacks(hostname=hostname,version=version)
        print(r)
        assert r["status"] == 200

    @pytest.mark.parametrize("name,pageNum,pageSize", [("fang001",1,1)])
    def test_queryStacksPage(self,name,pageNum,pageSize):
        """根据条件name获取技术栈列表  正例"""
        r = self.StackPage.queryStacksPage(pageNum=pageNum,pageSize=pageSize,name=name)
        print(r)
        assert r["status"] == 200
        assert r['data']["list"][0]["name"] == name


    @pytest.mark.parametrize("name,version", [("meilanzi001",1.1)])
    def test_addStacks(self,name,version):
        """ 测试添加技术栈,name，version为必填项   正例"""
        r = self.StackPage.addStack(name=name,version=version)
        print(r)
        id = r["data"]["id"]
        try:
            self.StackPage.queryStacks(hostname=name,version=version)
        finally:
            self.StackPage.deleteStack(id=id)
        assert r["status"] == 200
        assert r["data"]["name"] == name

    def test_queryStackCount(self):
        """ 测试按id获取技术栈总数  正例"""

        id = 40009049269350400
        r = self.StackPage.queryStackCount(id=id)
        print(r)
        assert r["status"] == 200

    def test_getStackByid(self):
        """ 测试按ID获取技术栈  正例"""
        id = "40009049269350400"
        r = self.StackPage.getStackByid(id=id)
        print(r)
        assert r["status"] == 200
        assert r["data"]['id'] == id

    @pytest.mark.parametrize("updatename,id", [("newname","40009487595089920")])
    def test_updateStack(self,updatename,id):
        """ 测试更新技术栈  正例"""
        result = self.StackPage.updateStack(id=id,name=updatename)
        assert result["status"] == 200
        # assert result['data']["name"] == updatename


    @pytest.mark.parametrize("name,version", [("meilanzi001",1.1)])
    def test_deleteStack(self,name,version):
        """ 测试删除技术栈 正例"""
        try:
            self.StackPage.queryStacks(hostname=name,version=version)
        finally:
            preid = self.StackPage.addStack(name=name,version=version)
            id = preid["data"]["id"]
        r = self.StackPage.deleteStack(id=id)
        assert r["status"] == 200

    @pytest.mark.parametrize("id", [(35343265364447232)])
    def test_getStackDetailById(self,id):
        """ 测试根据Id获取技术栈详情  正例"""
        r = self.StackPage.getStackDetaiByid(id=id)
        print(r)
        assert  r["status"] == 200
        assert r['data']['name'] == 'Wit'