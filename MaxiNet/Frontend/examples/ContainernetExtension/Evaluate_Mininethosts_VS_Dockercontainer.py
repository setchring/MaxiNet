#!/usr/bin/python2

#
# Minimal example showing how to use MaxiNet
#

import time

from MaxiNet.Frontend.containernetWrapper import ContainernetTopo, ContainerExperiment
from MaxiNet.Frontend.maxinet import Cluster
from mininet.log import setLogLevel, info
from mininet.node import OVSSwitch
from time import  time
import plotly.tools as tls


def plotBoxes(mininetHostTimes, dockerHostTimes):
    from plotly.graph_objs import Bar, Scatter, Figure, Layout
    import plotly.plotly as py
    import plotly.graph_objs as go

    trace0 = go.Box(
        y=mininetHostTimes,
        name='Startzeit Mininet Hosts',
        marker=dict(
            color='rgb(8, 81, 156)',
        ),
        boxmean='sd'
    )
    trace1 = go.Box(
        y=dockerHostTimes,
        name='Startzeit Ubuntu Container',
        marker=dict(
            color='rgb(10, 140, 208)',
        ),
        boxmean='sd'
    )
    data = [trace0, trace1]
    layout = Layout(title='My Plot')
    py.plot(data, layout)


def runHostTopo(n, minWorker, dimage=None):
    n += 1
    topo = ContainernetTopo(controller=OVSSwitch)

    info('*** Adding switch\n')
    s1 = topo.addSwitch('s1')
    s2 = topo.addSwitch('s2')

    topo.addLink(s1, s2)

    info('*** Adding hosts\n')

    L = list()

    if not dimage:
        for i in xrange(2, n):
            h = topo.addHost('h{0}'.format(i * 2))
            topo.addLink(s1, h)
            L.append(h)

        for i in xrange(1, n):
            h = topo.addHost('h{0}'.format((i * 2) + 1))
            topo.addLink(s2, h)
            L.append(h)

    else:
        for i in xrange(2, n):
            d = topo.addDocker('d{0}'.format(i * 2), ip='10.0.0.{0}'.format(i * 2), dimage=dimage)
            topo.addLink(s1, d)
            L.append(d)

        for i in xrange(1, n):
            d = topo.addDocker('d{0}'.format((i * 2) + 1), ip='10.0.0.{0}'.format((i * 2) + 1), dimage=dimage)
            topo.addLink(s2, d)
            L.append(d)

    cluster = Cluster(minWorkers=minWorker)

    exp = ContainerExperiment(cluster, topo, switch=OVSSwitch)

    start = time()
    exp.setup()

    # for host in L:
    #    while exp.ping(hosts=[host, h1]) != 0.0:
    #        sleep(5)

    end = time()
    elapsedTime = end - start
    print(elapsedTime)

    exp.stop()
    cluster.remove_workers()

    return elapsedTime


tls.set_credentials_file(username='setchring', api_key='hhtnrk0t9x')

setLogLevel('info')

# test startup for n mininet hosts
n = 5
# number of testruns
runs = 2

elapsedTimeNormal_1Worker, elapsedTimeUbuntu_1Worker, elapsedTimeNormal_2Worker, elapsedTimeUbuntu_2Worker = [], [], [], []

#logFile = open('/tmp/measurementsMininetVSDocker.csv', 'w')

# for i in xrange(1, runs + 1):
#     elapsedTimeNormal_1Worker.append(runHostTopo(n, 1))
#
# for i in xrange(1, runs + 1):
#     elapsedTimeUbuntu_1Worker.append(runHostTopo(n, 1, "ubuntu:trusty"))
#
# for i in xrange(1, runs + 1):
#     elapsedTimeNormal_2Worker.append(runHostTopo(n, 2))
#
# for i in xrange(1, runs + 1):
#     elapsedTimeUbuntu_2Worker.append(runHostTopo(n, 2, "ubuntu:trusty"))
elapsedTimeNormal_1Worker = [1, 3]
elapsedTimeUbuntu_1Worker = [1, 4]
plotBoxes(elapsedTimeNormal_1Worker, elapsedTimeUbuntu_1Worker)

#print 'Startup time normal hosts: %d seconds' % (elapsedTimeNormal/runs)
#print 'Startup time docker \"%s\" hosts: %d seconds' % ("ubuntu:trusty", elapsedTimeUbuntu/runs)
