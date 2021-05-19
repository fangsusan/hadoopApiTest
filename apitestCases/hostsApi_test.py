import allure
import pytest
from pageApi.hostsPage import HostsPage

@allure.feature("主机管理接口")
class TestHosts:
    """ 主机管理接口 """
    def setup(self):
        self.HostsPage = HostsPage()

    def teardown(self):
        pass

    @allure.story("获取所有主机 Api")
    def test_gethosts(self):
        """获取所有主机 正例"""
        result = self.HostsPage.gethosts()
        assert result["status"] == 200


    @allure.story("添加主机 Api")
    @pytest.mark.parametrize("hostname,clusterId,osId,osVer,rackId,siteId",
                             [("meilanzi004","10000","100001","1.2","101","100"),
                              ("meilanzi005","1000","10001","1.2","1001","1100")])
    def test_addHost(self,hostname,clusterId,osId,osVer,rackId,siteId):
        """ 添加主机 正例"""
        result = self.HostsPage.addHost(hostname=hostname,clusterId=clusterId,osVer=osVer,
                                   osId=osId,rackId=rackId,siteId=siteId)
        id = result['data']['id']
        try:
            self.HostsPage.getHostByHostname(hostname)
        finally:
            self.HostsPage.deleteHost(id=id)
        assert result["data"]["hostname"] == hostname
        assert result["status"] == 200

    @allure.story("批量添加集群主机 Api")
    def test_addClusterHosts(self):
        """批量添加集群主机"""
        clusterId = 46249190782685184
        hostsIds = [45518527477600256,45518527477600256,45831284282380288]
        try:
            result = self.HostsPage.addClusterHosts(clusterId=clusterId,hostsIds=hostsIds)
            print(result)
        finally:
            self.HostsPage.deleteClusterHosts(clusterId=clusterId, hostsIds=hostsIds)
        assert result["status"] == 200

    @allure.story("批量删除集群主机 Api")
    def test_deleteClusterHosts(self):
        """ 批量删除集群主机 """
        clusterId = 46249190782685184
        hostsIds = [45518527477600256, 45518527477600256, 45831284282380288]
        try:
            self.HostsPage.addClusterHosts(clusterId=clusterId, hostsIds=hostsIds)
        finally:
            result = self.HostsPage.deleteClusterHosts(clusterId=clusterId, hostsIds=hostsIds)
        print(result)
        assert result["status"] == 200

    @allure.story("根据条件获取主机总数 Api")
    def test_getHostcount(self):
        """ 根据条件获取主机总数  正例"""
        name = "fang"
        result = self.HostsPage.getHostCount(name=name)
        print(result)
        assert result['status'] == 200

    @allure.story("根据主机名称获取主机信息 Api")
    @pytest.mark.parametrize("hostname",[("s3.r1.n235")])
    def test_getHostByHostname(self,hostname):
        """根据主机名称获取主机信息 正例"""
        r = self.HostsPage.getHostByHostname(hostname=hostname)
        print(r)
        assert r["status"] == 200
        assert r["data"]["hostname"] == hostname

    @allure.story("根据条件获取主机列表(模糊) Api")
    @pytest.mark.parametrize("hostname,pageSize,pageNum",[("s3.r1.n235",1,10)])
    def test_queryhostPage(self,hostname,pageSize,pageNum):
        """根据条件获取主机列表(模糊)"""
        result = self.HostsPage.queryhostPage(hostname=hostname,pageSize=pageSize,pageNum=pageNum)
        assert result['status'] == 200

    @allure.story("获取集群ID为空的主机 Api")
    @pytest.mark.parametrize("hostname,pageSize,pageNum",[("s3.r1.n235",1,10)])
    def test_getHostPageClusterIsNUll(self,hostname,pageSize,pageNum):
        """获取集群ID为空的主机"""
        result = self.HostsPage.getHostPageClusterIsNUll(hostname=hostname,pageSize=pageSize,pageNum=pageNum)
        assert result['status'] == 200


    @allure.story("根据条件获取主机列表(模糊查询) Api")
    @pytest.mark.parametrize("hostname",[("s3.r1.n235")])
    def test_queryHosts(self,hostname):
        """根据条件获取主机列表(模糊查询)"""
        result = self.HostsPage.queryHosts(hostname=hostname)
        print(result)
        assert result['status'] == 200
        assert result["data"][0]["hostname"] == hostname


    @allure.story("根据Id获取主机信息 Api")
    @pytest.mark.parametrize("id",[("40072218616541184")])
    def test_getHostById(self,id):
        """根据Id获取主机信息 正例"""
        r = self.HostsPage.getHostById(id=id)
        print(r)
        assert r["status"] == 200

    @allure.story("更新主机 Api")
    @pytest.mark.parametrize("id,hostname,clusterId,osId,osVer,rackId,siteId",
                             [("40072904993419264","meilanzi900","10000","100001","1.2","101","100")])
    def test_updataHost(self,id,hostname,clusterId,osId,osVer,rackId,siteId):
        """ 更新主机  正例"""
        result = self.HostsPage.updateHost(id=id,hostname=hostname, clusterId=clusterId, osVer=osVer,
                               osId=osId, rackId=rackId, siteId=siteId)
        return result["status"] == 200

    @allure.story("根据ID删除主机 Api")
    @pytest.mark.parametrize("hostname,clusterId,osId,osVer,rackId,siteId",
                             [("meilanzi004","10000","100001","1.2","101","100"),
                              ("meilanzi005","1000","10001","1.2","1001","1100")])
    def test_deleteHost(self,hostname,clusterId,osId,osVer,rackId,siteId):
        """根据ID删除主机  正例"""
        try:
            self.HostsPage.getHostByHostname(hostname=hostname)
        finally:
            r = self.HostsPage.addHost(hostname=hostname, clusterId=clusterId, osVer=osVer,
                               osId=osId, rackId=rackId, siteId=siteId)
            id = r["data"]["id"]

        result = self.HostsPage.deleteHost(id=id)
        print(result)
        assert result["status"] == 200





