import speech_recognition as sr
import json
from datetime import datetime
import os.path
import PySimpleGUI as sg
import pandas as pd

'''
CITxHackathon Speech2Text App
Authors: Priya DCosta, Sean Chuang, James Chin

Date: 16 January 2023
'''

# GUI window
with open("TeamCurryLogo.png", "rb") as f:
    image_bytes = f.read()

layout = [[sg.Image(data=image_bytes)],
            [sg.Text('Press start button to record')],
          [sg.Button('Start'), sg.Button('Stop')]]

window = sg.Window('Team Curry\'s CITxHackathon Speech2Text', layout, size=(400,300), resizable=True, background_color='green')


r = sr.Recognizer()
run=True
data = {}

if os.path.exists("notepad.json"):
    print("notepad.json exists")
#with open(f"{new_file_name}.json","r") as f:
    with open("notepad.json","r") as f:
        try:
            data = json.load(f)
            print("data:", data)
        except json.decoder.JSONDecodeError as e:
            print("Error loading json file:", str(e))
else:
    data={"notes":[]}


while True:
    event, values = window.read()
    if event in (None, 'Stop'):
        print('Stopping')
        run = False
        break

    elif event == 'Start':
        print("Waiting for audio input")
        run = True

        while run:
            with sr.Microphone(device_index=0) as source:
                print("Working")
                        
                try:
                    r.adjust_for_ambient_noise(source,duration = 0.5) #eliminates any background noises
                    audio_text=r.listen(source)
                    text=r.recognize_google(audio_text)
                    print(json.dumps(data,indent=4))

                    # create json file
                    now = datetime.now()
                    timestamp = datetime.timestamp(now)
                    dt_obj=datetime.fromtimestamp(timestamp)
                    data["notes"].append({
                            str(dt_obj):text
                        })

                    with open("notepad.json","w") as outfile:
                        outfile.write(json.dumps(data,indent=4))

                except KeyboardInterrupt:
                    print("Stopping")
                except Exception as e:
                    print("Error: ", str(e))
                    run=False
                
print("Done")

df = pd.read_json(r'notepad.json')
df.to_csv(r'output.txt', index=False)