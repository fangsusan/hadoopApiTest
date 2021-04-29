import pytest
import requests

from pageApi.hostsPage import HostsPage

class TestHosts:

    def setup(self):
        self.HostsPage = HostsPage()

    def teardown(self):
        pass

    def test_gethosts(self):
        """获取所有主机 正例"""

        r = self.HostsPage.gethosts()
        assert r["status"] == 200

    @pytest.mark.parametrize("hostname,clusterId,osId,osVer,rackId,siteId",
                             [("meilanzi004","10000","100001","1.2","101","100"),
                              ("meilanzi005","1000","10001","1.2","1001","1100")])
    def test_addHost(self,hostname,clusterId,osId,osVer,rackId,siteId):
        """ 添加主机 正例"""
        r = self.HostsPage.addHost(hostname=hostname,clusterId=clusterId,osVer=osVer,
                                   osId=osId,rackId=rackId,siteId=siteId)
        id = r['data']['id']
        try:
            self.HostsPage.getHostByHostname(hostname)
        finally:
            self.HostsPage.deleteHost(id=id)
        assert r["data"]["hostname"] == hostname
        assert r["status"] == 200

    def test_getHostcount(self):
        """ 根据条件获取主机总数  正例"""
        name = "fang"
        result = self.HostsPage.getHostCount(name=name)
        print(result)
        assert result['status'] == 200

    def test_getHostByHostname(self):
        """根据主机名称获取主机信息 正例"""
        hostname = "meilanzi001"
        r = self.HostsPage.getHostByHostname(hostname)
        print(r)
        assert r["status"] == 200
        assert r["data"]["hostname"] == hostname

    def test_getHostById(self):
        """根据Id获取主机信息 正例"""
        id = "40072218616541184"
        r = self.HostsPage.getHostById(id=id)
        print(r)
        assert r["status"] == 200


    @pytest.mark.parametrize("hostname,clusterId,osId,osVer,rackId,siteId",
                             [("meilanzi900","10000","100001","1.2","101","100")])
    def test_updataHost(self,hostname,clusterId,osId,osVer,rackId,siteId):
        """ 更新主机  正例"""
        id = 40072904993419264
        result = self.HostsPage.updateHost(id=id,hostname=hostname, clusterId=clusterId, osVer=osVer,
                               osId=osId, rackId=rackId, siteId=siteId)
        return result["status"] == 200


    @pytest.mark.parametrize("hostname,clusterId,osId,osVer,rackId,siteId",
                             [("meilanzi004","10000","100001","1.2","101","100"),
                              ("meilanzi005","1000","10001","1.2","1001","1100")])
    def test_deleteHost(self,hostname,clusterId,osId,osVer,rackId,siteId):
        """根据ID删除主机  正例"""
        try:
            self.HostsPage.getHostByHostname(name=hostname)
        finally:
            r = self.HostsPage.addHost(hostname=hostname, clusterId=clusterId, osVer=osVer,
                               osId=osId, rackId=rackId, siteId=siteId)
            id = r["data"]["id"]

        result = self.HostsPage.deleteHost(id=id)
        print(result)
        assert result["status"] == 200





