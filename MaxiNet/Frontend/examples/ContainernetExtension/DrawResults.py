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


def plotBoxes():
    import plotly.plotly as py
    import plotly.graph_objs as go

    trace0 = go.Box(
        y=[
                1.220966100692749,
                1.194838047027588,
                1.1900928020477295,
                1.1873359680175781,
                1.1871559619903564
            ],
        name='10 Hosts',
        marker=dict(
            color='rgb(8, 81, 156)',
        ),
        boxmean='sd'
    )
    trace1 = go.Box(
        y=[
                3.0607070922851562,
                2.8704521656036377,
                2.8041749000549316,
                2.836987018585205,
                2.9370028972625732
            ],
        name='10 Container',
        marker=dict(
            color='rgb(10, 140, 208)',
        ),
        boxmean='sd'
    )
    trace2 = go.Box(
        y=[
                2.177574872970581,
                2.158424139022827,
                2.41457200050354,
                2.20817494392395,
                2.299355983734131
            ],
        name='20 Hosts',
        marker=dict(
            color='rgb(8, 81, 156)',
        ),
        boxmean='sd'
    )
    trace3 = go.Box(
        y=[
                5.638598918914795,
                5.547015905380249,
                5.462399005889893,
                5.517163038253784,
                5.487725019454956
            ],
        name='20 Container',
        marker=dict(
            color='rgb(10, 140, 208)',
        ),
        boxmean='sd'
    )
    trace4 = go.Box(
        y=[
                4.118584156036377,
                4.858264923095703,
                4.982507944107056,
                5.070256948471069,
                4.854703903198242
            ],
        name='40 Hosts',
        marker=dict(
            color='rgb(8, 81, 156)',
        ),
        boxmean='sd'
    )
    trace5 = go.Box(
        y=[
                12.242072105407715,
                11.051261901855469,
                11.07240915298462,
                11.05888319015503,
                11.168780088424683
            ],
        name='40 Container',
        marker=dict(
            color='rgb(10, 140, 208)',
        ),
        boxmean='sd'
    )
    trace6 = go.Box(
        y=[
                8.297120094299316,
                10.70746111869812,
                11.330874919891357,
                11.29092288017273,
                11.357799053192139
            ],
        name='80 Hosts',
        marker=dict(
            color='rgb(8, 81, 156)',
        ),
        boxmean='sd'
    )
    trace7 = go.Box(
        y=[
                25.65382409095764,
                22.612013816833496,
                22.563922882080078,
                22.958635807037354,
                23.199914932250977
            ],
        name='80 Container',
        marker=dict(
            color='rgb(10, 140, 208)',
        ),
        boxmean='sd'
    )
    trace8 = go.Box(
        y=[
                16.710778951644897,
                23.12172794342041,
                23.15219497680664,
                23.376353979110718,
                23.672327041625977
            ],
        name='160 Hosts',
        marker=dict(
            color='rgb(8, 81, 156)',
        ),
        boxmean='sd'
    )
    trace9 = go.Box(
        y=[
                55.71610999107361,
                50.11128902435303,
                51.42167401313782,
                52.32876491546631,
                53.01005816459656
            ],
        name='160 Container',
        marker=dict(
            color='rgb(10, 140, 208)',
        ),
        boxmean='sd'
    )
    trace10 = go.Box(
        y=[
                25.571568965911865,
                36.26844000816345,
                36.47072696685791,
                36.47522687911987,
                36.80563712120056
            ],
        name='240 Hosts',
        marker=dict(
            color='rgb(8, 81, 156)',
        ),
        boxmean='sd'
    )
    trace11 = go.Box(
        y=[
                88.68352913856506,
                80.14780402183533,
                82.73843598365784,
                84.35875296592712,
                86.76403188705444
            ],
        name='240 Container',
        marker=dict(
            color='rgb(10, 140, 208)',
        ),
        boxmean='sd'
    )
    trace12 = go.Box(
        y=[
                30.141373872756958,
                42.5898220539093,
                43.233330965042114,
                44.23212289810181,
                44.816850900650024
            ],
        name='280 Hosts',
        marker=dict(
            color='rgb(8, 81, 156)',
        ),
        boxmean='sd'
    )
    trace13 = go.Box(
        y=[
                107.80886006355286,
                96.45325303077698,
                99.27463698387146,
                102.14648795127869,
                104.41336393356323
            ],
        name='280 Container',
        marker=dict(
            color='rgb(10, 140, 208)',
        ),
        boxmean='sd'
    )
    trace14 = go.Box(
        y=[
                34.71859788894653,
                48.50111699104309,
                49.38033485412598,
                51.087302923202515,
                51.66889476776123
            ],
        name='320 Hosts',
        marker=dict(
            color='rgb(8, 81, 156)',
        ),
        boxmean='sd'
    )
    trace15 = go.Box(
        y=[-1],
        name='320 Container (Fehler)',
        marker=dict(
            color='rgb(10, 140, 208)',
        ),
        boxmean='sd'
    )
    data = [trace0, trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10, trace11, trace12, trace13, trace14, trace15]
    layout = go.Layout(title='Startzeiten von Hosts bzw. Containern mit einem Worker', showlegend=False)
    figure = go.Figure(data=data, layout=layout)
    py.plot(figure, auto_open=False)


def plotBoxes2():
    import plotly.plotly as py
    import plotly.graph_objs as go

    trace0 = go.Box(
        y=[
                1.35548996925354,
                1.3441359996795654,
                1.3321261405944824,
                1.3552589416503906,
                1.4191999435424805
            ],
        name='10 Hosts',
        marker=dict(
            color='rgb(8, 81, 156)',
        ),
        boxmean='sd'
    )
    trace1 = go.Box(
        y=[
                3.0793659687042236,
                3.071715831756592,
                2.9316048622131348,
                2.977012872695923,
                3.0160839557647705
            ],
        name='10 Container',
        marker=dict(
            color='rgb(10, 140, 208)',
        ),
        boxmean='sd'
    )
    trace2 = go.Box(
        y=[
                2.4199891090393066,
                2.305997133255005,
                2.3410701751708984,
                2.398021936416626,
                2.390981912612915
            ],
        name='20 Hosts',
        marker=dict(
            color='rgb(8, 81, 156)',
        ),
        boxmean='sd'
    )
    trace3 = go.Box(
        y=[
                5.805190086364746,
                5.519806861877441,
                5.623938083648682,
                5.696949005126953,
                5.692356109619141
            ],
        name='20 Container',
        marker=dict(
            color='rgb(10, 140, 208)',
        ),
        boxmean='sd'
    )
    trace4 = go.Box(
        y=[
                4.37345290184021,
                4.27826714515686,
                4.418522119522095,
                4.3067498207092285,
                4.399266004562378
            ],
        name='40 Hosts',
        marker=dict(
            color='rgb(8, 81, 156)',
        ),
        boxmean='sd'
    )
    trace5 = go.Box(
        y=[
                10.92971396446228,
                10.761906862258911,
                10.886162996292114,
                11.101104974746704,
                10.988735914230347
            ],
        name='40 Container',
        marker=dict(
            color='rgb(10, 140, 208)',
        ),
        boxmean='sd'
    )
    trace6 = go.Box(
        y=[
                8.743327856063843,
                8.655654907226562,
                8.607124090194702,
                8.785256147384644,
                8.714077949523926
            ],
        name='80 Hosts',
        marker=dict(
            color='rgb(8, 81, 156)',
        ),
        boxmean='sd'
    )
    trace7 = go.Box(
        y=[
                22.36103916168213,
                22.424012899398804,
                22.47895622253418,
                22.36395001411438,
                22.528213024139404
            ],
        name='80 Container',
        marker=dict(
            color='rgb(10, 140, 208)',
        ),
        boxmean='sd'
    )
    trace8 = go.Box(
        y=[
                18.521923065185547,
                18.818742036819458,
                18.903568029403687,
                19.197312116622925,
                19.296133041381836
            ],
        name='160 Hosts',
        marker=dict(
            color='rgb(8, 81, 156)',
        ),
        boxmean='sd'
    )
    trace9 = go.Box(
        y=[
                46.878589153289795,
                47.398112058639526,
                47.66672992706299,
                48.80990219116211,
                49.06117510795593
            ],
        name='160 Container',
        marker=dict(
            color='rgb(10, 140, 208)',
        ),
        boxmean='sd'
    )
    trace10 = go.Box(
        y=[
                29.72091507911682,
                30.075870037078857,
                30.25898790359497,
                30.211423873901367,
                30.677078008651733
            ],
        name='240 Hosts',
        marker=dict(
            color='rgb(8, 81, 156)',
        ),
        boxmean='sd'
    )
    trace11 = go.Box(
        y=[
                74.89307904243469,
                74.9702980518341,
                76.87759709358215,
                78.20884490013123,
                79.46793007850647
            ],
        name='240 Container',
        marker=dict(
            color='rgb(10, 140, 208)',
        ),
        boxmean='sd'
    )
    trace12 = go.Box(
        y=[
                36.64970803260803,
                36.93167185783386,
                37.233668088912964,
                37.48106002807617,
                37.63134694099426
            ],
        name='280 Hosts',
        marker=dict(
            color='rgb(8, 81, 156)',
        ),
        boxmean='sd'
    )
    trace13 = go.Box(
        y=[
                89.43371391296387,
                92.05170917510986,
                93.3434431552887,
                95.22685503959656,
                96.73871803283691
            ],
        name='280 Container',
        marker=dict(
            color='rgb(10, 140, 208)',
        ),
        boxmean='sd'
    )
    trace14 = go.Box(
        y=[
                42.13955593109131,
                35.43569993972778,
                35.852705001831055,
                35.9057719707489,
                36.216508865356445
            ],
        name='320 Hosts',
        marker=dict(
            color='rgb(8, 81, 156)',
        ),
        boxmean='sd'
    )
    trace15 = go.Box(
        y=[
                99.17356204986572,
                97.3440489768982,
                98.98178291320801,
                100.91142106056213,
                102.85055303573608
            ],
        name='320 Container',
        marker=dict(
            color='rgb(10, 140, 208)',
        ),
        boxmean='sd'
    )
    data = [trace0, trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10, trace11, trace12, trace13, trace14, trace15]
    layout = go.Layout(title='Startzeiten von Hosts bzw. Containern mit zwei Workern', showlegend=False)
    figure = go.Figure(data=data, layout=layout)
    py.plot(figure, auto_open=False)

tls.set_credentials_file(username='setchring', api_key='hhtnrk0t9x')

plotBoxes2()
