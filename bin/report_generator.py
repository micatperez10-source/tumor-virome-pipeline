#!/usr/bin/env python3
import sys, os, json, glob
from datetime import datetime

def main():
    sra_id  = sys.argv[1]
    workdir = sys.argv[2]
    fastq_files = glob.glob(os.path.join(workdir, "*.fastq"))
    fastq_info = [{"filename": os.path.basename(f), "size_mb": round(os.path.getsize(f)/(1024*1024), 2)} for f in fastq_files]
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
    with open("summary_report.json", "w") as f:
        json.dump(report, f, indent=2)
    print("Reporte generado: summary_report.json")

if __name__ == "__main__":
    main()
