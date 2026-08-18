import sounddevice as s # this is hte mic library for the computer s s make t easier to ttype 
import numpy as np
SAMPLE_RATE = 44100 #this is how many times per sec the mic measyres air preassure. this is a ficxed setting so it cant change mid run 

DURATION = 0.25 #record it for one second 

def record_chunk(): #this goes and gets audio 
    audio = s.rec(int(SAMPLE_RATE * DURATION), samplerate= SAMPLE_RATE, channels = 1) #this starts the recordingm and channles 1 
    s.wait() #the recoridng hapopens in the background. this syas pasue here until its done 
    return audio.flatten() #this allows numpt to return a nster shape and flannets swauched it isnto one plain list of numbers 

if __name__ == "__main__":
    print("Recording... make some noise")
    chunk = record_chunk()
    print("Loudness:", np.abs(chunk).mean())
