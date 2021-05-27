import allure
import pytest

from pageApi.HostMonitorPage import HostMinotorPage


@allure.feature("主机监控管理")
class TesthostMonitorPage:
    """ 主机监控管理 接口"""

    def setup(self):
        self.HostMinotorPage = HostMinotorPage()

    @allure.story("添加主机监控日志")
    @pytest.mark.parametrize("content,hostTime,hostname,type",[("fyj",0,"hostfyj","witf")])
    def test_addHostMonitor(self,content,hostTime,hostname,type):
        """ 添加主机监控日志"""
        result = self.HostMinotorPage.addHostMonitor(content, hostTime, hostname, type)
        print(result)
        id = result['data']['id']
        try:
            self.HostMinotorPage.getHostMonitorById(id)
        finally:
            self.HostMinotorPage.deleteHostMonitor(id)
        assert result['status'] == 200
        assert result['data']['hostname'] == hostname

    @allure.story("根据条件获取主机监控信息列表")
    def test_queryHostMonitorPage(self):
        """ 根据条件获取主机监控信息列表"""
        result = self.HostMinotorPage.queryHostMonitorPage(pageNum=1,pageSize=20)
        print(result)
        assert result['status'] == 200

    @allure.story("根据条件获取主机系统信息列表")
    def test_querySystemInfoPage(self):
        """ 根据条件获取主机系统信息列表"""
        result = self.HostMinotorPage.querySystemInfoPage(pageNum=1,pageSize=20)
        print(result)
        assert result['status'] == 200

    @allure.story("根据ID获取主机监控信息")
    def test_getHostMonitorById(self):
        """ 根据ID获取主机监控信息 """
        result = self.HostMinotorPage.getHostMonitorById(id=53145631790747648)
        print(result)
        assert result['status'] == 200
        assert result['data']['hostname'] == 'hostfyj'

    @allure.story("删除主机监控信息")
    @pytest.mark.parametrize("content,hostTime,hostname,type",[("fyj",0,"hostfyj","witf")])
    def test_deleteHostMonitor(self,content,hostTime,hostname,type):
        """ 删除主机监控信息 """

        pre = self.HostMinotorPage.addHostMonitor(content,hostTime,hostname,type)
        print(pre)
        id = pre['data']['id']
        try:
            self.HostMinotorPage.getHostMonitorById(id)
        finally:
            result = self.HostMinotorPage.deleteHostMonitor(id)
        print(result)
        assert result['status'] == 200