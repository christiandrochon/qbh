from sources.dtw import match_query
from sources.process_entree_audio import (
    preprocess_audio,
    extract_pitch,
    compute_intervals,
)


def query_by_humming(file_path, database):
    """
    Recherche une chanson dans une base de données en fonction d'un extrait audio.
    :param file_path:  Chemin du fichier audio.
    :param database:  Base de données d'intervalles.
    :return: Liste de correspondances (chanson, distance) triée par distance croissante.
    """
    # Étape 1 : Prétraitement
    y, sr = preprocess_audio(file_path)

    # Étape 2 : Extraction de pitch
    pitch_sequence = extract_pitch(y, sr)

    # Étape 3 : Calcul des intervalles
    query_intervals = compute_intervals(pitch_sequence)

    # Étape 4 : Correspondance
    matches = match_query(query_intervals, database)

    return matches
