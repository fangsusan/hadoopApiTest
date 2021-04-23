import requests
from Api import Api

class SitePage(Api):

    def getsites(self):
        """获取所有站点"""
        r = requests.get(f"{self.url()}/api/sites/")
        return r.json()

    def addsite(self,name):
        """添加站点"""
        data = {
            "name":name
        }
        r = requests.put(f"{self.url()}/api/sites/",json=data)
        return r.json()

    def getsitecount(self,name,**kwargs):
        """根据条件获取站点总数"""
        data = {
            "name":name,
        }
        data.update(kwargs)
        r = requests.post(f"{self.url()}/api/sites/count",json=data)
        return r.json()

    def getSiteByName(self,name):
        """根据名称name获取站点"""
        r = requests.get(f"{self.url()}/api/sites/name/{name}")
        return r.json()

    def querySitePage(self,pageNum,pageSize,name):
        """根据条件获取站点列表(模糊查询)"""
        data = {
            "name":name,
        }
        r = requests.post(f"{self.url()}/api/sites/page/{pageNum}/{pageSize}",json=data)
        return r.json()

    def querySites(self,name):
        """根据条件获取站点列表(模糊查询)"""
        data = {
            "name":name
        }
        r =requests.post(f"{self.url()}/api/sites/querise",json=data)
        return r.json()

    def getSiteById(self,id):
        """根据ID获取站点"""
        r =requests.get(f"{self.url()}/api/sites/{id}")
        return r.json()

    def updatesite(self,id,name,**kwargs):
        """更新站点"""
        data = {
            "name":name
        }
        r = requests.post(f"{self.url()}/api/sites/{id}",json=data)
        return r.json()

    def deleteSite(self,id):
        """删除站点"""
        r = requests.delete(f"{self.url()}/api/sites/{id}")
        return r.json()