import requests

from common.Api import Api


class HostMinotorPage(Api):
    """ 主机监控管理 接口"""
    def addHostMonitor(self,content,hostTime,hostname,type):
        """ 添加主机监控日志"""
        data = {
            "content": content,
            "hostTime": hostTime,
            "hostname": hostname,
            "type": type
        }
        r = requests.put(f"{self.url()}/api/monitors/",json=data)
        return r.json()

    def queryHostMonitorPage(self,pageNum,pageSize):
        """ 根据条件获取主机监控信息列表"""
        data = {

        }
        r = requests.post(f"{self.url()}/api/monitors/page/{pageNum}/{pageSize}", json=data)
        return r.json()

    def querySystemInfoPage(self,pageNum,pageSize):
        """ 根据条件获取主机系统信息列表"""
        data = {

        }
        r = requests.post(f"{self.url()}/api/monitors/systeminfo/page/{pageNum}/{pageSize}", json=data)
        return r.json()

    def getHostMonitorById(self,id):
        """ 根据ID获取主机监控信息 """
        r = requests.get(f"{self.url()}/api/monitors/{id}")
        return r.json()

    def deleteHostMonitor(self,id):
        """ 删除主机监控信息 """
        r = requests.get(f"{self.url()}/api/monitors/{id}")
        return r.json()