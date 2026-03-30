
# Recommandations basées sur règles


def generate_recommendations(data, analysis):
    """
    Génère des recommandations simples
    """

    recos = []

    if analysis["cpu"] == "élevé":
        recos.append("Augmenter les ressources CPU")

    if analysis["latency"] == "élevée":
        recos.append("Optimiser les requêtes ou ajouter du caching")

    if analysis["memory"] == "élevée":
        recos.append("Augmenter la RAM ou nettoyer les processus")

    return recos