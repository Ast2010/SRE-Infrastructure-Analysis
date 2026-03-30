
# ============================================
# Je fais la recommandation via LLM (Groq API)
# ============================================

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv("key.env")
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY non définie dans key.env")

client = Groq(api_key=api_key)

def generate_llm_recommendation(data, analysis):
    """
    Génère une expertise SRE basée sur l'intégralité des métriques d'infrastructure.
    """
    
    # Construction d'un contexte technique ultra-complet
    prompt = f"""
Tu es Astrel, Expert SRE Senior. Analyse ces métriques pour le CTO Jean.
RETOURNE UNIQUEMENT DES RECOMMANDATIONS TECHNIQUES. PAS DE SALUTATIONS. PAS DE SIGNATURE.

CONTEXTE TECHNIQUE COMPLET :
- Horodatage : {data.timestamp}
- Charge Système : CPU {data.cpu_usage}%, RAM {data.memory_usage}%, Threads: {data.thread_count}
- Performance : Latence {data.latency_ms}ms, Taux d'erreur: {data.error_rate}
- Stockage : Disk Usage {data.disk_usage}%, IO Wait: {data.io_wait}
- Réseau : In {data.network_in_kbps} kbps, Out {data.network_out_kbps} kbps, Connexions actives: {data.active_connections}
- Santé Hardware : Température {data.temperature_celsius}°C, Consommation: {data.power_consumption_watts}W
- Uptime : {data.uptime_seconds}s
- État des Services : {data.service_status}

ANALYSE LOGIQUE PRÉALABLE : {analysis}

MISSION : Identifie la cause racine (Root Cause) la plus probable et donne une action prioritaire immédiate, il faut proposer des
actions concrètes pour optimiser la performance de l infrastructure .
"""
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant", # c'est un modele gratuit qui a des limites
            messages=[
                {"role": "system", "content": "Tu es un ingénieur SRE pragmatique. Tu parles en termes d'infrastructure, de scalabilité et de résolution d'incidents. Sois très concis."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1 # On baisse la température pour plus de précision technique
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Erreur API : {str(e)}"