#!/usr/bin/python2

#
# Minimal example showing how to use MaxiNet with hostweights
# In this case the topology cut will balance the host weights between the workers
# It is useful if you have hosts with many workload, which should work on different workers
#

import time

from MaxiNet.Frontend import maxinet
from topo import Topo

topo = Topo()

s1 = topo.addSwitch("s1")
s2=topo.addSwitch("s2")
s3=topo.addSwitch("s3")
s4 =topo.addSwitch("s4")

h1 = topo.addHost("h1", CPUWeight='100', RAMWeight="30")
h2 = topo.addHost("h2", CPUWeight='50', RAMWeight="1")
h3 = topo.addHost("h3", CPUWeight='10', RAMWeight="1")
h4 = topo.addHost("h4", CPUWeight='10', RAMWeight="1")

topo.addLink(s1, h1)
topo.addLink(s2, h2)
topo.addLink(s3, h3)
topo.addLink(s1, s2)
topo.addLink(s2, s3)
topo.addLink(s4, h4)
topo.addLink(s4, s3)


cluster = maxinet.Cluster()

exp = maxinet.Experiment(cluster, topo)
exp.setup(setSwitchweightByHostweight=True)

print exp.get_node("h1").cmd("ifconfig")  # call mininet cmd function of h1
print exp.get_node("h4").cmd("ifconfig")

print "waiting 5 seconds for routing algorithms on the controller to converge"
time.sleep(5)

print exp.get_node("h1").cmd("ping -c 5 10.0.0.4")

exp.stop()
