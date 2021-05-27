import requests

from common.Api import Api


class solutionPage(Api):
    """ solution管理接口 """
    def getSolutions(self):
        """
        根据获取所有solution
        :return:
        """
        r = requests.get(f"{self.url()}/api/solutions/")
        return r.json()

    def querySolutions(self,name):
        """ 根据条件获取solution列表 """
        data = {
            "name":name,
        }
        r = requests.post(f"{self.url()}/api/solutions/",json=data)
        return r.json()

    def addSolution(self,name,version):
        """
        添加solution
        :return:
        """
        data = {
            "name":name,
            "version":version,
        }
        r = requests.put(f"{self.url()}/api/solutions/",json=data)
        return r.json()

    def querySolutionsCount(self,name,version):
        """
        根据条件获取solution总数
        :return:
        """
        data = {
            "name":name,
            "version": version
        }
        r = requests.post(f"{self.url()}/api/solutions/count",json=data)
        return r.json()

    def querySolutionsPage(self,pageNum,pageSize,name,version):
        """
        根据条件获取solution列表
        :return:
        """
        data = {
            "name": name,
            "version": version
        }
        r = requests.post(f"{self.url()}/api/solutions/page/{pageNum}/{pageSize}", json=data)
        return r.json()

    def getSolutionById(self,id):
        """
        根据ID获取solution
        :return:
        """
        r = requests.get(f"{self.url()}/api/solutions/{id}")
        return r.json()

    def updateSolution(self,id,name,version):
        """
        更新solution
        :return:
        """
        data = {
            "name": name,
            "version": version
        }
        r = requests.get(f"{self.url()}/api/solutions/{id}", json=data)
        return r.json()

    def deleteSolution(self,id):
        """
        根据id删除solution
        :return:
        """
        r = requests.delete(f"{self.url()}/api/solutions/{id}")
        return r.json()

    def getSolutionDetailById(self,solutionId):
        """
        根据ID获取solution详情
        :return:
        """
        r = requests.get(f"{self.url()}/api/solutions/{solutionId}/detail")
        return r.json()

