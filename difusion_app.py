# difusion_app.py
# preferible usar python 3.7.3

import PySimpleGUI as sg



# panel de presentacion donde se redacta el mensaje

mensaje_viewer_column =  [  
            [sg.Text("ingese su mensaje")],
            [sg.Input()],
            [sg.Button('ENVIAR')]
]


# caja de ingreso de texto y listado de los numeros


celu_list_column = [
            sg.Text("numero de celular"),
            [sg.Input()],
            [sg.Button('Ok')]
    ]


layout = [
    [
        sg.Column(celu_list_column),
        sg.VSeparator(),
        sg.Column(mensaje_viewer_column),
    ]
]




window = sg.Window("Image Viewer",layout)

# event loop

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

window.close()


# ultima modificacion