import numpy as np  # number crunching, and the FFT math
import time  # for the timestamp

# the 12 note names in order, used to convert a number into a letter
NOTE_NAME = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def detect_freq(audio, sample_rate=44100):  # takes audio numbers, returns the dominant Hz
    spectrum = np.abs(np.fft.rfft(audio))  # unmix the sound into all its frequencies, all positive
    freqs = np.fft.rfftfreq(len(audio), 1 / sample_rate)  # the Hz label for each slot
    peak_index = np.argmax(spectrum)  # which slot is loudest (a position, not a value)
    return freqs[peak_index]  # look up that slot's Hz

def freq_to_note(freq):  # takes a Hz number, returns a letter like "C"
    semitones_from_a4 = 12 * np.log2(freq / 440.0)  # how many semitones away from A4 (440 Hz)
    note_index = round(semitones_from_a4) + 9  # snap to nearest note; +9 shifts A to its spot in a C-first list
    return NOTE_NAME[note_index % 12]  # wrap any octave back into the 12 names


def get_sound_verdict():  # records and returns a full verdict dict
    from src.sound.capture import record_chunk  # your mic function
    audio = record_chunk()  # one second of sound
    spectrum = np.abs(np.fft.rfft(audio))  # unmix it
    freqs = np.fft.rfftfreq(len(audio), 1 / 44100)  # Hz labels
    peak_index = np.argmax(spectrum)  # loudest slot

    masked = spectrum.copy()  # duplicate, so edits don't damage the original
    masked[max(0, peak_index - 5):peak_index + 5] = 0  # zero out the peak and its neighbors
    runner_up = masked.max()  # tallest thing left = true second place
    confidence = 1 - (runner_up / spectrum[peak_index])  # how much the winner beat it, on a 0-1 scale

    return {
        "sound_pick_up": freq_to_note(freqs[peak_index]),  # the note name
        "confidence": float(confidence),  # how trustworthy
        "timestamp": time.time(),  # when it happened
        "volume": float(np.abs(audio).mean()),  # how loud
    }


if __name__ == "__main__":  # only runs when you launch this file directly
    from src.sound.capture import record_chunk
    print("Play or hum a note...")
    audio = record_chunk()
    freq = detect_freq(audio)
    print("Frequency:", freq)
    print("Note:", freq_to_note(freq))
    print(get_sound_verdict())  # the full dict