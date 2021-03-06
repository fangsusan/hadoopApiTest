import requests
from common.Api import Api

class clusterPage(Api):
    """ 集群信息管理接口"""
    def getClusters(self):
        """ 获取所有集群信息 """
        r = requests.get(f'{self.url()}/api/clusters/')
        return r.json()

    def addCluster(self,name,stackId):
        """添加集群信息 """
        data = {
            "name":name,
            "stackId":stackId
        }
        r =requests.put(f"{self.url()}/api/clusters/",json=data)
        return r.json()

    def startClusterComponent(self,clusterId,componentId,state):
        """启动/停止/重启集群服务组件 """
        r = requests.get(f"{self.url()}/api/clusters/components/action/{clusterId}/{componentId}/{state}")
        return r.json()


    def getClusterComponentsPage(self,pageNum,pageSize):
        """ 获取集群服务组件 post"""
        data = {

        }
        r = requests.post(f"{self.url()}/api/clusters/components/page/{pageNum}/{pageSize}", json=data)
        return r.json()

    def getClusterComponents(self,clusterId,serviceId):
        """ 获取集群服务组件 get"""
        r = requests.get(f"{self.url()}/api/clusters/components/{clusterId}/{serviceId}")
        return r.json()

    def getClusterCount(self,name,**kwargs):
        """ 根据条件获取集群总数"""
        data = {
            "name":name
        }
        data.update(kwargs)
        r = requests.post(f"{self.url()}/api/clusters/count",json=data)
        return r.json()

    def getClusterHosts(self,clusterId):
        """ 获取集群主机"""
        r = requests.get(f"{self.url()}/api/clusters/hosts/{clusterId}")
        return r.json()

    def getClusterByName(self,name):
        """ 根据名称获取集群"""
        r = requests.get(f"{self.url()}/api/clusters/name/{name}")
        return r.json()

    def queryClusterPage(self,pageNum,pageSize):
        """ 根据条件获取集群列表"""
        data = {

        }
        r = requests.post(f"{self.url()}/api/clusters/page/{pageNum}/{pageSize}",json=data)
        return r.json()

    def getClusterServiceConfig(self,clusterId,serviceId):
        """ 获取集群主机指定服务组件的配置列表 """
        r = requests.get(f"{self.url()}/api/clusters/services/install/{clusterId}/{serviceId}")
        return r.json()

    def installClusterService(self,clusterId,serviceId):
        """ 安装集群服务组件 """
        r = requests.get(f"{self.url()}/api/clusters/services/install/{clusterId}/{serviceId}")
        return r.json()

    def getClusterServices(self,clusterId):
        """ 获取集群服务 """
        r = requests.get(f"{self.url()}/api/clusters/services/{clusterId}")
        return r.json()

    def getClusterService(self, clusterId,serviceId):
        """ 获取集群服务详情 """
        r = requests.get(f"{self.url()}/api/clusters/services/{clusterId}/{serviceId}")
        return r.json()

    def deleteClusterService(self, clusterId, serviceId):
        """ 删除集群服务 """
        r = requests.delete(f"{self.url()}/api/clusters/services/{clusterId}/{serviceId}")
        return r.json()

    def addClusterServices(self,clusterId,stackId,services):
        """ 批量添加集群服务 """
        r = requests.put(f"{self.url()}/api/clusters/services/{clusterId}/{stackId}",json=services)
        return r.json()

    def getClusterById(self, id):
        """ 获取集群信息 """
        r = requests.get(f"{self.url()}/api/clusters/{id}")
        return r.json()

    def updateCluster(self,name,id):
        """ 更新集群信息 """
        data = {
            "name":name,
        }
        r = requests.post(f"{self.url()}/api/clusters/{id}",json=data)
        return r.json()

    def deleteCluster(self, id):
        """ 删除集群信息 """
        r = requests.delete(f"{self.url()}/api/clusters/{id}")
        return r.json()