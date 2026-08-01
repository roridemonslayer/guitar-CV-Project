import numpy as np 

def detect_freq(audio, sample_rate = 44100): #this is the default value 
    spectrum = np.abs(np.fft.rfft(audio)) # rfft does all of the unmixing audio over a set tumne = unmixing. this js makes all the outputs positive. this outputs where each slot ois how present the requency wa s
    freqs = np.fft.rfftfreq(len(audio), 1/sample_rate) #this builds the list of labels with the hz so the list comes back as liek 0 hz, 1hz, 2hz in a list
    peak_index = np.argmax(spectrum) #this returns which slot holds the biggest value. so if slot is 220 then the asnwer is 220 
    return freqs[peak_index]


if __name__ == "__main__":
    from src.sound.capture import record_chunk
    print("Play or hum a note...")
    audio = record_chunk()
    print("Frequency:", detect_freq(audio))

