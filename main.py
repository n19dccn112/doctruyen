# bị chậm
# from gtts import gTTS
# import os
# from playsound import playsound
#
# myText = "hi"
# language = 'vi'
# output = gTTS(text=myText, tld='com.vn', lang=language)
# output.save("output.mp3")
# playsound("output.mp3")
# os.system("start output.mp3")

# text to mp3

# import pyttsx3
#
# output = pyttsx3.init()
# voices = output.getProperty("voices")
# output.setProperty("voice", voices[1].id)
# output.say("xin chào")
# output.runAndWait()

# mp3 to mp4

import os
import shutil
import sys
from pathlib import Path
import subprocess
import ffmpeg
from asyncio.subprocess import PIPE
dir_path = os.path.dirname(os.path.realpath(__file__))

def CheckFile():
    try:
        files = []
        for path in os.listdir(sys.argv[1]):
            full_path = os.path.join(sys.argv[1], path)
            if os.path.isfile(full_path):
                files.append(full_path)
        mp3 = [x for x in files if x.endswith(".mp3")]
        if len(mp3) >= 1:
            return mp3, sys.argv[2], sys.argv[1]
        else:
            print(
                "Make Sure That You've at least 1 Mp3 file")
            exit()
    except FileNotFoundError:
        print("Sorry, This File Is Not Exist!")
        exit()


def Convert():
    mp3, jpg, name = CheckFile()
    name = f"{Path(name).name}-converted"
    shutil.rmtree(name, ignore_errors=True)
    os.mkdir(name)
    os.chdir(name)
    subprocess.run('conda activate DOCTRUYEN', shell=True, universal_newlines=True, check=True, stdout=PIPE)
    subprocess.run(
        'ffmpeg -loop 1 -framerate 1 -i image.png -i audio.mp3 -map 0:v -map 1:a -r 10 -vf '
        '"scale=\'iw-mod(iw,2)\':\'ih-mod(ih,2)\',format=yuv420p" -movflags +faststart -shortest -fflags +shortest'
        ' -max_interleave_delta 100M output.mp4', shell=True, universal_newlines=True, check=True, stdout=PIPE)


# Convert()
subprocess.run(
    ["conda activate DOCTRUYEN && conda run \'ffmpeg -loop 1 -framerate 1 -i "+dir_path+"\\image.png -i "+dir_path+"\\output.mp3 -map 0:v -map 1:a -r 10 -vf scale=\'iw-mod(iw,2)\':\'ih-mod(ih,2)\',format=yuv420p -movflags +faststart -shortest -fflags +shortest -max_interleave_delta 100M "+dir_path+"\\output.mp4\'"], shell=True, universal_newlines=True, check=True, stdout=PIPE)
