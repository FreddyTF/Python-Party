#!/usr/bin/env python
import PySimpleGUI as sg
# Simple example of TabGroup element and the options available to it

sg.theme('Python')     # Please always add color to your window

bg = sg.LOOK_AND_FEEL_TABLE[sg.CURRENT_LOOK_AND_FEEL]['BACKGROUND']

play = b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAByElEQVRoge3ZMWsUQRjG8Z8RFSKCgoJp0qSJjVpoZ2clkk8g5CtYpU+TD5DSUkvbVCFNYiM2dhZqY6GFQooEISGai8Xu4HgmcnM3c+su+4fj2L2dmedhb+Z95x16enp6hljBxaZF5OAE7/GoaSGTchJ9tnCrWTnjE0zs19+HWMPlJkWNQzAyh2c4rq+/YBnnmpOWRjASuIfX0f0d3GlAVzLDRmBG9Ta+1r8d4wVuTFdaGqcZCVzFOn7Uz+ziKc5PR1oa/zISWMRm9OxbPCisK5lRjASW8Clqs4H5MrLSSTECs1jFQd3ue319KbewVFKNBBbwMmr/EY8z6kpmXCOBh3gX9dNYdjCpEbigWs326r6OVKvdlQn7TSKHkcCcKt4MNJAd5DQSuI83Ud87uJ15jL8oYYTf2cE3f2YH1wuMhXJGAtdU8+WnwtlBaSOBu3gVjZc9O5iWEapJ/wSf6zEHeI6bZzWYmY6u/4v+rzUirZ/snVh+hwPitpYFxNanKJ1IGk9L4xcz6Eom18bqg5ZtrDqx1Y2LDwPVG2lV8aH15aDWF+jOKpkWi8o5GKWIXTwq56BzxwqdOejpxNFbJw5DO3M83dPT02J+AbN50HbYDxzCAAAAAElFTkSuQmCC'
stop = b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAAaklEQVRoge3ZQQqAMAxFwSre/8p6AZFUiXzKzLqLPNJVOwYAvLcVzpztU9Q8zrr/NUW3Y+JsZXsdSjdimY0ISSMkjZA0QtIISSMkjZA0QtIISSMkjZA0QtIISSMkzcxrfMo/ya1lNgIAX1zq+ANHUjXZuAAAAABJRU5ErkJggg=='
eject = b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAABmJLR0QA/wD/AP+gvaeTAAAByklEQVRoge3YO2gUURSA4S+JRnyACIGADyxERAsb0UKrWIidWIidlSA2YpFWSauNVtrYiIU2YpFCLGwEEWwsBAsLEbFQFARFfKBZizkyK5pkZvZmZ7PeH05z595z/sPszpxdMplMJpMZbDZFLGsm8CxiomWXxqzBQ3QiHmNdq0YNGMc9RQOvIjqxNt6iVy1GcF0h/h47sR1vY+0mRluzq8ElhfBn7O9a34tPce1KC161OK8Q/Y7D/7h+EF9jz7k+etXilELwJ44vsO8ofsTeM33wqsURpdzZCvtPK5s+toRetZjCF4XYTI1zM3HmGw4lt6rJbnxQCF1tcP5ynP2IPQm9arENb0LkDsYa5BjFrcjxDjuS2VVkI16EwH2s6iHXStxVvjy39GxXkfV4Iu3Y0T3OPMWGBDkXZDUeRMHnmEyY+/eA2cEjrE2Y+w/GcDsKvcbWJaixGS+jxixWpC4wgmvK+WlX6gJddM9lN6J2Mi4q56cDKRPPwz7lXHYhVdJp5W+KtmK61yZOYG4AGpnDyV6byWT+ZxZ7Rnf6YlGdeX2XxZ8AVag6AiR9uzZg0U/G0NyR3MigUfU7MmhPr78YmjuSyWQymUxmmPgFokSdfYSQKDwAAAAASUVORK5CYII='

#API
width = 2
height = 2

# The tab 1, 2, 3 layouts - what goes inside the tab
configurationLayout = [
                        [sg.Text('Konfiguration')],
                        [sg.Text('Put your layout in here')],
                        [sg.Text('Input something'), sg.Input(size=(12,1), key='-IN-TAB1-')]
                    ]

simulationLayout = [[
    #sg.Text('Simulation'),
    sg.Text('Iteration'),
    ],
    [
    sg.Table(values=[['0' for _ in range(width)] for _ in range(height)],headings=[str(i) for i in range(width)],auto_size_columns=True),
    ],
    [
    sg.Button(image_data=play, key='Play', border_width=0, button_color=(bg, bg)),
    sg.Button(image_data=stop, key='Stop',  button_color=(bg, bg), border_width=0),
    sg.Button(image_data=eject, key='Exit',  button_color=(bg, bg), border_width=0),
    [
        [
            sg.Text('Anzahl Iterationen:'),
            sg.Input(size=(12,1), key='-IN-TAB1-'),
        ],
        [
            sg.Text('Verzögerung:'),
            sg.Input(size=(12,1), key='-IN-TAB1-'),
        ]
    ]
    ]]


resultLayout = [[sg.Text('Auswertung')]]

# The TabgGroup layout - it must contain only Tabs
tab_group_layout = [[
    sg.Tab(
        'Konfiguration', 
        simulationLayout, 
        font='Courier 15', 
        key='-TAB1-'
        ),
                     
    sg.Tab(
        'Simulation', 
        configurationLayout, 
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
          [sg.Text('Make tab number'), sg.Input(key='-IN-', size=(3,1)), sg.Button('Invisible'), sg.Button('Visible'), sg.Button('Select')]]

window = sg.Window(
    'My window with tabs', 
    layout, 
    no_titlebar=False,
    #modal=True,
    resizable=True,
    )

tab_keys = ('-TAB1-','-TAB2-','-TAB3-')         # map from an input value to a key
while True:
    event, values = window.read()       # type
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    # handle button clicks
    if event == 'Invisible':
        window[tab_keys[int(values['-IN-'])-1]].update(visible=False)
    if event == 'Visible':
        window[tab_keys[int(values['-IN-'])-1]].update(visible=True)
    if event == 'Select':
        window[tab_keys[int(values['-IN-'])-1]].select()

window.close()