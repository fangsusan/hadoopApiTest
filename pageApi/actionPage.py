from Api import Api
import requests

class ActionPage(Api):
    """ 行为管理接口 """
    def getActions(self):
        """获取所有行为信息"""
        r = requests.get(f'{self.url()}/api/actions/')
        return r.json()

    def abortAction(self,actionId):
        """终止操作"""
        data = {
            "actionId":actionId,
        }
        r = requests.post(f'{self.url()}/api/actions/',json=data)
        return r.json()

    def queryActionPage(self,pageNum,pageSize,**kwargs):
        """根据条件获取信息列表 """
        data ={

        }
        data.update(kwargs)
        r = requests.post(f'{self.url()}/api/actions/page/{pageNum}/{pageSize}', json=data)
        return r.json()

    def queryActions(self,name,**kwargs):
        """根据条件获取信息列表 """
        data = {
                "name":name
        }
        data.update(kwargs)
        r = requests.post(f'{self.url()}/api/actions/querise', json=data)
        return r.json()

    def queryStagesPage(self,pageNum,pageSize):
        """根据条件获取信息列表"""
        data = {

        }
        r = requests.post(f'{self.url()}/api/actions/stages/page/{pageNum}/{pageSize}',json=data)
        return r.json()

    def queryStages(self):
        """获取所有行为的阶段信息 """
        data = {

        }
        r = requests.post(f'{self.url()}/api/actions/stages/querise', json=data)
        return r.json()


    def getStageById(self,stageId):
        """获取行为信息"""
        r = requests.get(f'{self.url()}/api/actions/stages/{stageId}')
        return r.json()


    def queryTasksPage(self,pageNum,pageSize,**kwargs):
        """根据条件获取信息列表"""
        data = {

        }
        data.update(kwargs)
        r = requests.post(f'{self.url()}/api/actions/tasks/page/{pageNum}/{pageSize}',json=data)
        return r.json()

    def queryTasks(self):
        """获取所有行为的阶段信息"""
        data = {

        }
        r = requests.post(f'{self.url()}/api/actions/tasks/querise', json=data)
        return r.json()

    def getTaskById(self,taskId):
        """获取行为信息"""
        r = requests.get(f'{self.url()}/api/actions/tasks/{taskId}')
        return r.json()

    def updateTask(self,taskId,name,status):
        """更新行为信息"""
        data = {
            "name":name,
            "status":status,
        }
        r = requests.post(f'{self.url()}/api/actions/tasks/{taskId}',json=data)
        return r.json()

    def testActionTaskResponse(self,):
        """测试Task返回结果"""
        taskConsumerDTO = {
                          "id": 0,
                          "result": {
                            "info": "string",
                            "message": "string",
                            "status": 0
                          },
                          "type": "string"
                        }
        r = requests.post(f"{self.url()}/api/actions/test",json=taskConsumerDTO)
        return r.json()

    def getActionById(self, taskId):
        """获取行为信息"""
        r = requests.get(f'{self.url()}/api/actions/tasks/{taskId}')
        return r.json()


