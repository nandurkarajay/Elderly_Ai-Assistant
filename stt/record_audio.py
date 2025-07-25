# stt/record_audio.py

import sounddevice as sd
import wave
from .config import SAMPLE_RATE, RECORD_SECONDS, AUDIO_FILENAME

def record_audio():
    print("🎤 बोलायला सुरुवात करा... (Recording)")
    audio = sd.rec(int(RECORD_SECONDS * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
    sd.wait()
    print("✅ रेकॉर्डिंग पूर्ण!")

    with wave.open(AUDIO_FILENAME, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 16-bit audio = 2 bytes
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(audio.tobytes())

    return AUDIO_FILENAME
