import allure
import pytest

from pageApi.filesPage import filePage

@allure.feature("文件管理接口模块")
class TestFiles:
    """ 文件管理接口 """
    def setup(self):
        self.filePage = filePage()
        self.name = "Wit_1.3_CentOS001.zip"

    @allure.story("获取所有文件接口 Api")
    def test_getFiles(self):
        """ 获取所有文件接口 正例 """
        result = self.filePage.getFiles()
        print(result)
        assert result['status'] == 200

    @allure.story("根据条件获取文件 Api")
    def test_queryFiles(self):
        """根据条件获取文件   正例"""
        result = self.filePage.queryFiles(name= self.name)
        print(result)
        assert result["status"] == 200
        assert result['data'][0]['name'] ==  self.name

    @allure.story("根据条件name获取文件总数 Api")
    def test_queryFilesCount(self):
        """根据条件name获取文件总数  正例"""

        result = self.filePage.queryFilesCount(name= self.name)
        print(result)
        assert result["status"] == 200

    @allure.story("根据ID获取文件内容 Api")
    @pytest.mark.parametrize("id",[(47699752619364352)])
    def test_getFileDataById(self,id):
        """ 根据ID获取文件内容 正例 """
        result = self.filePage.getFileDataById(id=id)
        assert result["status"] == 200

    @allure.story("上传文件zip Api")
    def test_uploadFile(self):
        """ 上传文件zip   正例 """
        # file = "C:\Users\admin\Desktop\Wit_1.3_CentOS133"
        name = "fang001"
        type = "zip"
        result = self.filePage.uploadFile(file=file,name=name,type=type)
        assert result['status'] == 200

    @allure.story("上传文件内容 Api")
    def test_uploadFileContent(self):
        """上传文件内容 """
        pass

    @allure.story("根据条件获取文件列表 Api")
    @pytest.mark.parametrize("pageNum,pageSize",[(1,1)])
    def test_queryFilesPage(self,pageNum, pageSize):
        """根据条件获取文件列表  正例"""
        result = self.filePage.queryFilesPage(pageSize=pageSize,pageNum=pageNum)
        print(result)
        assert result['status'] == 200

    @allure.story("根据ID获取文件信息 Api")
    @pytest.mark.parametrize("id",[("45560809509638144")])
    def test_getFileById(self,id):
        """根据ID获取文件信息 正例 """

        result = self.filePage.getFileById(id=id)
        assert result['status'] == 200
        # assert result['data']['id'] == id

    @allure.story("根据id删除文件 Api")
    @pytest.mark.parametrize("id",[("45560809509638144")])
    def test_deleteFile(self,id):
        """根据id删除文件 正例"""

        result = self.filePage.deleteFile(id=id)
        assert result['status'] == 200

    @allure.story("根据id下载文件 Api")
    @pytest.mark.parametrize("id", [("45565744418672640")])
    def test_downloadFile(self,id):
        """根据id下载文件 正例 """
        result = self.filePage.downloadFile(id=id)
        print(result)
        assert result['status'] == 200






