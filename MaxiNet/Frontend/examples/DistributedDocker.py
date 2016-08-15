#!/usr/bin/python2

#
# Minimal example showing how to use MaxiNet
#

import time

from MaxiNet.Frontend.containernetWrapper import ContainernetTopo, ContainerExperiment
from MaxiNet.Frontend import maxinet
from MaxiNet.tools import FatTree
from mininet.log import setLogLevel, info
from mininet.net import Containernet
from mininet.node import OVSSwitch, Node

setLogLevel('info')

topo = ContainernetTopo(controller=OVSSwitch)

info('*** Adding controller\n')


info('*** Adding hosts\n')
h1 = topo.addHost('h1')
h2 = topo.addHost('h2')

info('*** Adding docker containers\n')
d1 = topo.addDocker('d1', ip='10.0.0.251', dimage="ubuntu:trusty")
d2 = topo.addDocker('d2', ip='10.0.0.252', dimage="ubuntu:trusty", cpu_period=50000, cpu_quota=25000)
#d3 = topo.addHost('d3', ip='11.0.0.253', cls=Docker, dimage="ubuntu:trusty", cpu_shares=20)
#d5 = topo.addDocker('d5', dimage="ubuntu:trusty", volumes=["/:/mnt/vol1:rw"])

info('*** Adding switch\n')
s1 = topo.addSwitch('s1')
s2 = topo.addSwitch('s2')
#s3 = net.addSwitch('s3')

info('*** Creating links\n')
topo.addLink(d1, s1)
topo.addLink(s2, d2)
topo.addLink(h2, s2)
topo.addLink(h1, s2)
topo.addLink(s1, s2)
#net.addLink(s1, s2, cls=TCLink, delay="100ms", bw=1, loss=10)
# try to add a second interface to a docker container
#net.addLink(d2, s3, params1={"ip": "11.0.0.254/8"})
#net.addLink(d3, s3)


cluster = maxinet.Cluster()

exp = ContainerExperiment(cluster, topo)
exp.setup()

print exp.get_node("h1").cmd("ifconfig")  # call mininet cmd function of h1
print exp.get_node("h2").cmd("ifconfig")

print exp.get_node("d1").cmd("ifconfig")
print exp.get_node("d2").cmd("ifconfig")

print "waiting 5 seconds for routing algorithms on the controller to converge"
time.sleep(5)

print exp.get_node("d1").cmd("ping -c 5 10.0.0.252")

print "waiting 5 seconds again"
time.sleep(5)


exp.CLI(locals(), globals())

exp.stop()
