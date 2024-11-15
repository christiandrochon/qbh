import numpy as np
import scipy.io.wavfile as wav
import sounddevice as sd

from sources import entree_micro
from sources.dtw import match_query
from sources.entree_micro import remove_silence
from sources.process_entree_audio import preprocess_audio, extract_pitch


#
# def wake_up_camera():
#     cap = cv2.VideoCapture(0)  # 0 est souvent l'index de la première caméra
#     if not cap.isOpened():
#         print("Impossible d'ouvrir la caméra.")
#         return False
#     print("Caméra activée pour réveiller le microphone.")
#     time.sleep(2)  # Laisser la caméra s'activer pendant 2 secondes
#     cap.release()  # Libérer la caméra
#     print("Caméra libérée.")
#     return True


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


def list_audio_devices():
    print(sd.query_devices())


# def test_index_cam():
#     # for device_index in [1, 8, 18, 23]:
#     for device_index in [1, 10, 24, 30, 31]: #10 ou 31
#         print(f"Testing device index {device_index}")
#         entree_micro.record_audio(duration=2, sample_rate=44100, device_index=device_index)
#         print(f"Tested device index {device_index}")


def test_index_mic():
    # Étape 1 : Enregistrement audio
    print("Étape 1 : Enregistrement de l'audio...")
    DURATION = 10  # Enregistrement de 10 secondes
    SAMPLE_RATE = 44100  # Taux d'échantillonnage
    DEVICE_INDEX = 1  # Modifier en fonction de votre configuration

    database = {
        "ascending": np.linspace(0, 1, 426),  # Longueur similaire à query_intervals
        "descending": np.linspace(1, 0, 426),
        "random": np.random.uniform(0, 1, size=426),
    }

    # test_index_cam()
    # audio_data = entree_micro.record_audio(10, 44100, 1)
    audio_data = entree_micro.record_audio(DURATION, SAMPLE_RATE, DEVICE_INDEX)

    # Vérification si l'audio a été capturé
    if audio_data is None:
        print("Aucun audio n'a été capturé. Terminaison.")
        return

    # audio_file = "E:\\workspace_pycharm\\QBH\sources\\audio_from_webcam.wav"
    audio_file = r"E:\workspace_pycharm\QBH\sources\audio\audio_from_mic.wav"
    wav.write(audio_file, SAMPLE_RATE, (audio_data * 32767).astype(np.int16))
    print(f"Fichier audio enregistré : {audio_file}")

    # Étape 2 : Prétraitement de l'audio
    print("Étape 2 : Prétraitement de l'audio...")
    y, sr = preprocess_audio(audio_file)
    y = remove_silence(y, sr)

    print("### Debugging: Audio Signal ###")
    print(f"Type: {type(y)}")
    print(f"Shape: {y.shape}")
    print(f"First 10 samples: {y[:10]}")

    # Étape 3 : Extraction des caractéristiques (pitch et intervalles)
    print("Étape 3 : Extraction des caractéristiques...")
    pitch_sequence = extract_pitch(y, sr)
    print("### Debugging: Pitch Sequence ###", pitch_sequence[:10])

    # query_intervals = compute_intervals(pitch_sequence)
    query_intervals = np.random.uniform(-10, 10, size=430)
    print("### Debugging: Query Intervals ###")
    print(f"Type: {type(query_intervals)}")
    print(f"Shape: {np.array(query_intervals).shape}")
    print(f"First 10 elements: {query_intervals[:10]}")

    # Étape 4 : Recherche dans la base de données
    print("Étape 4 : Recherche dans la base de données...")
    results = match_query(query_intervals, database)
    print("Résultats de la similarité :", results)

    # Étape 5 : Affichage des résultats
    print("Résultats :")

    closest_song, closest_distance = results[0]
    print(
        f"La chanson la plus proche est : {closest_song} avec une distance de {closest_distance}"
    )
    # for song, distance in results:
    #     print(f"Chanson : {song}, Distance : {distance}")


if __name__ == "__main__":
    test_index_mic()
