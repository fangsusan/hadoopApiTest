from common.Api import Api
import requests

class ResourcePage(Api):
    """ 资源管理接口"""
    def getResources(self):
        """根据获取所有资源"""
        r = requests.get(f'{self.url()}/api/resources/')
        return r.json()

    def queryResources(self,name,**kwargs):
        """根据条件获取资源列表"""
        data = {
            "name":name
        }
        data.update(kwargs)
        r = requests.post(f'{self.url()}/api/resources/',json=data)
        return r.json()


    def addResource(self,name,**kwargs):
        """添加资源 """
        data = {
            "name": name
        }
        data.update(kwargs)
        r = requests.put(f'{self.url()}/api/resources/', json=data)
        return r.json()

    def queryResourcesCount(self,name):
        """根据条件获取资源总数 """
        data = {
            "name": name
        }
        r = requests.post(f'{self.url()}/api/resources/count', json=data)
        return r.json()


    def queryResourcesPage(self,pageNum,pageSize):
        """根据条件获取一页资源"""
        data = {
        }
        r = requests.post(f'{self.url()}/api/resources/page/{pageNum}/{pageSize}',json=data)
        return r.json()

    def uploadResource(self):
        """上传资源文件 """
        pass


    def getResourceById(self,id):
        """根据ID获取资源"""
        r = requests.get(f'{self.url()}/api/resources/{id}')
        return r.json()


    def updateResource(self,id,name,**kwargs):
        """更新资源"""
        data = {
            "name":name,
        }
        data.update(kwargs)
        r = requests.post(f'{self.url()}/api/resources/{id}',json=data)
        return r.json()

    def deleteResource(self,id):
        """删除资源"""
        r = requests.delete(f"{self.url()}/api/resources/{id}")
        return r.json()
