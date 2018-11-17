##import datetime
##import os
##stop = False
##while stop == False:
##    rn = str(datetime.datetime.now().time())
##    print(rn)
##    if rn > "15:52:00.286971":
##        stop = True
##        os.system("start Nintendo.mp3")
##
##

import subprocess

##def get_master_volume():
##    proc = subprocess.Popen('/usr/bin/amixer sget Master', shell=True, stdout=subprocess.PIPE)
##    print(proc.communicate()[0].split('\n')[4])
##    print(type(proc.communicate()[0].split('\n')[4]))
##    amixer_stdout = proc.communicate()[0].split('\n')[4]
##    proc.wait()
##
##    find_start = amixer_stdout.find('[') + 1
##    find_end = amixer_stdout.find('%]', find_start)
##
##    return float(amixer_stdout[find_start:find_end])
##
##def set_master_volume(volume):
##    val = float(int(volume))
##
##    proc = subprocess.Popen('/usr/bin/amixer sset Master ' + str(val) + '%', shell=True, stdout=subprocess.PIPE)
##    proc.wait()

##get_master_volume()

##from pydub import AudioSegment
##from pydub.playback import play

from playsound import playsound
##playsound('Nintendo.mp3')


##song = AudioSegment.from_mp3("Nintendo.mp3")
##
### boost volume by 6dB
##louder_song = song + 6
##
### reduce volume by 3dB
##quieter_song = song - 3
##
###Play song
##play(louder_song)
##
###save louder song 
##louder_song.export("louder_song.mp3", format='mp3')


##import osascript
##
##osascript.osascript("set volume output volume 100")


##from ctypes import cast, POINTER
##from comtypes import CLSCTX_ALL
##from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
## 
##devices = AudioUtilities.GetSpeakers()
##interface = devices.Activate(
##   IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
##volume = cast(interface, POINTER(IAudioEndpointVolume))
## 
### Control volume
###volume.SetMasterVolumeLevel(-0.0, None) #max
###volume.SetMasterVolumeLevel(-5.0, None) #72%
##volume.SetMasterVolumeLevel(-30.0, None) #51%
##playsound('bell.mp3')
##volume.SetMasterVolumeLevel(-5.0, None) #51%
##playsound('bell.mp3')
##volume.SetMasterVolumeLevel(-30.0, None) #51%

def play():
    from playsound import playsound
    playsound('bell.mp3')

def set_volume(vol):
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
     
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
       IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    volume.SetMasterVolumeLevel(vol, None) #51%




