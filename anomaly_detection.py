
# Détection anomalies globales

def detect_anomalies(data_list):
    """
    Détecte les anomalies sur toute la période
    """

    anomalies = []

    for data in data_list:

        if data.cpu_usage > 90:
            anomalies.append({
                "timestamp": data.timestamp,
                "status": f"ALERTE : CPU à {data.cpu_usage}%"
            })

        if data.service_status.get("api_gateway") != "online":
            anomalies.append({
                "timestamp": data.timestamp,
                "status": "CRITIQUE : api_gateway dégradé"
            })

        if data.service_status.get("database") == "offline":
            anomalies.append({
                "timestamp": data.timestamp,
                "status": "CRITIQUE : database offline"
            })

    return anomalies