#!/usr/bin/env python
"""
gui.py -

author: python party
date: 26.04.22
version: 0.0.1
license: MIT
"""
import PySimpleGUI as sg
from __pycache__.cache import cache
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
import sys, os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from DataManager.Datamodel import Person, Party, Spielfeld, Beziehung
from ImportAndExport import importData
import json
#from ImportAndExport import exportData

party = importData.importFromJson("config_example.json")

# Simple example of TabGroup element and the options available to it

sg.theme('Python')     # Please always add color to your window

BUTTON_SIZE = (40,40)
AUSWERTUNG_BUTTON_SIZE = (8,1)
INPUT_SIZE = (5,1)
FRAME_PADDING = (20,5)

bg = sg.LOOK_AND_FEEL_TABLE[sg.CURRENT_LOOK_AND_FEEL]['BACKGROUND']

play            = b'iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAABD0lEQVR4Ae3cMQ0CQQAEQGho6XGABlTgAhe4QAYq0IACBNBSkGObU0A+m3xmklWwCSzP/W0WBAAAAAAAAAD35JCUMJJ3ckm2SYECZh7JMSlQwMwnuSa7hEIBM8/klFAoYOab3JJ9QqGAmVdyTigVMGOyNgsoT1YFlCerAsqTVQHlyaqA8mRVQHmyKqA8WRVQnqwKKE9WBZQnqwLKk1UB5cmqgPJkVcAqJ6sCTNbRjck6ujFZRzcm6+jGZB29mKwKUICPIF/CCjBD/RBTgEcRHsZ5HF3gDxlMS3/KFziWgoNZjibicK7j6ZiWXlH6j5f08JqqF7VxVYHLOnBdjQubcGWZS/twbSUAAAAAAAAA/ADdgMtRnVRE7AAAAABJRU5ErkJggg=='
fast_forward    = b'iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAQAAABIkb+zAAABTElEQVR42u2auU1DQRRFryyRkJA5JCamADdABZTgCiiBClwCFbgBCiB3SkjmiAQhDZoIeeXz/5vlwjmTn6crebmzSAAAAAAAAAAAAMd40lVXnl+T9KpFR54Rg5M+9aiLTjyjBuf1opsuPKMHJ71r2YFnwuC81po39kwcnPSmu6aeyYPzWumymSdkcNJGt408QQGSPvSgWQNPWIC8nnVd3RMaIGmr+8qe4AB5DWs5UZ4CAYa1nChPkQBDWk6Up1CAn1tOlKdggPMtJ8pTNMC5lhPlKR7gVMuJ8lQIcLzlRHkqBThsOVGeagH2W06Up2KA3ZYT5akc4LvlRHkI8I8+QuZfYvOfUes/MvMqYV3mzOu09YbGfEtpvqm3PlYxP9iyPlo0P9w1P163vuAwv2KyvuQzv2a1vug2f2pg/tjD/rkNAAAAAAAAAAD8Rb4AZBxZqxbx4MsAAAAASUVORK5CYII='
pause           = b'iVBORw0KGgoAAAANSUhEUgAAAGAAAABgAQMAAADYVuV7AAAABlBMVEUAAAAAAAClZ7nPAAAAAXRSTlMAQObYZgAAABdJREFUeAFjAINR8P8/CA8nzihnlDMKAALA3yHZSvG0AAAAAElFTkSuQmCC'
skip_forward    = b'iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAQAAABIkb+zAAABFElEQVR42u3asU0DQQBE0ZElEhIyQmJiF0ADVEAJVEAJroASqIAGXAA5KSEZEQmyNOQY4zvJSPvt/5wjfQnD3O4lkiRJkiRJ0hRPuTjoz+uPz79r3nLDDmg2WeWMHNA0L7lmBzSfuWcHNM1zLtkBzXtu2QFN85hzdkDzmiU7oPnKQxbkgKZZ54od0Hzkjh3QdOZaGjBg3loaMmDOWho0YPpaGjhg2loaOmDKWho+YN9aAgT8vZYgAbvXEiZg11oCBfy+lmAB22vJAH+FTuVLDP8ziv5HBp8S6DEHn9PoBxr4IyX8oR59rAI/2EIfLcIPd+HH6+gLDvgVE/qSD37Nir7ohr9qAH/ZA/+6jSRJkiRJko7BNzOGq2XyvK9AAAAAAElFTkSuQmCC'
stop            = b'iVBORw0KGgoAAAANSUhEUgAAAGAAAABgAQMAAADYVuV7AAAABlBMVEUAAAAAAAClZ7nPAAAAAXRSTlMAQObYZgAAABhJREFUeAFjIBuMgv9gQGvOKGeUQy4YBQBv1R7w9ogoGwAAAABJRU5ErkJggg=='

# ------------------------------------------ API ------------------------------------------------
width = 10
height = 10
persons = [F'SACK{j}' for j in range(10)]

# ------------------------------- PASTE YOUR MATPLOTLIB CODE HERE -------------------------------

values_to_plot = (20, 35, 30, 35, 27)
ind = np.arange(len(values_to_plot))
p_width = 0.4

p1 = plt.bar(ind, values_to_plot, p_width)

plt.ylabel('Y-Axis Values')
plt.title('Plot Title')
plt.xticks(ind, ('Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0],), ('Data Group 1',))


# ------------------------------- END OF YOUR MATPLOTLIB CODE -------------------------------

# ------------------------------- Beginning of Matplotlib helper code -----------------------

def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, master=canvas)
    print(canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

# ------------------------------- Beginning of GUI CODE -------------------------------

# The tab 1, 2, 3 layouts - what goes inside the tab
configurationLayout = [
    [sg.Text("Konfiguration durch Import")],
    [sg.Text("Importpfad: "), sg.Text(""), sg.FileBrowse(key="-IMPORTPATH-")],
    [sg.Button("Importieren")],
    [sg.Text('Manuelle Komfiguration:')],
    [sg.Text('ID: ', size=(15, 1)), sg.InputText()],
    [sg.Text('Name: ', size=(15, 1)), sg.InputText()],
    [sg.Text('Startposition: ', size=(15, 1)), sg.InputText()],
    [sg.Submit()],
    

    [sg.Button("Exportieren")]
]


simulationLayout = [[
    sg.Column([
        [
        #sg.Text('Simulation'),
        sg.Text('Iteration',key='-ITER-'),
        ],
        [sg.Column([[sg.Button('-', size=(2, 1), key=(i,j), pad=(0,0), disabled=True)] for j in range(width)],pad=(0,5)) for i in range(height)] + [sg.Frame('Legende',[[sg.Column([[sg.Text(text=person)] for person in persons])]], p=FRAME_PADDING)],
        [
        *[sg.Column([[sg.Button(image_data=button[0], key=button[1],button_color=(bg, bg), border_width=0, image_size=BUTTON_SIZE)],[sg.Text(button[1])]], element_justification='center') for button in [(stop,'Stop'),(play,'Play'),(pause,'Pause'),(skip_forward,'Iteration'),(fast_forward,'Guest')]],
        sg.Frame('Konfigurationen', [[
            sg.Column([  
            [sg.Text('Anzahl Iterationen:'  ,expand_x=True),sg.Input(size=INPUT_SIZE, key='-IN-TAB1-')],
            [sg.Text('Verzögerung:'         ,expand_x=True),sg.Input(size=INPUT_SIZE, key='-IN-TAB1-')],
            ]),
            ]]),
        ]
    ]),
    sg.VerticalSeparator(),
    sg.Column([
        [
            sg.Frame('OnlineStatistik',
            [
                []
            ])
        ],
        [
            sg.Text('durchschnittliches\nParty-Unbehagen:',expand_x=True),
            sg.Input(size=INPUT_SIZE, key='-IN-TAB1-')
        ]
    ])
]]

fig = plt.gcf()  # if using Pyplot then get the figure from the plot
figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds

resultLayout = [
    [
        sg.Button(button_text=button[0],k=button[1], s=AUSWERTUNG_BUTTON_SIZE) for button in [('Laden...','load'),('Sichern...','safe'),('Reset','reset')]
    ],
    [
        sg.Frame('Legende',[[sg.Column([[sg.Text(text=person)] for person in persons])]], p=FRAME_PADDING),
        sg.Canvas(size=(figure_w, figure_h), key='-CANVAS-')
    ],
    [
        sg.Text('durchschnittliches\nParty-Unbehagen:'),
        sg.Input(size=INPUT_SIZE, key='-IN-TAB1-'),
        sg.Text('Party-Bewertung: '),
        sg.Input(size=INPUT_SIZE, key='-IN-TAB1-')
    ]   
]

# The TabgGroup layout - it must contain only Tabs
tab_group_layout = [[
    sg.Tab(
        'Konfiguration', 
        configurationLayout, 
        font='Courier 15', 
        key='-TAB1-'
        ),
                     
    sg.Tab(
        'Simulation', 
        simulationLayout, 
        key='-TAB2-'
        ),
                     
    sg.Tab(
        'Auswertung', 
        resultLayout, 
        key='-TAB3-'),
    ]]

# The window layout - defines the entire window
layout = [[sg.TabGroup(
                    tab_group_layout,
                    enable_events=True,
                    key='-TABGROUP-',
                    #expand_x=True,
                    #expand_y=True
                       )],
          ]

cache = cache(layout)

tab_keys = ('-TAB1-','-TAB2-','-TAB3-')         # map from an input value to a key

drawn = False

party = importData.importFromJson("config_example.json")

while True:
    event, values = cache.read()       # type
    print(event, values)
    # add the plot to the window
    if not drawn:
        fig_photo = draw_figure(cache['-CANVAS-'].TKCanvas, fig)
        drawn = True
    if event == 'Importieren':
        party = importData.importFromJson(values['-IMPORTPATH-'])
    if event == 'Exportieren':
        jsonStr = json.dumps(party.personenliste.__dict__)
        print(jsonStr)
    if event == sg.WIN_CLOSED:
        cache.close()
        break