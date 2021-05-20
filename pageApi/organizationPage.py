import requests

from common.Api import Api


class organizationPage(Api):
    """ WitServer 组织管理接口"""
    def getOrganizations(self):
        """ 获取所有组织"""
        r = requests.get(f"{self.url()}/api/organization/")
        return r.json()

    def insert(self,name):
        """ 添加组织信息"""
        data = {
            "name":name
        }
        r = requests.put(f"{self.url()}/api/organization/",json=data)
        return r.json()

    def countAll(self):
        """ 获取组织总数 """

        r = requests.get(f"{self.url()}/api/organization/count")
        return r.json()

    def countByName(self,name):
        """根据组织名称获取组织总数 """
        r = requests.get(f"{self.url()}/api/organization/count/name/{name}")
        return r.json()

    def findByName(self,name,pageNum,pageSize):
        """ 根据组织名称获取组织列表 """
        r = requests.get(f"{self.url()}/api/organization/name/{name}/{pageNum}/{pageSize}")
        return r.json()

    def findPage(self,pageNum,pageSize):
        """ 获取组织列表 """
        r = requests.get(f"{self.url()}/api/organization/page/{pageNum}/{pageSize}")
        return r.json()

    def getUsers(self,organizationId):
        """ 获取组织所有用户"""
        r = requests.get(f"{self.url()}/api/organization/users/{organizationId}")
        return r.json()

    def getOranization(self,id):
        """ 获取组织信息 """
        r = requests.get(f"{self.url()}/api/organization/{id}")
        return r.json()

    def updateOrganization(self,id,name,**kwargs):
        """ 更新组织信息 """
        data = {
            name:name,
        }
        data.update(kwargs)
        r = requests.post(f"{self.url()}/api/organization/{id}",json=data)
        return r.json()

    def deleteOrganization(self,id):
        """删除组织信息 """
        r = requests.delete(f"{self.url()}/api/organization/{id}")
        return r.json()

    def insertUser(self,organizationId,userId):
        """ 添加一个组织用户 """
        r = requests.put(f"{self.url()}/api/organization/{organizationId}/user/{userId}")
        return  r.json()

    def deleteUser(self,organizationId,userId):
        """ 删除组织下某个用户 """
        r = requests.delete(f"{self.url()}/api/organization/{organizationId}/user/{userId}")
        return  r.json()

    def batchDeleteUser(self,organizationId,userIds):
        """ 删除组织下的一批用户 """
        r = requests.post(f"{self.url()}/api/organization/{organizationId}/user",json=userIds)
        return r.json()

    def batchInsertUser(self,organizationId,userIds):
        """ 批量添加组织用户 """
        r = requests.put(f"{self.url()}/api/organization/{organizationId}/user", json=userIds)
        return r.json()

    def deleteAllUser(self,organizationId):
        """删除组织下的所有用户 """
        r = requests.delete(f"{self.url()}/api/organization/{organizationId}/user")
        return r.json()