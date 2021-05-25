import allure
import pytest
from pageApi.clusterPage import clusterPage

@allure.feature("集群信息管理接口")
class Testcluster:
    """ 集群信息管理接口 """

    def setup(self):
        self.clusterPage = clusterPage()

    @allure.story('获取所有集群信息 Api')
    def test_getClusters(self):
        """ 获取所有集群信息   正例"""
        result = self.clusterPage.getClusters()
        assert result['status'] == 200
        assert result['data'] != 0


    @allure.story('添加集群信息 Api')
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

    @allure.story('启动/停止/重启集群服务组件 Api')
    @pytest.mark.parametrize("clusterId,componentId,state",[("meilanzi002","39654636168163328",1)])
    def test_startClusterComponent(self,clusterId,componentId,state):
        """启动/停止/重启集群服务组件
         state值为：0,1,2
        """
        result = self.clusterPage.startClusterComponent(clusterId=clusterId,componentId=componentId,state=state)
        assert result['status'] == 400


    @allure.story('获取集群服务组件post Api')
    @pytest.mark.parametrize("pageSize,pageNum",[(1,5)])
    def test_getClusterComponentsPage(self,pageSize,pageNum):
        """ 获取集群服务组件post 正例"""
        result = self.clusterPage.getClusterComponentsPage(pageSize=pageSize,pageNum=pageNum)
        print(result)
        assert  result['status'] ==200
        assert result['data'] != 0


    @allure.story('获取集群服务组件get Api')
    @pytest.mark.parametrize("clusterId,serviceId",[("35357258225291264","35396345778933761")])
    def test_getClusterComponents(self,clusterId,serviceId):
        """ 获取集群服务组件get 正例"""
        result = self.clusterPage.getClusterComponents(clusterId=clusterId,serviceId=serviceId)
        print(result)
        assert  result['status'] ==200
        assert result['data'] != 0

    @allure.story('根据条件获取集群总数 Api')
    @pytest.mark.parametrize("name",[("leicluster")])
    def test_getClusterCount(self,name):
        """ 根据条件获取集群总数 正例"""
        result = self.clusterPage.getClusterCount(name=name)
        print(result)
        assert result['status'] ==200
        assert result['data'] != 0

    @allure.story('根据ID获取集群主机 Api')
    @pytest.mark.parametrize("id", [("35358245971300352")])
    def test_getClusterHosts(self,id):
        """ 根据ID获取集群主机 正例"""
        result = self.clusterPage.getClusterHosts(clusterId=id)
        print(result)
        assert result['status'] == 200
        assert result['data'] != 0


    @allure.story('根据名称name获取集群主机 Api')
    @pytest.mark.parametrize("name", [("DATANODE")])
    def test_getClusterByName(self,name):
        """ 根据名称name获取集群主机 正例"""
        result = self.clusterPage.getClusterByName(name=name)
        print(result)
        assert result['status'] == 200

    @allure.story('根据条件获取集群列表 Api')
    @pytest.mark.parametrize("pageNum,pageSize", [(1,1)])
    def test_queryClusterPage(self,pageNum,pageSize):
        """ 根据条件获取集群列表 正例"""
        result = self.clusterPage.queryClusterPage(pageSize=pageSize,pageNum=pageNum)
        print(result)
        assert result['status'] == 200
        assert result['data'] != 0

    # @allure.story('安装集群服务组件 Api')
    # @pytest.mark.parametrize("clusterId,serviceId", [(49511843881832448,47021053267955712)])
    # def test_getClusterServiceConfig(self,clusterId,serviceId):
    #     """ 安装集群服务组件 """
    #     result = self.clusterPage.getClusterServiceConfig(clusterId=clusterId,serviceId=serviceId)
    #     print(result)
    #     assert result['status'] == 200

    @allure.story('获取集群服务 Api')
    @pytest.mark.parametrize("clusterId",[(45875034329206784)])
    def test_getClusterServices(self,clusterId):
        """ 获取集群服务 """
        result = self.clusterPage.getClusterServices(clusterId=clusterId)
        print(result)
        assert result['status'] == 200

    @allure.story('获取集群服务详情 Api')
    @pytest.mark.parametrize("clusterId,serviceId", [(45875034329206784,45875485170749440)])
    def test_getClusterService(self, clusterId,serviceId):
        """ 获取集群服务详情 """
        result = self.clusterPage.getClusterService(clusterId=clusterId,serviceId=serviceId)
        print(result)
        assert result['status'] == 200

    @allure.story('删除集群服务 Api')
    @pytest.mark.parametrize("clusterId,serviceId", [(45875034329206784,45875485170749440)])
    def test_deleteClusterService(self,clusterId,serviceId):
        """ 删除集群服务 """
        result = self.clusterPage.deleteClusterService(clusterId=clusterId,serviceId=serviceId)
        assert result['status'] == 200

    @allure.story('批量添加集群服务 Api')
    def test_addClusterServices(self):
        """ 批量添加集群服务 """
        clusterId = 49879018303934464
        stackId = 47021053267955712
        services = [45831284282380288,45831791520534528]
        result = self.clusterPage.addClusterServices(clusterId=clusterId,services=services,stackId=stackId)
        print(result)
        assert result['status'] == 400

    @allure.story('根据ID获取集群信息 Api')
    @pytest.mark.parametrize("id", [("49879018303934464")])
    def test_getClusterById(self,id):
        """ 根据ID获取集群信息    正例"""
        result = self.clusterPage.getClusterById(id=id)
        print(result)
        assert result['status'] == 200
        assert result['data']['id']  == id

    @allure.story('更新集群信息 Api')
    @pytest.mark.parametrize("id,name", [("49879018303934464","newname")])
    def test_updateCluster(self, name,id):
        """ 更新集群信息    正例"""
        result = self.clusterPage.updateCluster(id=id,name=name)
        print(result)
        assert result['status'] == 200


    @allure.story('删除集群信息 Api')
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







