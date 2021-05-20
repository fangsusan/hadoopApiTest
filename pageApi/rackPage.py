import requests

from common.Api import Api

class RackPage(Api):

    def getRacks(self):
        """获取所有站点"""
        r = requests.get(f"{self.url()}/api/racks/")
        return r.json()

    def addRacks(self,siteId,name):
        """添加机架 siteId,name 必填"""
        data = {
            "siteId":siteId,
            "name":name,
        }
        r = requests.put(f"{self.url()}/api/racks/",json=data)
        return r.json()


    def getRackCount(self,name):
        """根据条件获取站点总数"""
        data = {
            "name":name
        }
        r =requests.post(f"{self.url()}/api/racks/count/",json=data)
        return r.json()

    def getRackByName(self,name):
        """根据名称获取机架"""
        r = requests.get(f"{self.url()}/api/racks/name/{name}")
        return r.json()

    def queryRackPage(self,pageNum,pageSize,name):
        """根据条件获取机架列表(模糊)"""
        data = {
            "name": name
        }
        r = requests.post(f"{self.url()}/api/racks/page/{pageNum}/{pageSize}", json=data)
        return r.json()

    def queryRacks(self,name):
        """根据条件获取机架列表(模糊查询) """
        data = {
            "name": name
        }
        r = requests.post(f"{self.url()}/api/racks/querise/", json=data)
        return r.json()

    def getRackById(self,id):
        """根据ID获取机架 """
        r = requests.get(f"{self.url()}/api/racks/{id}")
        return r.json()

    def updaterack(self,name,id):
        """更新机架 """
        data = {
            "name": name
        }
        r = requests.post(f"{self.url()}/api/racks/{id}", json=data)
        return r.json()

    def deleteRack(self,id):
        """删除机架 """
        r = requests.delete(f"{self.url()}/api/racks/{id}")
        return r.json()
