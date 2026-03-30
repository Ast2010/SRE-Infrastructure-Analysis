***Infrastructure Monitoring & AI Analysis (SRE Tool)***

Realisé par Astrel Télémaque

Test Technique : Analyseur d'Infrastructure Intelligent

***Présentation du Projet***
Ce projet est une solution complète d'ingestion et d'analyse de métriques d'infrastructure. Il combine une analyse déterministe (basée sur des seuils de performance) et une analyse cognitive (via LLM) pour fournir des recommandations stratégiques exploitables par un CTO.

***Architecture Modulaire du projet***

1. Le code a été découpé en services distincts pour garantir une maintenance aisée et une scalabilité du pipeline :

2. ingestion.py : Moteur de parsing robuste. Il ne se contente pas de lire le JSON, il mappe l'intégralité des 15+ métriques (CPU, IO Wait, Température, Network, etc.) dans des objets Python typés.

3. analysis.py : Moteur de règles métier. Identifie les dépassements de seuils critiques de manière fiable et constante.

4. llm_recommender.py : Intelligence Artificielle exploitant l'API Groq (Llama 3.1 8B). Le prompt a été optimisé pour un profil SRE (Astrel) afin de fournir des "Root Cause Analysis" sans fioritures (pas de salutations, focus technique pur).

5. anomaly_detection.py & recommendation.py : Logiques de détection globale et de remédiation automatique (Auto-healing).

6. main.py : Chef d'orchestre pilotant le flux de données de l'ingestion jusqu'à l'export final.

***Choix Techniques Stratégiques***

1. Optimisation du LLM (Efficiency over Size)
J'ai sélectionné le modèle llama-3.1-8b-instant via Groq pour trois raisons :

Vitesse : Inférence ultra-rapide (LPU).

Fiabilité : Meilleure gestion des quotas (Rate Limits) par rapport au modèle 70B.

Précision : Configuration à temperature=0.1 pour garantir des réponses techniques déterministes et éviter les hallucinations créatives.

2. Traitement Exhaustif des Données
Contrairement à une analyse basique, ce programme traite l'intégralité des métriques SRE :

Hardware : Surveillance de la température et de la consommation électrique.

Système : Analyse fine des IO Wait et du Thread Count.

Services : Monitoring de l'état spécifique (service_status) de la base de données, du cache et de la gateway.

3. Sortie de Données (Observabilité)
Terminal : Feedback visuel en temps réel pour le suivi de l'exécution.

output.json : Génération d'un rapport structuré persistant, prêt à être consommé par un dashboard ou un outil de ticketing (Jira/ServiceNow).

***Installation & Usage***
1. Environnement :

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

2. Configuration : Créer un fichier key.env à la racine :

GROQ_API_KEY= la cle que j'ai cree sur Grog

3. Exécution :
python3 main.py

***Format de Sortie (le fameu output.json)***
Le fichier généré regroupe l'analyse technique brute et l'expertise IA pour chaque point de mesure, permettant une prise de décision rapide.