#!/usr/bin/python2

#
# Minimal example showing how to use MaxiNet
#

import time

from MaxiNet.Frontend.containernetWrapper import ContainernetTopo, ContainerExperiment, ContainernetCluster
from MaxiNet.tools import Tools
from mininet.log import setLogLevel, info
from mininet.node import OVSSwitch


setLogLevel('info')

topo = ContainernetTopo(controller=OVSSwitch)


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


cluster = ContainernetCluster()

exp = ContainerExperiment(cluster, topo, switch=OVSSwitch)
# start hosts parallel
exp.setup(startWorkerConcurrent=True)

# versch tests




print exp.get_node("h1").cmd("ifconfig")  # call mininet cmd function of h1
print exp.get_node("h2").cmd("ifconfig")

print exp.get_node("d1").cmd("ifconfig")
print exp.get_node("d2").cmd("ifconfig")

print "waiting 5 seconds for routing algorithms on the controller to converge"
#time.sleep(5)

print "ping d1 ---> d2"
print exp.get_node("d1").cmd("ping -c 5 10.0.0.252")
print "ping d2 ---> d1"
print exp.get_node("d2").cmd("ping -c 5 10.0.0.251")

#exp.CLI(locals(), globals())

print "add d3 at runtime"
#worker = exp.get_worker('s1')
#worker.addDocker('d4', dimage="ubuntu:trusty")
d3 = exp.addDocker("d3", pos="s1", dimage="ubuntu:trusty", ip="10.0.0.254", max=Tools.makeMAC(3))
#d3.setIP(ip='10.0.0.254')
#h3 = exp.get_worker("s1").addHost('h3', ip=Tools.makeIP(3), max=Tools.makeMAC(3))
#d3 = exp.get_worker("s1").addDocker('d3', dimage="ubuntu:trusty")

print "add link s1 <---> d3"
#exp.addLink(exp.get_node("d3"), exp.get_node("s1"), params1={"ip": "10.0.0.254/8"})
exp.addLink("d3", "s1", autoconf=True)


print "wait 5 seconds"
time.sleep(5)

print "ping d3 --> d1"
print d3.cmd("ping -c 5 10.0.0.251")
print "ping d1 --> d3"
print exp.get_node("d1").cmd("ping -c 5 10.0.0.254")

# remove a container
exp.removeDocker('d1')
print d3.cmd("ping -c 5 10.0.0.251")

print "ping d3 --> d2"
print d3.cmd("ping -c 5 10.0.0.252")
print "ping d2 --> d3"
print exp.get_node("d2").cmd("ping -c 5 10.0.0.254")


exp.CLI(locals(), globals())

exp.stop()
