import unittest
import time

from MaxiNet.Frontend.containernetWrapper import ContainernetTopo, ContainerExperiment, ContainernetCluster
from mininet.node import OVSSwitch


# This file contains unittests which should test the added functions of Containernet and the modified partitioner class
# Warning: this will kill all ubuntu docker containers !!!

class MyTestCase(unittest.TestCase):
    def test_2D_2S(self):
        """
        Test following static topo with different numbers of workers    d1---s1---s2---d1
        :return:
        """
        enough_available_Workers(self)

        iterate_number_of_worker(self, Topo_2D_2S)

        # Default case
        Topo_2D_2S(self, None, None)

    def test_docker_exclusive_methods(self):
        """
        Test following static topo with different numbers of workers    d1---s1---s2---d1
        Test add/remove docker dynamically
        :return:
        """
        enough_available_Workers(self)

        iterate_number_of_worker(self, Test_Exclusive_DockerFeatures)


if __name__ == '__main__':
    unittest.main()


def enough_available_Workers(testCase):
    """make sure that we have at least 2 worker"""
    workers = len(ContainernetCluster(maxWorkers=0).get_available_workers())
    testCase.assertGreaterEqual(workers, 2,
                                msg='For this test you need at least 2 running workers. You have %s worker free.' % workers)


def iterate_number_of_worker(testCase, testToRun):
    # Each test should work on 1 or more workers
    testToRun(testCase, 1, 1)  # exactly one worker

    testToRun(testCase, 2, 2)  # two worker

    testToRun(testCase, None, None)  # all available worker


def Topo_2D_2S(testCase, minNumOfWorkers, maxNumOfWorkers):
    """
    - Creates Topo with 2 Dockercontainers and 2 Switches    d1---s1---s2---d1
    - Test if the connection between d1 an d2 works
    - Test if link update works
    """
    topo = ContainernetTopo(controller=OVSSwitch)
    waitTime = 7

    d1 = topo.addDocker('d1', ip='10.0.0.251', dimage="ubuntu:trusty")
    d2 = topo.addDocker('d2', ip='10.0.0.252', dimage="ubuntu:trusty")

    s1 = topo.addSwitch('s1')
    s2 = topo.addSwitch('s2')

    topo.addLink(d1, s1)
    topo.addLink(s2, d2)
    topo.addLink(s1, s2)

    cluster = ContainernetCluster(minWorkers=minNumOfWorkers, maxWorkers=maxNumOfWorkers)

    exp = ContainerExperiment(cluster, topo, switch=OVSSwitch)
    exp.setup(startWorkerConcurrent=True)

    # waiting 5 seconds for routing algorithms on the controller to converge
    time.sleep(waitTime)

    out = exp.get_node('d1').cmd("ping -c 5 10.0.0.252")
    testCase.assertRegexpMatches(out, '.* 0% packet loss.*')

    out = exp.get_node('d2').cmd("ping -c 5 10.0.0.251")
    testCase.assertRegexpMatches(out, '.* 0% packet loss.*')

    # update link status  d1-x-s1---s2---d2
    exp.configLinkStatus("d1", "s1", "down")
    time.sleep(waitTime)

    out = exp.get_node('d1').cmd("ping -c 5 10.0.0.252")
    testCase.assertRegexpMatches(out, '.* 100% packet loss.*')

    out = exp.get_node('d2').cmd("ping -c 5 10.0.0.251")
    testCase.assertRegexpMatches(out, '.* 100% packet loss.*')

    # update link status  d1---s1-x-s2---d2
    exp.configLinkStatus("d1", "s1", "up")
    exp.configLinkStatus("s1", "s2", "down")
    time.sleep(waitTime)

    out = exp.get_node('d1').cmd("ping -c 5 10.0.0.252")
    testCase.assertRegexpMatches(out, '.* 100% packet loss.*')

    out = exp.get_node('d2').cmd("ping -c 5 10.0.0.251")
    testCase.assertRegexpMatches(out, '.* 100% packet loss.*')

    # update link status  d1---s1---s2---d2
    exp.configLinkStatus("s1", "s2", "up")
    time.sleep(waitTime)

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

    time.sleep(waitTime * 2)


def Test_Exclusive_DockerFeatures(testCase, minNumOfWorkers, maxNumOfWorkers):
    """                                                               h1 d3
                                                                       \/
        - Creates Topo with 2 Dockercontainers and 2 Switches    d1---s1---s2---d1
        - Test all methods and attributes of the Docker class
        - Add and remove a container at runtime
        - Test concurrent startup when using multiple worker
        - Test if automatic pull works (checking methods _check_image_[exists, pull])
        """
    topo = ContainernetTopo(controller=OVSSwitch)
    waitTime = 7

    d1 = topo.addDocker('d1', ip='10.0.0.251', dimage="ubuntu:trusty")
    d2 = topo.addDocker('d2', ip='10.0.0.252', dimage="ubuntu:trusty")

    h1 = topo.addHost('h1')

    s1 = topo.addSwitch('s1')
    s2 = topo.addSwitch('s2')

    topo.addLink(d1, s1)
    topo.addLink(s2, d2)
    topo.addLink(s1, s2)
    topo.addLink(s1, h1)

    cluster = ContainernetCluster(minWorkers=minNumOfWorkers, maxWorkers=maxNumOfWorkers)

    # automatic pull will pull missing images, so we remove them before
    for worker in cluster.workers():
        print worker.run_cmd("docker pull ubuntu:precise")

    exp = ContainerExperiment(cluster, topo, switch=OVSSwitch)
    exp.setup()

    # waiting 5 seconds for routing algorithms on the controller to converge
    time.sleep(waitTime)

    # ping between Mininet Host and Docker Host
    out = exp.get_node('h1').cmd("ping -c 5 10.0.0.251")
    testCase.assertRegexpMatches(out, '.* 0% packet loss.*')
    out = exp.get_node('d2').cmd("ping -c 5 %s" % exp.get_node('h1').IP())
    testCase.assertRegexpMatches(out, '.* 0% packet loss.*')

    nodewrapperd2 = exp.get_node('d2')

    # Test docker methods over nodewrapper
    nodewrapperd2.updateCpuLimit(cpu_shares=512, cpu_period=50001, cpu_quota=20001, cores='0')
    time.sleep(waitTime)

    testCase.assertEqual(nodewrapperd2.dimage, "ubuntu:trusty")
    testCase.assertEqual(nodewrapperd2.cpu_shares, 512)
    testCase.assertEqual(nodewrapperd2.cpu_period, 50001)
    testCase.assertEqual(nodewrapperd2.cpu_quota, 20001)
    testCase.assertEqual(nodewrapperd2.cpuset, None)
    testCase.assertEqual(nodewrapperd2.cgroupGet('cpus', resource='cpuset'), 0)

    nodewrapperd2.updateMemoryLimit(mem_limit=66093056)
    testCase.assertEqual(nodewrapperd2.mem_limit, 66093056)

    nodewrapperd2.updateMemoryLimit(memswap_limit=-1)
    testCase.assertEqual(nodewrapperd2.memswap_limit, -1)

    testCase.assertEqual(nodewrapperd2.volumes, [])

    # test dynamically add of container
    exp.addDocker('d3', ip='10.0.0.253', dimage="ubuntu:trusty", pos='s1')
    exp.addLink('d3', 's1', autoconf=True)

    # ping should be work now
    out = exp.get_node('d1').cmd("ping -c 5 10.0.0.253")
    testCase.assertRegexpMatches(out, '.* 0% packet loss.*')
    out = exp.get_node('d2').cmd("ping -c 5 10.0.0.253")
    testCase.assertRegexpMatches(out, '.* 0% packet loss.*')

    # remove d1
    exp.removeDocker('d1')
    time.sleep(waitTime)

    # d1 should be unreachable
    out = exp.get_node('d2').cmd("ping -c 5 10.0.0.251")
    testCase.assertRegexpMatches(out, '.* 100% packet loss.*')
    out = exp.get_node('d3').cmd("ping -c 5 10.0.0.251")
    testCase.assertRegexpMatches(out, '.* 100% packet loss.*')

    # test docker image methods
    exp.get_worker('d2').run_cmd("docker rmi -f ubuntu:precise")
    out = exp.get_node('d2')._image_exists('ubuntu', 'precise')
    testCase.assertFalse(out)

    # both methods should return false
    out = exp.get_node('d2')._check_image_exists('ubuntu:precise')
    testCase.assertFalse(out)
    out = exp.get_node('d2')._image_exists('ubuntu', 'precise')
    testCase.assertFalse(out)

    # pull a missing image, should return true
    out = exp.get_node('d2')._pull_image('ubuntu', 'precise')
    testCase.assertTrue(out)

    # both methods should return true
    out = exp.get_node('d2')._check_image_exists('ubuntu:precise')
    testCase.assertTrue(out)
    out = exp.get_node('d2')._image_exists('ubuntu', 'precise')
    testCase.assertTrue(out)

    exp.stop()
    cluster.remove_workers()

    time.sleep(waitTime * 2)
