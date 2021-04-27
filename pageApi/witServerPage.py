import requests

from Api import Api


class witServerPage(Api):
    """WitServer管理接口"""
    def findPage(self,pageNum,pageSize ):
        """获取WitServer服务器列表 """
        r = requests.get(f"{self.url()}/api/server/page/{pageNum}/{pageSize }")
        return r.json()