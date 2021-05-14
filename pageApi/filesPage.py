import requests
from Api import Api


class filePage(Api):
    """文件管理接口"""
    def getFiles(self):
        """获取所有文件接口"""
        r = requests.get(f"{self.url()}/api/files/")
        return r.json()

    def queryFiles(self,name,**kwargs):
        """根据条件获取文件"""
        data = {
            "name":name
        }
        data.update(kwargs)
        r = requests.post(f"{self.url()}/api/files/",json=data)
        return r.json()

    def queryFilesCount(self,name,**kwargs):
        """根据条件获取文件总数"""
        data = {
            "name": name
        }
        data.update(kwargs)
        r = requests.post(f"{self.url()}/api/files/count/", json=data)
        return r.json()

    def getFileDataById(self,id):
        """ 根据ID获取文件内容"""
        r = requests.get(f"{self.url()}/api/files/data/{id}")
        return r.json()

    def uploadFile(self,file,name,type):
        """ 上传文件"""
        data = {
            "file": file,
            "name":name,
            "type":type
        }
        r = requests.post(f"{self.url()}/api/files/files/", json=data)
        return r.json()

    def uploadFileContent(self,file,name,type):
        """上传文件内容 """
        data = {
            "file": file,
            "name": name,
            "type": type
        }
        r = requests.post(f"{self.url()}/api/files/files/content",json=data)
        return r.json()

    def queryFilesPage(self,pageNum,pageSize,**kwargs ):
        """根据条件获取文件列表"""
        data = {
        }
        data.update(**kwargs)
        r = requests.post(f"{self.url()}/api/files/page/{pageNum}/{pageSize}", json=data)
        return r.json()

    def getFileById(self,id):
        """根据ID获取文件信息"""
        r = requests.get(f"{self.url()}/api/files/{id}")
        return r.json()

    def deleteFile(self,id):
        """根据id删除文件"""
        r = requests.delete(f"{self.url()}/api/files/{id}")
        return r.json()

    def downloadFile(self,id):
        """根据id下载文件"""
        r = requests.get(f"{self.url()}/api/files/{id}/data")
        return r.json()