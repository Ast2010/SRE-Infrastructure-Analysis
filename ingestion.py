
# Chargement des données JSON

import json

class DataPoint:
    """
    Représente une entrée de métriques (objet structuré)
    """

    def __init__(self, raw):
        self.timestamp = raw.get("timestamp")
        self.cpu_usage = raw.get("cpu_usage")
        self.memory_usage = raw.get("memory_usage")
        self.latency_ms = raw.get("latency_ms")
        self.disk_usage = raw.get("disk_usage")
        self.network_in_kbps = raw.get("network_in_kbps")
        self.network_out_kbps = raw.get("network_out_kbps")
        self.io_wait = raw.get("io_wait")
        self.thread_count = raw.get("thread_count")
        self.active_connections = raw.get("active_connections")
        self.error_rate = raw.get("error_rate")
        self.uptime_seconds = raw.get("uptime_seconds")
        self.temperature_celsius = raw.get("temperature_celsius")
        self.power_consumption_watts = raw.get("power_consumption_watts")
        self.disk_usage = raw.get("disk_usage")
        self.service_status = raw.get("service_status", {})


def load_data(path):
    """
    Charge un fichier JSON contenant une liste de métriques
    """

    with open(path, "r") as f:
        raw_data = json.load(f)

    # Si c'est un seul objet → le transformer en liste
    if isinstance(raw_data, dict):
        raw_data = [raw_data]

    return [DataPoint(item) for item in raw_data]