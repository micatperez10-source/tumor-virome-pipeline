import json
import os
import sys

def generate_summary(sra_id, output_dir):
    print(f"--- Analizando resultados para {sra_id} ---")
    
    # Simulamos la extracción de métricas que vendrían de FastQC
    report_data = {
        "sample_id": sra_id,
        "status": "Success",
        "reads_processed": 10000,
        "quality_score_average": 35.8,
        "path": os.path.abspath(output_dir)
    }
    
    with open(f"{output_dir}/summary_report.json", "w") as f:
        json.dump(report_data, f, indent=4)
    
    print(f"✅ Reporte JSON generado en: {output_dir}/summary_report.json")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python report_generator.py <SRA_ID> <OUTDIR>")
    else:
        generate_summary(sys.argv[1], sys.argv[2])
