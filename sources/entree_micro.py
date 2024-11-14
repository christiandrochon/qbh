# sources/entree_micro.py
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

# Recording parameters
DURATION = 10  # Duration in seconds
SAMPLE_RATE = 44100  # Sample rate in Hz
DEVICE_INDEX = 1  # Replace with the correct device index

def record_audio(duration, sample_rate, device_index):
    print(f"Enregistrement depuis le périphérique {device_index}...")
    try:
        with sd.InputStream(samplerate=sample_rate, channels=1, device=device_index, dtype='float32') as stream:
            audio_data, overflowed = stream.read(int(duration * sample_rate))
            print("Enregistrement terminé.")
            return audio_data
    except sd.PortAudioError as e:
        print(f"Erreur d'enregistrement audio : {e}")
        return None
# def record_audio(duration, sample_rate, device_index):
#     print(f"Enregistrement depuis le périphérique {device_index}...")
#     try:
#         # Enregistrement en stéréo pour plus de compatibilité
#         audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='float32', device=device_index)
#         sd.wait()  # Attendre que l'enregistrement soit terminé
#         print("Enregistrement terminé.")
#
#         # Vérification des données enregistrées
#         if np.all(audio_data == 0):
#             print("Aucun son capturé (données nulles).")
#         else:
#             print("Données audio capturées (non nulles).")
#
#         # Application d'un gain pour amplifier si le son est faible
#         audio_data = audio_data * 10  # Facteur d'amplification ajustable
#
#         return audio_data
#     except sd.PortAudioError as e:
#         print(f"Erreur d'enregistrement audio : {e}")
#         return None

# Record audio
audio_data = record_audio(DURATION, SAMPLE_RATE, DEVICE_INDEX)

# Save to a WAV file
if audio_data is not None:
    print(f"Audio data shape: {audio_data.shape}")
    wav.write("E:/workspace_pycharm/QBH/sources/audio_from_webcam.wav", SAMPLE_RATE, (audio_data * 32767).astype(np.int16))
    print("Audio file saved: audio_from_webcam.wav")