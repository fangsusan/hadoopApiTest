import pytest
import requests
from Api import Api

class StackPage(Api):
    def getStacks(self):
        """获取所有技术栈接口"""

        r = requests.get(f"{self.url()}/api/stacks/")
        return r.json()

    def queryStacks(self,hostname,version,**kwargs):
        """根据hostname获取技术栈列表"""
        urlnew = f"{self.url()}/api/stacks/"
        data = {
            "hostname":hostname,
            "version":version,
         }
        data.update(kwargs)
        r = requests.post(url=urlnew,json=data)
        return r.json()

    def addStack(self,name,version,**kwargs):
        """ 添加技术栈"""
        data = {
             "name":name,
             "version":version,
        }
        data.update(kwargs)
        r = requests.put(f"{self.url()}/api/stacks/",json=data)
        return r.json()

    def queryStackCount(self, id, **kwargs):
        """ 按条件获取技术栈总数"""

        data = {
            "id": id
        }
        data.update(kwargs)
        r = requests.post(f"{self.url()}/api/stacks/count", json=data)
        return r.json()

    def queryStacksPage(self, pageNum, pageSize, name, **kwargs):
        """ 按page页码查询询技术栈总数"""
        urlnew = f"{self.url()}/api/stacks/page/{pageNum}/{pageSize}"
        data = {
            "name": name,
        }
        data.update(kwargs)
        r = requests.post(url=urlnew, json=data)
        return r.json()

    def getStackByid(self,id):
        """ 按ID获取技术栈"""
        r = requests.get(f"{self.url()}/api/stacks/{id}")
        return r.json()

    def updateStack(self,id,name,**kwargs):
        """ 更新技术栈"""
        data = {
            "name":name,
        }

        data.update(kwargs)
        r = requests.post(f"{self.url()}/api/stacks/{id}",json=data)
        return r.json()

    def deleteStack(self,id):
        """ 根据id删除技术栈"""
        r = requests.delete(f"{self.url()}/api/stacks/{id}")
        return r.json()

    def getStackDetaiByid(self,id):
        """ 根据Id获取技术栈详情"""
        r = requests.get(f"{self.url()}/api/stacks/{id}/detail")
        return r.json()