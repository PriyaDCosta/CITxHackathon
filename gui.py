import PySimpleGUI as sg
import Speech2Text_jc as stt

layout = [[sg.Text("You can Start Recording Here!")], [sg.Button("Record")],[sg.Text("Click Below to stop Recording!")], [sg.Button("Stop Recording")]]

# Create the window
window = sg.Window("Transcription App", layout)

# Create an event loop
while True:
    event, values = window.read()

    # End program if user closes window or
    # presses the OK button
    if event == "Stop Recording" or event == sg.WIN_CLOSED:
        break
window.close()