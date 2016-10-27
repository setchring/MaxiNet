#!/usr/bin/python2

#
# Plotter for bachelor thesis results
#

import plotly.plotly as py
from plotly.graph_objs import *
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
    # trace10 = go.Box(
    #     y=[
    #         25.571568965911865,
    #         36.26844000816345,
    #         36.47072696685791,
    #         36.47522687911987,
    #         36.80563712120056
    #     ],
    #     name='240 Hosts',
    #     marker=dict(
    #         color='rgb(8, 81, 156)',
    #     ),
    #     boxmean='sd'
    # )
    # trace11 = go.Box(
    #     y=[
    #         88.68352913856506,
    #         80.14780402183533,
    #         82.73843598365784,
    #         84.35875296592712,
    #         86.76403188705444
    #     ],
    #     name='240 Container',
    #     marker=dict(
    #         color='rgb(10, 140, 208)',
    #     ),
    #     boxmean='sd'
    # )
    # trace12 = go.Box(
    #     y=[
    #         30.141373872756958,
    #         42.5898220539093,
    #         43.233330965042114,
    #         44.23212289810181,
    #         44.816850900650024
    #     ],
    #     name='280 Hosts',
    #     marker=dict(
    #         color='rgb(8, 81, 156)',
    #     ),
    #     boxmean='sd'
    # )
    # trace13 = go.Box(
    #     y=[
    #         107.80886006355286,
    #         96.45325303077698,
    #         99.27463698387146,
    #         102.14648795127869,
    #         104.41336393356323
    #     ],
    #     name='280 Container',
    #     marker=dict(
    #         color='rgb(10, 140, 208)',
    #     ),
    #     boxmean='sd'
    # )
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
        name='320 Container',
        marker=dict(
            color='rgb(10, 140, 208)',
        ),
        boxmean='sd'
    )
    data = [trace0, trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace14, trace15]
    layout = go.Layout(title='Startzeiten von Hosts bzw. Containern mit einem Worker', showlegend=False, yaxis=dict(
            title="Startzeit in Sekunden"
        ))
    figure = go.Figure(data=data, layout=layout)
    # py.plot(figure, auto_open=False)
    # py.iplot(figure, filename='svg75')
    from plotly.offline import init_notebook_mode, plot
    init_notebook_mode()
    plot(figure, image='svg', filename='einWorker.html')
    # py.image.save_as(figure, format='svg')


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
    # trace10 = go.Box(
    #     y=[
    #         29.72091507911682,
    #         30.075870037078857,
    #         30.25898790359497,
    #         30.211423873901367,
    #         30.677078008651733
    #     ],
    #     name='240 Hosts',
    #     marker=dict(
    #         color='rgb(8, 81, 156)',
    #     ),
    #     boxmean='sd'
    # )
    # trace11 = go.Box(
    #     y=[
    #         74.89307904243469,
    #         74.9702980518341,
    #         76.87759709358215,
    #         78.20884490013123,
    #         79.46793007850647
    #     ],
    #     name='240 Container',
    #     marker=dict(
    #         color='rgb(10, 140, 208)',
    #     ),
    #     boxmean='sd'
    # )
    # trace12 = go.Box(
    #     y=[
    #         36.64970803260803,
    #         36.93167185783386,
    #         37.233668088912964,
    #         37.48106002807617,
    #         37.63134694099426
    #     ],
    #     name='280 Hosts',
    #     marker=dict(
    #         color='rgb(8, 81, 156)',
    #     ),
    #     boxmean='sd'
    # )
    # trace13 = go.Box(
    #     y=[
    #         89.43371391296387,
    #         92.05170917510986,
    #         93.3434431552887,
    #         95.22685503959656,
    #         96.73871803283691
    #     ],
    #     name='280 Container',
    #     marker=dict(
    #         color='rgb(10, 140, 208)',
    #     ),
    #     boxmean='sd'
    # )
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
    data = [trace0, trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace14, trace15]
    layout = go.Layout(title='Startzeiten von Hosts bzw. Containern mit zwei Workern', showlegend=False,yaxis=dict(
            title="Startzeit in Sekunden"
        ))
    figure = go.Figure(data=data, layout=layout)
    # py.plot(figure, auto_open=False)
    from plotly.offline import init_notebook_mode, plot
    init_notebook_mode()
    plot(figure, image='svg', filename='zweiWorker.html')


def systemLastVergleich():
    trace1 = Box(
        y=[174.05624198913574, 173.948890209198, 173.94454908370972, 173.9467408657074, 173.94518518447876,
           173.95012092590332, 173.95043110847473, 173.94655680656433, 174.53029203414917, 173.9404320716858,
           173.9495029449463, 173.95225501060486, 173.94485592842102, 173.94097995758057, 173.96589398384094,
           173.9597988128662, 173.94549107551575, 173.9661078453064, 174.53516697883606, 173.98816299438477],
        boxmean='sd',
        marker=Marker(
            color='rgb(8, 81, 156)'
        ),
        name='2 Mininet Hosts (1W)',
        ysrc='setchring:97:12cf8c'
    )
    trace2 = Box(
        y=[174.0329999923706, 173.96394085884094, 173.95319485664368, 173.95863509178162, 173.94559407234192,
           173.95078206062317, 173.96819806098938, 173.94542288780212, 174.57363319396973, 173.9398968219757,
           173.95656490325928, 173.9443531036377, 173.94898891448975, 173.95273303985596, 173.9473750591278,
           173.95579290390015, 173.95104503631592, 173.97713804244995, 174.54663395881653, 173.96244096755981],
        boxmean='sd',
        marker=Marker(
            color='rgb(10, 140, 208)'
        ),
        name='2 Ubuntu Container (1W)',
        ysrc='setchring:97:28e33b'
    )
    trace3 = Box(
        y=[87.11957716941833, 87.00569295883179, 87.00749588012695, 87.01642107963562, 87.00478601455688,
           87.01821398735046, 87.0056049823761, 87.00564479827881, 87.00377297401428, 87.00858116149902,
           87.01909303665161, 87.01344585418701, 87.00871896743774, 87.01720023155212, 87.00548887252808,
           87.00659012794495, 87.00090003013611, 87.62443900108337, 87.60383987426758, 87.0222909450531],
        boxmean='sd',
        marker=Marker(
            color='rgb(8, 81, 156)'
        ),
        name='2 Mininet Hosts (2W)',
        ysrc='setchring:97:755dbf'
    )
    trace4 = Box(
        y=[87.10864400863647, 87.03255987167358, 87.00552487373352, 87.00663709640503, 86.99984693527222,
           87.00633597373962, 87.00061416625977, 87.0000250339508, 86.99881911277771, 87.00222516059875,
           87.00338101387024, 87.00585508346558, 87.00474500656128, 87.01482605934143, 87.00232291221619,
           87.00039505958557, 87.00300908088684, 87.0094940662384, 87.60664296150208, 87.00194597244263],
        boxmean='sd',
        marker=Marker(
            color='rgb(10, 140, 208)'
        ),
        name='2 Ubuntu Container (2W)',
        ysrc='setchring:97:056208'
    )
    data = Data([trace1, trace2, trace3, trace4])
    layout = Layout(
        showlegend=False,
        title='CPU Benchmark Laufzeiten von Hosts bzw. Containern',
        yaxis=dict(
            range=[0, 180],
            showgrid=True,
            zeroline=True,
            title="Laufzeit in Sekunden"
        ),
        xaxis=dict(tickangle=45)
    )
    fig = Figure(data=data, layout=layout)
    from plotly.offline import init_notebook_mode, plot
    init_notebook_mode()
    plot(fig, image='svg', filename='SystemLastVergleich.html')

def start160Sequenziell():
    import plotly.plotly as py
    from plotly.graph_objs import *
    py.sign_in('username', 'api_key')
    trace1 = Box(
        y=[16.710778951644897, 23.12172794342041, 23.15219497680664, 23.376353979110718, 23.672327041625977],
        boxmean='sd',
        marker=Marker(
            color='rgb(8, 81, 156)'
        ),
        name='Mininethosts (1W)',
        ysrc='setchring:81:588b00'
    )
    trace2 = Box(
        y=[18.521923065185547, 18.818742036819458, 18.903568029403687, 19.197312116622925, 19.296133041381836],
        boxmean='sd',
        marker=Marker(
            color='rgb(8, 81, 156)'
        ),
        name='Mininethosts (2W)',
        ysrc='setchring:81:188a28'
    )
    trace3 = Box(
        y=[55.71610999107361, 50.11128902435303, 51.42167401313782, 52.32876491546631, 53.01005816459656],
        boxmean='sd',
        marker=Marker(
            color='rgb(10, 140, 208)'
        ),
        name='Ubuntu Container (1W)',
        ysrc='setchring:81:fb5f3d'
    )
    trace4 = Box(
        y=[46.878589153289795, 47.398112058639526, 47.66672992706299, 48.80990219116211, 49.06117510795593],
        boxmean='sd',
        marker=Marker(
            color='rgb(10, 140, 208)'
        ),
        name='Ubuntu Container (2W)',
        ysrc='setchring:81:80411e'
    )
    data = Data([trace1, trace2, trace3, trace4])
    layout = Layout(
        showlegend=False,
        title='Startvergleich mit 160 Hosts bzw. Containern (Sequenziell)',
    yaxis = dict(
        range=[0, 60],
        showgrid=True,
        zeroline=True,
        title="Startzeit in Sekunden"
    ),
        xaxis=dict(tickangle=45)
    )
    fig = Figure(data=data, layout=layout)
    from plotly.offline import init_notebook_mode, plot
    init_notebook_mode()
    plot(fig, image='svg', filename='startvergleich160seq.html')
# tls.set_credentials_file(username='setchring', api_key='hhtnrk0t9x')

def start160Parralel():
    import plotly.plotly as py
    from plotly.graph_objs import *
    py.sign_in('username', 'api_key')
    trace1 = Box(
        y=[17.107424020767212, 23.18073296546936, 23.362980842590332, 23.812504053115845, 23.346518993377686],
        boxmean='sd',
        marker=Marker(
            color='rgb(8, 81, 156)'
        ),
        name='Mininethosts (1W)',
        ysrc='setchring:103:df6b28'
    )
    trace2 = Box(
        y=[11.409734010696411, 14.017661094665527, 14.139786958694458, 14.00459909439087, 13.936722993850708],
        boxmean='sd',
        marker=Marker(
            color='rgb(8, 81, 156)'
        ),
        name='Mininethosts (2W)',
        ysrc='setchring:103:e9dd30'
    )
    trace3 = Box(
        y=[62.070091009140015, 56.22917199134827, 56.44520902633667, 57.48769211769104, 58.8430700302124],
        boxmean='sd',
        marker=Marker(
            color='rgb(10, 140, 208)'
        ),
        name='Ubuntu Container (1W)',
        ysrc='setchring:103:5a50e4'
    )
    trace4 = Box(
        y=[32.30044984817505, 30.182456016540527, 30.279242038726807, 30.52851104736328, 30.67842388153076],
        boxmean='sd',
        marker=Marker(
            color='rgb(10, 140, 208)'
        ),
        name='Ubuntu Container (2W)',
        ysrc='setchring:103:58e6b9'
    )
    data = Data([trace1, trace2, trace3, trace4])
    layout = Layout(
        title='Startvergleich mit 160 Hosts bzw. Containern'
    )
    layout = Layout(
        showlegend=False,
        title='Startvergleich mit 160 Hosts bzw. Containern (Parallel)',
        yaxis=dict(
            range=[0, 70],
            showgrid=True,
            zeroline=True,
            title="Startzeit in Sekunden"
        ),
        xaxis=dict(tickangle=45))
    fig = Figure(data=data, layout=layout)
    from plotly.offline import init_notebook_mode, plot
    init_notebook_mode()
    plot(fig, image='svg', filename='startvergleich160paralel.html')

#systemLastVergleich()
plotBoxes()
plotBoxes2()
#start160Sequenziell()
#start160Parralel()