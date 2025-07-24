# stt/config.py

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Marathi Vosk Model Path
VOSK_MODEL_PATH = os.path.join(BASE_DIR, "models", "vosk-model-hindi")

# Audio Record Config
SAMPLE_RATE = 16000  # 16kHz for Vosk
RECORD_SECONDS = 5
AUDIO_FILENAME = os.path.join(BASE_DIR, "output.wav")
