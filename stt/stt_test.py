# test_stt.py (प्रोजेक्टच्या रूटमध्ये)
from stt.record_audio import record_audio
from stt.recognize_vosk import recognize_from_file


if __name__ == "__main__":
    wav_file = record_audio()
    text = recognize_from_file(wav_file)
    print("📝 ओळखलेले वाक्य:", text)
