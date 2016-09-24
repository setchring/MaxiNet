import unittest
import time

from MaxiNet.Frontend.containernetWrapper import ContainernetTopo, ContainerExperiment
from MaxiNet.Frontend.maxinet import Cluster
from MaxiNet.tools import Tools
from mininet.log import setLogLevel, info
from mininet.node import OVSSwitch


class MyTestCase(unittest.TestCase):
    def test_2D_2S(self):
        """
        Test following static topo with different numbers of workers    d1---s1---s2---d1
        :return:
        """
        workers = len(Cluster(maxWorkers=0).get_available_workers())
        self.assertGreaterEqual(workers, 3,
                                msg='For this test you need at least 3 running workers. You have %s worker free.' % workers)

        iterate_number_of_worker(self, Topo_2D_2S)

        # Default case
        Topo_2D_2S(self, None, None)


if __name__ == '__main__':
    unittest.main()


def iterate_number_of_worker(testCase, testToRun): #TODO zusaetzliche Variablen durchleiten
    testToRun(testCase, 1, 1)

    testToRun(testCase, 1, 2)

    testToRun(testCase, 1, 3)

    testToRun(testCase, 2, 2)

    testToRun(testCase, 2, 3)

    testToRun(testCase, 3, 3)


def Topo_2D_2S(testCase, minNumOfWorkers, maxNumOfWorkers):
    """
    - Creates Topo with 2 Dockercontainers and 2 Switches    d1---s1---s2---d1
    - Test if the connection between d1 an d2 works
    - Test if link update works
    """
    topo = ContainernetTopo(controller=OVSSwitch)

    d1 = topo.addDocker('d1', ip='10.0.0.251', dimage="busybox:latest")
    d2 = topo.addDocker('d2', ip='10.0.0.252', dimage="ubuntu:trusty")

    s1 = topo.addSwitch('s1')
    s2 = topo.addSwitch('s2')

    topo.addLink(d1, s1)
    topo.addLink(s2, d2)
    topo.addLink(s1, s2)

    cluster = Cluster(minWorkers=minNumOfWorkers, maxWorkers=maxNumOfWorkers)

    exp = ContainerExperiment(cluster, topo, switch=OVSSwitch)
    exp.setup()

    # waiting 5 seconds for routing algorithms on the controller to converge
    time.sleep(5)

    out = exp.get_node('d1').cmd("ping -c 5 10.0.0.252")
    testCase.assertRegexpMatches(out, '.* 0% packet loss.*')

    out = exp.get_node('d2').cmd("ping -c 5 10.0.0.251")
    testCase.assertRegexpMatches(out, '.* 0% packet loss.*')

    # update link status  d1-x-s1---s2---d2
    exp.configLinkStatus("d1", "s1", "down")
    time.sleep(5)

    out = exp.get_node('d1').cmd("ping -c 5 10.0.0.252")
    testCase.assertRegexpMatches(out, '.* 100% packet loss.*')

    out = exp.get_node('d2').cmd("ping -c 5 10.0.0.251")
    testCase.assertRegexpMatches(out, '.* 100% packet loss.*')

    # update link status  d1---s1-x-s2---d2
    exp.configLinkStatus("d1", "s1", "up")
    exp.configLinkStatus("s1", "s2", "down")
    time.sleep(5)

    out = exp.get_node('d1').cmd("ping -c 5 10.0.0.252")
    testCase.assertRegexpMatches(out, '.* 100% packet loss.*')

    out = exp.get_node('d2').cmd("ping -c 5 10.0.0.251")
    testCase.assertRegexpMatches(out, '.* 100% packet loss.*')

    # update link status  d1---s1---s2---d2
    exp.configLinkStatus("s1", "s2", "up")
    time.sleep(5)

    # ping should be work now again
    out = exp.get_node('d1').cmd("ping -c 5 10.0.0.252")
    testCase.assertRegexpMatches(out, '.* 0% packet loss.*')

    out = exp.get_node('d2').cmd("ping -c 5 10.0.0.251")
    testCase.assertRegexpMatches(out, '.* 0% packet loss.*')

    d1_hostname = exp.get_worker('d1').hn()
    d2_hostname = exp.get_worker('d2').hn()

    # d1 and d2 shouldn't be on the same worker if number of worker is > 1
    if len(exp.workerid_to_hostname) > 1:
        testCase.assertNotEqual(d1_hostname, d2_hostname)
    else:
        testCase.assertEqual(d1_hostname, d2_hostname)

    exp.stop()
    cluster.remove_workers()

    time.sleep(10)

