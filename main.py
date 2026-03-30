from ingestion import load_data
from analysis import analyze_metrics
from anomaly_detection import detect_anomalies
from recommendation import generate_recommendations
from llm_recommender import generate_llm_recommendation
import json



def export_json_report(data_list, analyses, recommendations, llm_recos, anomalies):
   rapport = []


   for i, data in enumerate(data_list):
       bloc = {
           "timestamp": data.timestamp,
           "analyse": analyses[i],
           "recommandations_logiques": recommendations[i],
           "recommandation_llm": llm_recos[i]
       }
       rapport.append(bloc)


   full_report = {
       "resultats": rapport,
       "anomalies_globales": anomalies
   }


   with open("output.json", "w") as f:
       json.dump(full_report, f, indent=2, ensure_ascii=False)


   print("\n Le rapport final est exporté dans *output.json*")




def main():
   data_list = load_data("rapport.json")


   all_analyses = []
   all_recos = []
   all_llm_recos = []


   print("=== Analyse des métriques ===")
   for data in data_list:
       summary = analyze_metrics(data)
       all_analyses.append(summary)


       print(f"Timestamp: {data.timestamp}")
       for key, value in summary.items():
           print(f"  {key}: {value}")


       recommandations = generate_recommendations(data, summary)
       all_recos.append(recommandations)


       if recommandations:
           print("  Recommandations :")
           for reco in recommandations:
               print(f"   - {reco}")


       llm_reco = generate_llm_recommendation(data, summary)
       all_llm_recos.append(llm_reco)


       print(" Recommandation LLM :")
       print(f"   {llm_reco}")
       print("-" * 40)


   print("\n*Détection d’anomalies globale*")
   anomalies = detect_anomalies(data_list)
   for entry in anomalies:
       print(f"{entry['timestamp']}: {entry['status']}")


   export_json_report(data_list, all_analyses, all_recos, all_llm_recos, anomalies)




if __name__ == "__main__":
   main()



