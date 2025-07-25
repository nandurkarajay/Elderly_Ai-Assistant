# stt/recognize_vosk.py

import os
import wave
import json
from vosk import Model, KaldiRecognizer
from .config import VOSK_MODEL_PATH, AUDIO_FILENAME
print("✅ recognize_vosk.py loaded")
def recognize_from_file(audio_path=AUDIO_FILENAME):
    if not os.path.exists(VOSK_MODEL_PATH):
        raise FileNotFoundError(f"Vosk Marathi मॉडेल सापडले नाही: {VOSK_MODEL_PATH}")

    wf = wave.open(audio_path, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() != 16000:
        raise ValueError("ऑडियो फाईल mono (16-bit 16kHz) असावी लागते.")

    model = Model(VOSK_MODEL_PATH)
    rec = KaldiRecognizer(model, wf.getframerate())

    result_text = ""
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            result_text += res.get("text", "") + " "

    final_res = json.loads(rec.FinalResult())
    result_text += final_res.get("text", "")

    return result_text.strip()
