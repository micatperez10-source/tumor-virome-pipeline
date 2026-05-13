#!/usr/bin/env python3
"""
report_generator.py
Genera un resumen JSON del pipeline tumor-virome.
Uso: python report_generator.py <sra_id> <workdir>
"""

import sys
import os
import json
import glob
from datetime import datetime


def generate_report(sra_id: str, workdir: str) -> dict:
    """Recopila métricas del directorio de trabajo y arma el reporte."""

    # Buscar archivos FASTQ generados
    fastq_files = glob.glob(os.path.join(workdir, "*.fastq"))
    fastq_info = []
    for f in fastq_files:
        size_mb = os.path.getsize(f) / (1024 * 1024)
        fastq_info.append({
            "filename": os.path.basename(f),
            "size_mb": round(size_mb, 2)
        })

    # Buscar reportes HTML de FastQC
    html_reports = glob.glob(os.path.join(workdir, "*.html"))

    report = {
        "pipeline": "tumor-virome-pipeline",
        "sra_id": sra_id,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "status": "completed",
        "fastq_files": fastq_info,
        "fastq_count": len(fastq_files),
        "qc_reports": [os.path.basename(h) for h in html_reports],
        "summary": {
            "total_fastq_size_mb": round(sum(f["size_mb"] for f in fastq_info), 2),
            "qc_passed": len(html_reports) > 0
        }
    }
    return report


def main():
    if len(sys.argv) < 3:
        print("Uso: python report_generator.py <sra_id> <workdir>", file=sys.stderr)
        sys.exit(1)

    sra_id  = sys.argv[1]
    workdir = sys.argv[2]

    report = generate_report(sra_id, workdir)

    output_path = "summary_report.json"
    with open(output_path, "w") as f:
        json.dump(report, f, indent=2)

    print(f"✅ Reporte generado: {output_path}")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
