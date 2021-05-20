import requests

from common.Api import Api


class systemResourcePage(Api):
    """ WitServer系统资源管理接口"""

    def getResources(self):
        """ 获取所有资源 """
        r = requests.get(f"{self.url()}/api/system/resource/")
        return r.json()

    def insertSystemresource(self,name,**kwargs):
        """ 添加系统资源信息"""
        data = {
            "name":name
        }
        r =requests.put(f"{self.url()}/api/system/resource/",json=data)
        return r.json()

    def countAll(self):
        """ 获取资源总数"""
        r = requests.get(f"{self.url()}/api/system/resource/count")
        return r.json()


    def countByName(self,name):
        """ 根据资源名称获取资源总数"""
        r = requests.get(f"{self.url()}/api/system/resource/count/name/{name}")
        return r.json()

    def countByType(self,type):
        """ 根据资源类型获取资源总数"""
        r = requests.get(f"{self.url()}/api/system/resource/count/type/{type}")
        return r.json()

    def findByName(self,name,pageNum,pageSize):
        """ 根据资源名称获取资源列表"""
        r = requests.get(f"{self.url()}/api/system/resource/name/{name}/{pageSize}/{pageNum}")
        return r.json()

    def findPage(self,pageNum,pageSize):
        """ 获取资源列表 """
        r = requests.get(f"{self.url()}/api/system/resource/page/{pageSize}/{pageNum}")
        return r.json()

    def findByType(self,type,pageNum,pageSize):
        """ 根据资源类型获取资源列表 """
        r = requests.get(f"{self.url()}/api/system/resource/type/{type}/{pageSize}/{pageNum}")
        return r.json()

    def getSystemResource(self,id):
        """ 获取资源信息 """
        r = requests.get(f"{self.url()}/api/system/resource/{id}")
        return r.json()

    def updateSystemResource(self,id,name,**kwargs):
        """ 更新资源信息 """
        data = {
                "name":name
        }
        data.update(kwargs)
        r = requests.post(f"{self.url()}/api/system/resource/{id}",json=data)
        return r.json()

    def deleteystemResource(self,id):
        """ 删除资源信息 """
        r = requests.delete(f"{self.url()}/api/system/resource/{id}")
        return r.json()
