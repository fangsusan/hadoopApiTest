import pytest

from pageApi.clusterPage import clusterPage


class Testcluster:
    def setup(self):
        self.clusterPage = clusterPage()

    def teardown(self):
        pass

    def test_getClusters(self):
        """ 获取所有集群信息   正例"""
        result = self.clusterPage.getClusters()
        assert result['status'] == 200
        assert result['data'] != 0

    @pytest.mark.parametrize("name,stackId",[("meilanzi002","39654636168163328")])
    def test_addCluster(self,name,stackId):
        """添加集群信息  正例"""
        result = self.clusterPage.addCluster(name=name,stackId=stackId)
        print(result)
        id = result['data']['id']
        try:
            self.clusterPage.getClusterByName(name=name)
        finally:
            self.clusterPage.deleteCluster(id=id)
        assert result['status'] == 200
        assert result['data']['name'] == name

    @pytest.mark.parametrize("pageSize,pageNum",[(1,5)])
    def test_getClusterComponentsPage(self,pageSize,pageNum):
        """ 获取集群服务组件post 正例"""
        result = self.clusterPage.getClusterComponentsPage(pageSize=pageSize,pageNum=pageNum)
        print(result)
        assert  result['status'] ==200
        assert result['data'] != 0

    @pytest.mark.parametrize("clusterId,serviceId",[("35357258225291264","35396345778933761")])
    def test_getClusterComponents(self,clusterId,serviceId):
        """ 获取集群服务组件get 正例"""
        result = self.clusterPage.getClusterComponents(clusterId=clusterId,serviceId=serviceId)
        print(result)
        assert  result['status'] ==200
        assert result['data'] != 0

    @pytest.mark.parametrize("name",[("meilanzi001")])
    def test_getClusterCount(self,name):
        """ 根据条件获取集群总数 正例"""
        result = self.clusterPage.getClusterCount(name=name)
        print(result)
        assert  result['status'] ==200
        assert result['data'] != 0

    @pytest.mark.parametrize("id", [("35358245971300352")])
    def test_getClusterHosts(self,id):
        """ 根据ID获取集群主机 正例"""
        result = self.clusterPage.getClusterHosts(clusterId=id)
        print(result)
        assert result['status'] == 200
        assert result['data'] != 0


    @pytest.mark.parametrize("name", [("DATANODE")])
    def test_getClusterByName(self,name):
        """ 根据名称name获取集群主机 正例"""
        result = self.clusterPage.getClusterByName(name=name)
        print(result)
        assert result['status'] == 200



    @pytest.mark.parametrize("pageNum,pageSize", [(1,1)])
    def test_queryClusterPage(self,pageNum,pageSize):
        """ 根据条件获取集群列表 正例"""
        result = self.clusterPage.queryClusterPage(pageSize=pageSize,pageNum=pageNum)
        print(result)
        assert result['status'] == 200
        assert result['data'] != 0

    @pytest.mark.parametrize("id", [("40401700057530368")])
    def test_getClusterById(self,id):
        """ 根据ID获取集群信息    正例"""
        result = self.clusterPage.getClusterById(id=id)
        print(result)
        assert result['status'] == 200
        assert result['data']['id']  == id

    @pytest.mark.parametrize("id", [("40401700057530368")])
    def test_updateCluster(self, id):
        """ 更新集群信息    正例"""
        result = self.clusterPage.updateCluster(id=id)
        print(result)
        assert result['status'] == 200
        assert result['data']['id'] == id

    @pytest.mark.parametrize("id,name,stackId", [("40401700057530368","meilanzi002","39654636168163328")])
    def test_deleteCluster(self,id,name,stackId):
        """ 删除集群信息    正例"""
        try:
            self.clusterPage.getClusterById(id=id)
        finally:
            pre = self.clusterPage.addCluster(name=name, stackId=stackId)
            id = pre['data']['id']

        result = self.clusterPage.deleteCluster(id=id)
        print(result)
        assert result['status'] == 200

    # @pytest.mark.parametrize("clusterId,serviceId)",[("35358245971300352","35400276559007744")])
    # def test_getClusterServiceConfig(self,clusterId,serviceId):
    #     """ 获取集群主机指定服务组件的配置列表 正例"""
    #     result = self.clusterPage.getClusterServiceConfig(clusterId=clusterId,serviceId=serviceId)
    #     print(result)
    #     assert result['status'] == 200
    #     # assert result['data'] != 0
    #
    # @pytest.mark.parametrize("clusterId,serviceId)", [("35358245971300352", "35400276559007744")])
    # def test_installClusterService(self,clusterId,serviceId):
    #     """ 安装集群服务组件 正例"""
    #     result = self.clusterPage.installClusterService(clusterId=clusterId,serviceId=serviceId)
    #     print(result)
    #     assert result['status'] == 200
    #     # assert result['data'] != 0








