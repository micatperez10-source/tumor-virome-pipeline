#!/usr/bin/env nextflow

params.sra_id = "SRR8476839"
params.outdir = "results"
params.fastq_dir = "${projectDir}/results/fastq"

workflow {
    // Leer los fastq directamente, sin descargar
    fastq_ch = channel.fromPath("${params.fastq_dir}/${params.sra_id}*.fastq")
                      .collect()

    QC(fastq_ch)
    GENERATE_REPORT(channel.of(params.sra_id), QC.out.collect())
}

process QC {
    publishDir "${params.outdir}/reports", mode: 'copy'
    container 'quay.io/biocontainers/fastqc:v0.11.9_cv8'

    input:
    path reads

    output:
    path "*.html"

    script:
    """
    fastqc ${reads}
    """
}

process GENERATE_REPORT {
    publishDir "${params.outdir}/summary", mode: 'copy'
    container 'python:3.9-slim'

    input:
    val sra_id
    path qc_reports

    output:
    path "summary_report.json"

    script:
    """
    cp ${projectDir}/bin/report_generator.py .
    python report_generator.py ${sra_id} .
    """
}
