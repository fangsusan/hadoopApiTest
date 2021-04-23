import requests
from Api import Api


class osfamilyPage(Api):

    def getOsFamilys(self):
        """获取所有系统类型"""
        r = requests.get(f"{self.url()}/api/osfamilys/")
        return r.json()

    def addOsFamily(self,family):
        """添加系统类型"""
        data = {
            "family":family,
        }
        r = requests.put(f"{self.url()}/api/osfamilys/",json=data)
        return r.json()

    def getOsFamilyCount(self,family):
        """根据条件获取系统类型总数"""
        data = {
            "family": family,
        }
        r = requests.post(f"{self.url()}/api/osfamilys/count", json=data)
        return r.json()

    def getByFamily(self,family):
        """根据名称获取系统类型"""
        r = requests.get(f"{self.url()}/api/osfamilys/family/{family}")
        return r.json()

    def queryOsFamilyPage(self,pageNum,pageSize,family):
        """根据条件获取系统类型列表"""
        data = {
            "family":family
        }
        r = requests.post(f"{self.url()}/api/osfamilys/page/{pageNum}/{pageSize}",json=data)
        return r.json()

    def queryOsFamilys(self,family):
        """根据条件获取系统类型列表(模糊查询)"""
        data = {
            "family":family
        }
        r = requests.post(f"{self.url()}/api/osfamilys/querise",json=data)
        return r.json()

    def getById(self,id):
        """根据ID获取系统类型"""
        r = requests.get(f"{self.url()}/api/osfamilys/{id}")
        return r.json()

    def updateOsFamily(self,id,family,**kwargs):
        """更新系统类型"""
        data = {
            "family":family
        }
        data.update(*kwargs)
        r = requests.post(f"{self.url()}/api/osfamilys/{id}",json=data)
        return r.json()

    def deleteOsFamily(self,id):
        """删除系统类型"""
        r = requests.delete(f"{self.url()}/api/osfamilys/{id}")
        return r.json()



