import librosa
import numpy as np


def preprocess_audio(file_path):
    """
    Prétraite un fichier audio en supprimant le bruit de fond.
    :param file_path:  Chemin du fichier audio.
    :return:  Tuple (y, sr) où y est le signal audio et sr est le taux d'échantillonnage.
    """
    # Charge le fichier audio
    y, sr = librosa.load(file_path, sr=22050)
    # Supprime le bruit de fond (optionnel)
    y = librosa.effects.trim(y, top_db=20)[0]
    return y, sr


def extract_pitch(y, sr):
    """
    Extrait les hauteurs de notes d'un signal audio.
    :param y:  Signal audio.
    :param sr:  Taux d'échantillonnage.
    :return:  Liste de hauteurs de notes.
    """
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr, fmin=50.0, fmax=500.0)
    pitch_sequence = []
    for t in range(pitches.shape[1]):
        index = np.argmax(magnitudes[:, t])
        pitch = pitches[index, t]
        if pitch > 0:  # Filtre les valeurs nulles
            pitch_sequence.append(pitch)
    print("### Debugging: Pitch Sequence ###")
    print(f"Type: {type(pitch_sequence)}")
    print(f"Length: {len(pitch_sequence)}")
    print(f"First 10 pitches: {pitch_sequence[:10]}")
    return pitch_sequence


def compute_intervals(pitch_sequence):
    """
    Calcule les intervalles entre les hauteurs des notes dans une séquence de hauteurs de notes.
    :param pitch_sequence: Séquence de hauteurs de notes.
    :return: Liste d'intervalles entre les hauteurs de notes consécutives.
    """
    intervals = []
    for i in range(1, len(pitch_sequence)):
        interval = pitch_sequence[i] - pitch_sequence[i - 1]
        intervals.append(interval)
    print("### Debugging: Computed Intervals ###")
    print(f"Type: {type(intervals)}")
    print(f"Length: {len(intervals)}")
    print(f"First 10 intervals: {intervals[:10]}")
    return intervals
