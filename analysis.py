# Analyse des métriques demandées

def analyze_metrics(data):
    
    #Analyse simple des métriques techniques


    result = {}

    # CPU
    if data.cpu_usage > 80:
        result["cpu"] = "élevé"
    else:
        result["cpu"] = "normal"

    # Mémoire
    if data.memory_usage > 75:
        result["memory"] = "élevée"
    else:
        result["memory"] = "normale"

    # Latence
    if data.latency_ms > 200:
        result["latency"] = "élevée"
    else:
        result["latency"] = "normale"

    # Erreurs
    if data.error_rate > 0.01:
        result["error_rate"] = "critique"
    else:
        result["error_rate"] = "ok"

    return result