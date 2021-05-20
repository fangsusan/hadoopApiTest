import requests

from common.Api import Api


class rolePage(Api):
    """ WitServer角色管理接口 """

    def insertrole(self,name):
        """添加角色信息 """
        data = {
                "name":name
        }
        r =requests.put(f"{self.url()}/api/role/",json=data)
        return  r.json()

    def countAll(self):
        """ 获取角色总数 """
        r = requests.get(f"{self.url()}/api/role/count")
        return r.json()

    def countByName(self,name):
        """ 根据角色名称获取角色总数 """
        r = requests.get(f"{self.url()}/api/role/count/name/{name}")
        return r.json()

    def findByName(self,name,pageNum,pageSize):
        """ 根据角色名称获取角色列表 """
        r = requests.get(f"{self.url()}/api/role/name/{name}/{pageSize}/{pageNum}")
        return r.json()

    def findPage(self,pageNum,pageSize):
        """ 获取角色列表 """
        r = requests.get(f"{self.url()}/api/role/page/{pageSize}/{pageNum}")
        return r.json()

    def getUsers(self,roleId):
        """ 获取角色所有用户"""
        r = requests.get(f"{self.url()}/api/role/users/{roleId}")
        return r.json()

    def getRole(self,id):
        """ 获取角色信息"""
        r = requests.get(f"{self.url()}/api/role/{id}")
        return r.json()

    def updateRole(self,id,name):
        """ 更新角色信息 """
        data = {
            "name":name
        }
        r = requests.post(f"{self.url()}/api/role/{id}",json=data)
        return r.json()

    def deleteRole(self,id):
        """ 删除角色信息 """
        r = requests.delete(f"{self.url()}/api/role/{id}")
        return r.json()

    def getPermissions(self,roleId):
        """ 获取角色所有权限"""
        r = requests.get(f"{self.url()}/api/role/{roleId}/permission")
        return r.json()


    def batchDeletePermission(self,permissionIds,roleId):
        """ 删除角色下的一批权限 """
        r = requests.post(f"{self.url()}/api/role/{roleId}/permission",json=permissionIds)
        return r.json()

    def batchInsertPermission(self,permissionIds,roleId):
        """批量添加角色权限 """
        r = requests.put(f"{self.url()}/api/role/{roleId}/permission",json=permissionIds)
        return r.json()

    def deleteAllPermission(self,roleId):
        """ 删除角色下的所有权限"""
        r = requests.delete(f"{self.url()}/api/role/{roleId}/permission")
        return r.json()

    def insertPermission(self,permissionIds,roleId):
        """添加一个角色权限 """
        r = requests.put(f"{self.url()}/api/role/{roleId}/permission/{permissionIds}")
        return r.json()


    def deletePermission(self,permissionIds,roleId):
        """ 删除角色下的某个权限 """
        r = requests.delete(f"{self.url()}/api/role/{roleId}/permission/{permissionIds}")
        return r.json()

    def batchDeleteUser(self,roleId,userIds):

        """删除角色下的一批用户 """
        r = requests.post(f"{self.url()}/api/role/{roleId}/user",json=userIds)
        return r.json()

    def batchInsertUser(self,roleId,userIds):
        """批量添加角色用户 """
        r = requests.post(f"{self.url()}/api/role/{roleId}/user", json=userIds)
        return r.json()

    def deleteAllUser(self,roleId):
        """ 删除角色下的所有用户 """
        r = requests.delete(f"{self.url()}/api/role/{roleId}/user")
        return r.json()

    def insertUser(self,roleId,userIds):
        """ 添加一个角色用户 """
        r = requests.put(f"{self.url()}/api/role/{roleId}/user/{userIds}")
        return r.json()

    def deleteUser(self,roleId,userIds):
        """ 删除角色下的某个用户 """
        r = requests.delete(f"{self.url()}/api/role/{roleId}/user/{userIds}")
        return r.json()

