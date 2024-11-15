import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import euclidean


def normalize_intervals(intervals):
    intervals = np.array(intervals)
    min_val = np.min(intervals)
    max_val = np.max(intervals)
    if max_val - min_val == 0:  # Cas où tous les éléments sont identiques
        return intervals * 0
    return (intervals - min_val) / (max_val - min_val)


def smooth_intervals(intervals, window_size=5):
    return np.convolve(intervals, np.ones(window_size) / window_size, mode="valid")


def adjust_length(query_intervals, intervals):
    target_length = min(len(query_intervals), len(intervals))
    return query_intervals[:target_length], intervals[:target_length]


def match_query(query_intervals, database):
    """
    Compare les intervalles d'une requête à ceux de la base de données.
    :param query_intervals:  Liste d'intervalles de la requête.
    :param database:  Base de données d'intervalles.
    :return: Liste de tuples (chanson, distance) triée par distance croissante.
    """
    results = {}
    query_intervals = smooth_intervals(normalize_intervals(query_intervals))
    print(f"Smoothed and normalized query intervals: {query_intervals[:10]}")

    for song, intervals in database.items():
        intervals = smooth_intervals(normalize_intervals(intervals))

        # Ajuster les longueurs
        query_intervals, intervals = adjust_length(query_intervals, intervals)

        print(f"Adjusted Query Intervals: {query_intervals[:10]}")
        print(f"Adjusted Database Intervals for {song}: {intervals[:10]}")

        # Calculer la distance
        distance = euclidean(query_intervals, intervals)
        results[song] = distance

    # Trier les résultats
    sorted_results = sorted(results.items(), key=lambda x: x[1])

    # Visualisation
    print("Visualisation des intervalles...")
    plt.figure(figsize=(10, 6))
    plt.plot(query_intervals[:50], label="Query Intervals", linewidth=2)
    for song, intervals in database.items():
        plt.plot(
            smooth_intervals(normalize_intervals(intervals))[:50],
            label=f"{song} Intervals",
            alpha=0.7,
        )
    plt.legend()
    plt.title("Comparaison des intervalles - Query vs Database")
    plt.xlabel("Index")
    plt.ylabel("Valeur normalisée")

    plt.savefig(
        r"E:\workspace_pycharm\QBH\sources\matplot\query_vs_database_intervals.png"
    )
    plt.show()

    return sorted_results
