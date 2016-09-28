#!/usr/bin/python2

#
# Minimal example showing how to use MaxiNet
#

import time, sys

from MaxiNet.Frontend.containernetWrapper import ContainernetTopo, ContainerExperiment
from MaxiNet.Frontend.maxinet import Cluster
from mininet.log import setLogLevel, info
from mininet.node import OVSSwitch
from time import time
import plotly.tools as tls


def plotBoxes(mininetHostTimes1, mininetHostTimes2, dockerHostTimes1, dockerHostTimes2, hostnumber):
    import plotly.plotly as py
    import plotly.graph_objs as go

    trace0 = go.Box(
        y=mininetHostTimes1,
        name='Mininethosts (Ein Worker)',
        marker=dict(
            color='rgb(8, 81, 156)',
        ),
        boxmean='sd'
    )
    trace1 = go.Box(
        y=mininetHostTimes2,
        name='Mininethosts (Zwei Worker)',
        marker=dict(
            color='rgb(8, 81, 156)',
        ),
        boxmean='sd'
    )
    trace2 = go.Box(
        y=dockerHostTimes1,
        name='Ubuntu Container (Ein Worker)',
        marker=dict(
            color='rgb(10, 140, 208)',
        ),
        boxmean='sd'
    )
    trace3 = go.Box(
        y=dockerHostTimes2,
        name='Ubuntu Container (Zwei Worker)',
        marker=dict(
            color='rgb(10, 140, 208)',
        ),
        boxmean='sd'
    )
    data = [trace0, trace1, trace2, trace3]
    layout = go.Layout(title='Startvergleich mit ' + str(hostnumber) + ' Hosts bzw. Containern')
    figure = go.Figure(data=data, layout=layout)
    py.plot(figure, auto_open=False)


def runHostTopo(n, maxWorker, dimage=None):
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

    cluster = Cluster(minWorkers=maxWorker, maxWorkers=maxWorker)

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


def maintest(numOfHosts, runs, file):
    elapsedTimeNormal_1Worker, elapsedTimeUbuntu_1Worker, elapsedTimeNormal_2Worker, elapsedTimeUbuntu_2Worker = [], [], [], []

    # logFile = open('/tmp/measurementsMininetVSDocker.csv', 'w')

    for i in xrange(1, runs + 1):
        elapsedTimeNormal_1Worker.append(runHostTopo(numOfHosts, 1))

    for i in xrange(1, runs + 1):
        elapsedTimeUbuntu_1Worker.append(runHostTopo(numOfHosts, 1, "ubuntu:trusty"))

    for i in xrange(1, runs + 1):
        elapsedTimeNormal_2Worker.append(runHostTopo(numOfHosts, 2))

    for i in xrange(1, runs + 1):
        elapsedTimeUbuntu_2Worker.append(runHostTopo(numOfHosts, 2, "ubuntu:trusty"))

    file.write('elapsedTimeNormal_1Worker\n')
    file.write(str(elapsedTimeNormal_1Worker))

    file.write('\nelapsedTimeNormal_2Worker\n')
    file.write(str(elapsedTimeNormal_2Worker))

    file.write('\nelapsedTimeUbuntu_1Worker\n')
    file.write(str(elapsedTimeUbuntu_1Worker))

    file.write('\nelapsedTimeUbuntu_2Worker\n')
    file.write(str(elapsedTimeUbuntu_2Worker))

    plotBoxes(elapsedTimeNormal_1Worker, elapsedTimeNormal_2Worker, elapsedTimeUbuntu_1Worker,
              elapsedTimeUbuntu_2Worker, numOfHosts)


tls.set_credentials_file(username='setchring', api_key='hhtnrk0t9x')

setLogLevel('info')

logfile = open('/tmp/evaluationLog', 'w')
sys.stderr = logfile
sys.stdin = logfile

f = open('/tmp/results', 'w')

j = 10

while j < 1000:
    maintest(j, 15, f)
    j += 10

f.close()
logfile.close()
# print 'Startup time normal hosts: %d seconds' % (elapsedTimeNormal/runs)
# print 'Startup time docker \"%s\" hosts: %d seconds' % ("ubuntu:trusty", elapsedTimeUbuntu/runs)
