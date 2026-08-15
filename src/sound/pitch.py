import numpy as np
import time  #this is needed for the timestamp

def detect_freq(audio, sample_rate = 44100): #this is the default value 
    spectrum = np.abs(np.fft.rfft(audio)) # rfft does all of the unmixing audio over a set tumne = unmixing. this js makes all the outputs positive. this outputs where each slot ois how present the requency wa s
    freqs = np.fft.rfftfreq(len(audio), 1/sample_rate) #this builds the list of labels with the hz so the list comes back as liek 0 hz, 1hz, 2hz in a list
    peak_index = np.argmax(spectrum) #this returns which slot holds the biggest value. so if slot is 220 then the asnwer is 220 
    return freqs[peak_index]

NOTE_NAME = ["C", "C#", "D","D#","E","F","F#","G","G#","A","A#","B"]


def freq_to_note(freq):
    semitones_from_a4 = 12 *np.log2(freq/440.0)
    note_index = round(semitones_from_a4) + 9 
    return NOTE_NAME[note_index % 12]

def get_sound_verdict():
    from src.sound.capture import record_chunk #pulls the recording function
    audio = record_chunk() #one sec of mic data, 44,100 numbers 
    spectrum = np.abs(np.fft.rfft(audio)) # this pulls the 
    freqs = np.fft.rfftfreq(len(audio), 1/44100)# the hz score same as the last one 
    peak_index = np.argmax(spectrum) #which slot is the loudest 
    masked = spectrum.copy()
    masked[max(0, peak_index-5):peak_index+5] = 0
    runner_up = masked.max()
    confidence = 1 -(runner_up/spectrum[peak_index])
    return {
        "sound_pick_up":freq_to_note(freqs[peak_index]),
        "confidence":float(spectrum[peak_index] / spectrum.sum()),
        "timestamp":time.time(),
        "volume": float(np.abs(audio).mean()), 
    }

    
     









#this whole line js take sa nfumer liek 330 and turn it to note. "C"
if __name__ == "__main__":
    from src.sound.capture import record_chunk
    print("Play or hum a note...")
    audio = record_chunk()
    freq = detect_freq(audio)
    print("Frequency:", freq)
    print("Note:", freq_to_note(freq))
    print(get_sound_verdict())