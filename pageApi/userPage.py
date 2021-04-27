import requests

from Api import Api


class userPage(Api):
    """ WitServer 用户管理接口"""

    def insert(self,password,salt,username,**kwargs):
        """添加用户信息"""
        data = {
                "password":password,
                "salt":salt,
                "username":username,
            }
        data.update(kwargs)
        r = requests.put(f"{self.url()}/api/user/",json=data)
        return r.json()

    def countAll(self):
        """ 获取用户总数"""
        r = requests.get(f"{self.url()}/api/user/count")
        return r.json()

    def countByName(self,name):
        """根据用户名称获取用户总数"""
        r = requests.get(f"{self.url()}/api/user/count/name/{name}")
        return r.json()

    def findByName(self,name,pageNum,pageSize):
        """根据用户名称获取用户列表"""
        r = requests.get(f"{self.url()}/api/user/name/{name}/{pageSize}/{pageNum}")
        return r.json()

    def findPage(self,pageNum,pageSize):
        """获取用户列表"""
        r = requests.get(f"{self.url()}/api/user/page/{pageSize}/{pageNum}")
        return r.json()

    def getUser(self,id):
        """获取用户信息"""
        r = requests.get(f"{self.url()}/api/user/{id}")
        return r.json()

    def updateUser(self,id,name,**kwargs):
        """更新用户信息 """
        data = {
                "name":name
        }
        data.update(kwargs)
        r = requests.post(f"{self.url()}/api/user/{id}",json=data)
        return r.json()

    def deleteUser(self,id):
        """ 删除用户信息 """
        r =requests.delete(f"{self.url()}/api/user/{id}")
        return r.json()


    def delete(self,userId,password,salt,username,**kwargs):
        """批量添加用户角色"""
        data = {
            "password": password,
            "salt": salt,
            "username": username,
        }
        data.update(kwargs)
        r = requests.put(f"{self.url()}/api/user/{userId}/user",json=data)
        return r.json()

    def batchInsertRole(self,roleId):
        """批量添加用户角色"""
        r = requests.put(f"{self.url()}/api/user/{roleId}/user")
        return  r.json()


    def batchDeleteRole(self,userId,roleIds):
        """删除用户下的一批角色"""
        r = requests.post(f"{self.url()}/api/user/{userId}/role")
        return r.json()

    def deleteAllRole(self,userId):
        """删除用户下的所有角色"""

        r = requests.delete(f"{self.url()}/api/user/{userId}/role")
        return r.json()

    def insertRole(self,userId,roleId):
        """添加一个用户角色"""
        r = requests.put(f"{self.url()}/api/user/{userId}/user/{roleId}")
        return r.json()

    def deleteRole(self,userId,roleId):
        """删除用户下的某个角色"""
        r = requests.delete(f"{self.url()}/api/user/{userId}/user/{roleId}")
        return r.json()

