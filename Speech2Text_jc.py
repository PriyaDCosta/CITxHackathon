import speech_recognition as sr
import json
from datetime import datetime
import os.path

r = sr.Recognizer()
run=True
data = {}

# data = {"notes": []}
# with open("notepad.json", "w") as outfile:
#     json.dump(data, outfile)

if os.path.exists("notepad.json"):
    print("notepad.json exists")
    with open("notepad.json","r") as f:
        try:
            data = json.load(f)
            print("data:", data)
        except json.decoder.JSONDecodeError as e:
            print("Error loading json file:", str(e))
else:
    data={"notes":[]}

while run:
    with sr.Microphone() as source:
        print("Working")
        audio_text=r.listen(source)
        
        try:
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
