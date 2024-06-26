import sounddevice as sd
import soundfile as sf
from tkinter import *

def record_audio(filename, duration):
    fs = 44100  # Sampling frequency
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()
    sf.write(filename, recording, fs)

def voice_rec():
    fs = 48000
    duration = 5
    record_audio("recording.wav", duration)

master = Tk()

Label(master, text="Voice Recorder:").grid(row=0, sticky=W, rowspan=5)

b = Button(master, text="Start", command=voice_rec)
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

mainloop()