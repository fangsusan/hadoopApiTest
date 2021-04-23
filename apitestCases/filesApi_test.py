import pytest

from pageApi.filesPage import filePage


class TestFiles:

    def setup(self):
        self.filePage = filePage()
        self.name = "Wit_1.3_CentOS133.zip"


    def test_getFiles(self):
        """ 获取所有文件接口 正例 """
        result = self.filePage.getFiles()
        print(result)
        assert result['status'] == 200

    def test_queryFiles(self):
        """根据条件获取文件   正例"""
        result = self.filePage.queryFiles(name= self.name)
        print(result)
        assert result["status"] == 200
        assert result['data'][0]['name'] ==  self.name

    def test_queryFilesCount(self):
        """根据条件name获取文件总数  正例"""

        result = self.filePage.queryFilesCount(name= self.name)
        print(result)
        assert result["status"] == 200

    def test_uploadFile(self):
        """ 上传文件zip   正例 """
        file = "C:\Users\admin\Desktop\Wit_1.3_CentOS133"
        name = "fang001"
        type = "zip"
        result = self.filePage.uploadFile(file=file,name=name,type=type)
        assert result['status'] == 200

    @pytest.mark.parametrize("pageNum,pageSize",[(1,1)])
    def test_queryFilesPage(self,pageNum, pageSize):
        """根据条件获取文件列表  正例"""
        result = self.filePage.queryFilesPage(pageSize=pageSize,pageNum=pageNum)
        print(result)
        assert result['status'] == 200

    @pytest.mark.parametrize("id",[("39649245812240384")])
    def test_getFileById(self,id):
        result = self.filePage.getFileById(id=id)
        assert result['status'] == 200
        assert result['data']['id'] == id


    def test_deleteFile(self,id):

        result = self.filePage.deleteFile(id=id)
        assert result['status'] == 200
        assert result['data']['id'] == id





