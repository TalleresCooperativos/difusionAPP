# difusion_app.py
# preferible usar python 3.7.3

import PySimpleGUI as sg

sg.Window(title = "hello world", layout =[[]
], margins = (500, 500)).read()



# panel de presentacion donde se redacta el mensaje

mensaje_viewer_column =  [  
            [sg.Text("What's your name?")],     
            [sg.Input()],
            [sg.Button('Ok')]
]


# caja de ingreso de texto y listado de los numeros


file_list_column = [
    [
            sg.Text("Image Folder"),
            sg.In(size=(25,1), enable_events=True, key="-FOLDER-"),
            sg.FolderBrowse(),
    ]
] 


