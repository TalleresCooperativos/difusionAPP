#difusion_app.py

import PySimpleGUI as sg

sg.Window(title = "hello world", layout =[[]
], margins = (500, 500)).read()



# presentacion donde se redacta el mensaje

mensaje_viewer_column = [
    [sg.Text("Choose an imagen on the list of the left:")],
    [sg.Text(size=(40,1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]


#caja de ingreso de texto 


file_list_column = [
    [
            sg.Text("Image Folder"),
            sg.In(size=(25,1), enable_events=True, key="-FOLDER-"),
            sg.FolderBrowse(),
    ]] 