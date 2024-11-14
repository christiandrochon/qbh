import sounddevice as sd
import cv2
import time
import entree_micro


# def main():
#     print("Bienvenue dans mon application Python!")
#
# def test():
#     print(test_periphe)

def list_audio_devices():
    print(sd.query_devices())


import cv2
import time
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav


def wake_up_camera():
    cap = cv2.VideoCapture(0)  # 0 est souvent l'index de la première caméra
    if not cap.isOpened():
        print("Impossible d'ouvrir la caméra.")
        return False
    print("Caméra activée pour réveiller le microphone.")
    time.sleep(2)  # Laisser la caméra s'activer pendant 2 secondes
    cap.release()  # Libérer la caméra
    print("Caméra libérée.")
    return True


# def record_audio(duration, sample_rate, device_index):
#     print(f"Enregistrement depuis le périphérique {device_index}...")
#     try:
#         audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32', device=device_index)
#         sd.wait()  # Attendre que l'enregistrement soit terminé
#         print("Enregistrement terminé.")
#         return audio_data
#     except sd.PortAudioError as e:
#         print(f"Erreur d'enregistrement audio : {e}")
#         return None

def test_index_cam():
    # for device_index in [1, 8, 18, 23]:
    for device_index in [1, 10, 24, 30, 31]: #10 ou 31
        print(f"Testing device index {device_index}")
        entree_micro.record_audio(duration=2, sample_rate=44100, device_index=device_index)
        print(f"Tested device index {device_index}")


if __name__ == "__main__":

# main()

    # list_audio_devices()

    test_index_cam()

    entree_micro.record_audio(10, 44100, 1)
# if wake_up_camera():
#     record_audio(duration=5, sample_rate=44100, device_index=1)
# else:
#     print("Échec de l'activation de la caméra.")

# list_audio_devices()
# entree_micro.record_audio(10, 44100, 23)

# if wake_up_camera():
#
#     # print(sd.query_devices())
#
#     # audio_data = record_audio(5, 44100, 23)
#     audio_data = entree_micro.record_audio(5, 44100, 13)
#     if audio_data is not None:
#         wav.write("E:\\workspace_pycharm\\QBH\\sources\\audio_from_webcam.wav", 44100, audio_data)
#         print("Fichier audio enregistré : audio_from_webcam.wav")
#     else:
#         print("Aucun audio capturé.")
# else:
#     print("La caméra n'a pas pu être activée.")
