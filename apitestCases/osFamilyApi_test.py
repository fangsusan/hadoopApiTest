import pytest

from pageApi.osfamilyPage import osfamilyPage

class TestosFamilyApi:
    def setup(self):
        self.osfamilyPage = osfamilyPage()

    def teardown(self):
        pass

    def test_getOsFamilys(self):
        """获取所有系统类型"""
        result = self.osfamilyPage.getOsFamilys()
        assert result['status'] == 200

    @pytest.mark.parametrize("family",[("fang002")])
    def test_addOsFamily(self,family):
        """添加系统类型    正例"""
        result = self.osfamilyPage.addOsFamily(family=family)
        id = result["data"]["id"]

        try:
            # self.osfamilyPage.getByFamily(family=family)
            self.osfamilyPage.getById(id=id)
        finally:
            self.osfamilyPage.deleteOsFamily(id=id)
        print(result)
        assert result['status'] == 200

    @pytest.mark.parametrize("family",[("fang001")])
    def test_getOsFamilyCount(self,family):
        """根据条件获取系统类型总数   正例"""
        result = self.osfamilyPage.getOsFamilyCount(family=family)
        print(result)
        assert result['status'] == 200
        assert result['data']  != 0

    @pytest.mark.parametrize("family",[("fang001")])
    def test_getByFamily(self,family):
        """根据名称获取系统类型  正例"""
        result = self.osfamilyPage.getByFamily(family=family)
        # assert result['data'] != 0
        assert result['status'] == 200


    @pytest.mark.parametrize("pageNum,pageSize,family",[(1,1,"fang001")])
    def test_queryOsFamilyPage(self,pageNum,pageSize,family,**kwargs):
        """根据条件获取系统类型列表  正例"""
        result = self.osfamilyPage.queryOsFamilyPage(pageNum=pageNum,pageSize=pageSize,family=family)
        print(result)
        assert result['status'] == 200
        assert result['data']['list'][0]["family"] == family

    @pytest.mark.parametrize("family",[("fang")])
    def test_queryOsFamilys(self,family):
        """根据条件获取系统类型列表(模糊查询)   正例"""
        result = self.osfamilyPage.queryOsFamilys(family=family)
        print(result)
        assert result['status'] == 200
        assert result['data'][0]['family'] != family  # 模糊查询

    @pytest.mark.parametrize("id",[("35343191389507584")])
    def test_getById(self,id):
        """根据ID获取系统类型   正例"""
        result = self.osfamilyPage.getById(id=id)
        assert result['status'] == 200
        assert result['data']['id'] == id

    @pytest.mark.parametrize("family,id",[("fang","40812487070724096")])
    def test_updateOsFamily(self,id,family):
        """更新系统类型  正例"""
        result = self.osfamilyPage.updateOsFamily(id=id,family=family)
        assert result['status'] == 200

    @pytest.mark.parametrize("family",[("fang005")])
    def test_deleteOsFamily(self,family):
        """删除系统类型  正例"""
        try:
            self.osfamilyPage.getByFamily(family=family)
        finally:
            preid = self.osfamilyPage.addOsFamily(family=family)
            id = preid["data"]["id"]

        result = self.osfamilyPage.deleteOsFamily(id=id)
        assert result['status'] == 200


