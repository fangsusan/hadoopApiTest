import allure
import requests

from Api import Api


class userPage(Api):
    """ WitServer 用户管理接口"""

    def getUsers(self):
        """获取所有用户 """

        r = requests.get(f"{self.url()}/api/user/",headers=self.get_headers())
        return r.json()

    def login(self,username,password):
        """用户登录"""
        data = {
            "username":username,
            "password":password
        }
        r = requests.post(f"{self.url()}/api/user/auth",json=data)
        return r.json()

    def logout(self):
        r = requests.get(f"{self.url()}/api/user/auth")
        return r.json()

    def insert(self,name,phone,email,username,password,**kwargs):
        """添加用户信息 （admin账号才有的权限）"""
        data = {
            "name":name,
            "phone":phone,
            "email":email,
            "username": username,
            "password":password,
            }
        data.update(kwargs)
        r = requests.put(f"{self.url()}/api/user/",json=data,headers=self.get_adminheaders())
        return r.json()

    def countAll(self):
        """ 获取用户总数"""

        r = requests.get(f"{self.url()}/api/user/count",headers=self.get_headers())
        return r.json()

    def countByName(self,name):
        """根据用户名称获取用户总数"""

        r = requests.get(f"{self.url()}/api/user/count/name/{name}",headers=self.get_headers())
        return r.json()

    def findByName(self,name,pageNum,pageSize):
        """根据用户名称获取用户列表"""
        r = requests.get(f"{self.url()}/api/user/name/{name}/{pageSize}/{pageNum}",headers=self.get_headers())
        return r.json()

    def getOrganizations(self,userId):
        """获取用户所有组织"""
        r = requests.get(f"{self.url()}/api/user/organizations/{userId}",headers=self.get_headers())
        return r.json()

    def findPage(self,pageNum,pageSize):
        """获取用户列表"""
        r = requests.get(f"{self.url()}/api/user/page/{pageSize}/{pageNum}",headers=self.get_headers())
        return r.json()

    def adminchangePwd(self,username,password):
        """管理员修改密码"""
        data ={
            "password":password,
            "username":username
        }
        r = requests.post(f"{self.url()}/api/user/pwd",json=data,headers=self.get_adminheaders())
        return r.json()


    def changePwd(self,username,password):
        """普通用户修改密码"""
        data ={
            "password":password,
            "username":username
        }
        r = requests.post(f"{self.url()}/api/user/pwd",json=data,headers=self.get_headers())
        return r.json()

    def getUser(self,id):
        """获取用户信息"""
        r = requests.get(f"{self.url()}/api/user/{id}",headers=self.get_headers())
        return r.json()

    def updateUser(self,id,realname,phone,email,**kwargs):
        """更新用户信息 """
        data = {
            "id":id,
            "realname":realname,
            "phone":phone,
            "email":email
        }
        data.update(kwargs)
        r = requests.post(f"{self.url()}/api/user/{id}",json=data,headers=self.get_adminheaders())
        return r.json()

    def changeUserStatus(self,id,status):
        """ 禁用/启用用户"""
        r = requests.get(f"{self.url()}/api/user/{id}/{status}",headers=self.get_adminheaders())
        return r.json()

    def getPermissions(self,userId):
        """获取用户所有权限 """
        r = requests.get(f"{self.url()}/api/user/{userId}/permission",headers=self.get_adminheaders())
        return r.json()

    def getRoles(self,userId):
        """获取用户所有角色 """
        r = requests.get(f"{self.url()}/api/user/{userId}/role",headers=self.get_headers())
        return r.json()

    def batchInsertRole(self,userId,roleIds):
        """批量添加用户角色"""
        data = roleIds
        r = requests.put(f"{self.url()}/api/user/{userId}/user",json=data,headers=self.get_headers())
        return  r.json()

    def batchDeleteRole(self,userId,roleIds):
        """删除用户下的一批角色"""
        data = roleIds
        r = requests.post(f"{self.url()}/api/user/{userId}/role",json=data,headers=self.get_headers())
        return r.json()

    def deleteAllRole(self,userId):
        """删除用户下的所有角色"""

        r = requests.delete(f"{self.url()}/api/user/{userId}/role",headers=self.get_headers())
        return r.json()

    def insertRole(self,userId,roleId):
        """添加一个用户角色"""
        r = requests.put(f"{self.url()}/api/user/{userId}/role/{roleId}",headers=self.get_headers())
        return r.json()

    def deleteRole(self,userId,roleId):
        """删除用户下的某个角色"""
        r = requests.delete(f"{self.url()}/api/user/{userId}/user/{roleId}",headers=self.get_headers())
        return r.json()

