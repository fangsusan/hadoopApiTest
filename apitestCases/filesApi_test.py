import allure
import pytest

from pageApi.filesPage import filePage

@allure.feature("文件管理接口模块")
class TestFiles:
    """ 文件管理接口 """
    def setup(self):
        self.filePage = filePage()
        self.file = {'file': open('C:\\Users\\admin\\Desktop\\test.txt', 'rb')}
        self.name = "Wit_1.3_CentOS001.zip"
        self.type = "txt"

    def teardown(self):
        pass
        # self.filePage.deleteFile(id=id)

    @allure.story("获取所有文件接口 Api")
    def test_getFiles(self):
        """ 获取所有文件接口 正例 """
        result = self.filePage.getFiles()
        print(result)
        assert result['status'] == 200

    @allure.story("根据条件获取文件 Api")
    def test_queryFiles(self):
        """根据条件获取文件   正例"""
        result = self.filePage.queryFiles(name=self.name)
        print(result)
        assert result["status"] == 200
        assert result['data'][0]['name'] == self.name

    @allure.story("根据条件name获取文件总数 Api")
    def test_queryFilesCount(self):
        """根据条件name获取文件总数  正例"""
        result = self.filePage.queryFilesCount(name=self.name)
        print(result)
        assert result["status"] == 200
        assert result['data'] !=0

    @allure.story("根据ID获取文件内容 Api")
    @pytest.mark.parametrize("id",[("45573444435202048")])
    def test_getFileDataById(self,id):
        """ 根据ID获取文件内容 正例 """
        result = self.filePage.getFileDataById(id=id)
        assert result["status"] == 200

    @allure.story("上传文件zip Api")
    def test_uploadFile(self):
        """ 上传文件zip   正例 """
        try:
            result = self.filePage.uploadFile(files=self.file,name=self.name,type=self.type)
            print(result)
            id = result['data']['id']
        finally:
            self.filePage.deleteFile(id=id)
        assert result['status'] == 200
        assert result['data']['name'] == self.name

    @allure.story("上传文件内容 Api")
    @pytest.mark.parametrize("content",[("string11110")])
    def test_uploadFileContent(self,content):
        """上传文件内容 """
        result = self.filePage.uploadFileContent(content=content)
        print(result)
        assert result['status'] == 200

    @allure.story("根据条件获取文件列表 Api")
    @pytest.mark.parametrize("pageNum,pageSize",[(1,1)])
    def test_queryFilesPage(self,pageNum, pageSize):
        """根据条件获取文件列表  正例"""
        result = self.filePage.queryFilesPage(pageSize=pageSize,pageNum=pageNum)
        print(result)
        assert result['status'] == 200

    @allure.story("根据ID获取文件信息 Api")
    def test_getFileById(self):
        """根据ID获取文件信息 正例 """
        try:
            pre = self.filePage.uploadFile(files=self.file,name=self.name,type=self.type)
            id = pre['data']['id']
            result = self.filePage.getFileById(id=id)
        finally:
            self.filePage.deleteFile(id=id)

        assert result['status'] == 200


    @allure.story("根据id删除文件 Api")
    def test_deleteFile(self):
        """根据id删除文件 正例"""
        try:
            pre = self.filePage.uploadFile(files=self.file,name=self.name,type=self.type)
            id = pre['data']['id']
        finally:
            result = self.filePage.deleteFile(id=id)
        assert result['status'] == 200

    @allure.story("根据id下载文件 Api")
    def test_downloadFile(self):
        """根据id下载文件 正例 """
        try:
            pre = self.filePage.uploadFile(files=self.file, name=self.name, type=self.type)
            id = pre['data']['id']
            result = self.filePage.downloadFile(id=id)
        finally:
            self.filePage.deleteFile(id=id)
        print(result)  # 返回的是文件内容，so校验的name是文件内容的name而不是文件名
        assert result['name'] == "Wit"






