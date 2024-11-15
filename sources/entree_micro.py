# sources/entree_micro.py
import librosa
import numpy as np
import sounddevice as sd

# Recording parameters
DURATION = 10  # Duration in seconds
SAMPLE_RATE = 44100  # Sample rate in Hz
DEVICE_INDEX = 1  # Replace with the correct device index


def remove_silence(y, sr, threshold=0.02):
    """
    Supprime les silences d'un signal audio.
    :param y:  Signal audio.
    :param sr:  Taux d'échantillonnage.
    :param threshold:  Seuil de silence.
    :return:  Signal audio sans les silences.
    """
    intervals = librosa.effects.split(y, top_db=-20 * np.log10(threshold))
    trimmed_audio = np.concatenate([y[start:end] for start, end in intervals])
    return trimmed_audio


def record_audio(duration, sample_rate, device_index):
    """
    Enregistre un signal audio à partir d'un périphérique audio.
    :param duration:  Durée de l'enregistrement en secondes.
    :param sample_rate:  Taux d'échantillonnage.
    :param device_index:  Index du périphérique audio.
    :return:  Signal audio enregistré.
    """
    # print(f"Enregistrement depuis le périphérique {device_index}...")
    print("Commencez à parler dès maintenant pour éviter le silence.")

    try:
        with sd.InputStream(
            samplerate=sample_rate, channels=1, device=device_index, dtype="float32"
        ) as stream:
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
# audio_data = record_audio(DURATION, SAMPLE_RATE, DEVICE_INDEX)

# Save to a WAV file
# if audio_data is not None:
#     print(f"Audio data shape: {audio_data.shape}")
#     wav.write("E:/workspace_pycharm/QBH/sources/audio_from_webcam.wav", SAMPLE_RATE, (audio_data * 32767).astype(np.int16))
#     print("Audio file saved: audio_from_webcam.wav")
