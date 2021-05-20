import requests

from common.Api import Api


class permissionPage(Api):
    """ WitServer 系统资源管理接口"""
    def  insertPermission(self,resourceId,tag,**kwargs):
        """ 添加权限信息 """
        data = {
            "resourceId": resourceId,
            "tag": tag,
        }
        data.update(kwargs)
        r = requests.put(f"{self.url()}/api/permission/",json=data)
        return r.json()

    def countAll(self):
        """获取权限总数 """
        r = requests.get(f"{self.url()}/api/permission/count")
        return r.json()

    def countByTag(self,tag):
        """ 根据权限名称获取权限总数"""
        r = requests.get(f"{self.url()}/api/permission/count/tag/{tag}")
        return r.json()

    def findPage(self,pageNum,pageSize):
        """ 获取权限列表 """
        r = requests.get(f"{self.url()}/api/permission/page/{pageNum}/{pageSize}")
        return r.json()

    def findByTag(self,tag,pageNum,pageSize):
        """ 根据权限名称获取权限列表 """
        r = requests.get(f"{self.url()}/api/permission/tag/{tag}/{pageNum}/{pageSize}")
        return r.json()

    def getPermission(self,id):
        """ 获取权限信息 """
        r = requests.get(f"{self.url()}/api/permission/{id}")
        return r.json()

    def updatePermission(self,id,tag):
        """更新权限信息"""
        data = {
            "tag":tag
        }
        r = requests.post(f"{self.url()}/api/permission/{id}",json=data)
        return r.json()

    def deletePermission(self,id):
        """ 删除权限信息 """
        r = requests.delete(f"{self.url()}/api/permission/{id}")
        return r.json()