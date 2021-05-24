from common.Api import Api
import requests

class HostsPage(Api):
    """ 主机管理接口"""

    def gethosts(self):
        """ 获取所有主机 """
        r = requests.get(f"{self.url()}/api/hosts/")
        print(r)
        return r.json()

    def addHost(self,hostname,clusterId,osId,osVer,rackId,siteId):
        """添加主机,必填项hostname"""
        data = {
                 "hostname": hostname,
                 "clusterId":clusterId,
                 "osId":osId,
                 "osVer":osVer,
                 "rackId":rackId,
                 "siteId":siteId
                  }
        r = requests.put(f"{self.url()}/api/hosts/",json=data)
        return r.json()

    def addClusterHosts(self,clusterId,hostsIds):
        """批量添加集群主机"""

        r = requests.put(f"{self.url()}/api/hosts/cluster/{clusterId}",json=hostsIds)
        return r.json()


    def deleteClusterHosts(self,clusterId,hostsIds):
        """批量删除集群主机"""
        r = requests.delete(f"{self.url()}/api/hosts/cluster/{clusterId}", json=hostsIds)
        return r.json()

    def getHostCount(self,name):
        """根据条件获取主机总数"""
        data = {
            "name":name
        }
        r = requests.post(f"{self.url()}//api/hosts/count",json=data)
        return r.json()

    def getHostByHostname(self,hostname):
        """根据名称获取主机"""
        result = requests.get(f"{self.url()}/api/hosts/hostname/{hostname}")
        return result.json()

    def queryhostPage(self,hostname,pageNum,pageSize):
        """根据条件获取主机列表(模糊)"""
        data = {
            "hostname":hostname
        }
        r = requests.post(f"{self.url()}/api/hosts/page/{pageNum}/{pageSize}",json=data)
        return r.json()

    def getHostPageClusterIsNUll(self,hostname,pageNum,pageSize):
        """获取集群ID为空的主机"""
        data = {
            "hostname": hostname
        }
        r = requests.post(f"{self.url()}/api/hosts/page/{pageNum}/{pageSize}/clusterIsNull", json=data)
        return r.json()

    def queryHosts(self,hostname):
        """根据条件获取主机列表(模糊查询)"""
        data = {
            "hostname": hostname
        }
        r = requests.post(f"{self.url()}/api/hosts/querise", json=data)
        return r.json()

    def getHostById(self,id):
        """根据ID获取主机"""
        r = requests.get(f"{self.url()}/api/hosts/hostname/{id}")
        return r.json()

    def updateHost(self,id,hostname,clusterId,osId,osVer,rackId,siteId):
        """更新主机"""

        data = {
            "hostname":hostname,
            "clusterId": clusterId,
            "osId": osId,
            "osVer": osVer,
            "rackId":rackId,
            "siteId":siteId,
        }
        r = requests.post(f"{self.url()}/api/hosts/{id}",json=data)
        return r.json()

    def deleteHost(self,id):
        """ 根据Id删除主机"""
        r = requests.delete(f"{self.url()}/api/hosts/{id}")
        return r.json()
