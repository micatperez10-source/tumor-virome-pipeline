#!/usr/bin/env nextflow

params.sra_id = "SRR8476839"
params.outdir = "results"

workflow {
    sra_ch = channel.of(params.sra_id)
    
    DOWNLOAD_SRA(sra_ch)
    QC(DOWNLOAD_SRA.out.fastq)
    
    // Nuevo paso: Usar Python para consolidar resultados
    GENERATE_REPORT(sra_ch)
}

process DOWNLOAD_SRA {
    publishDir "${params.outdir}/fastq", mode: 'copy'
    container 'ncbi/sra-tools:3.1.0'
    shell '/bin/sh', '-e'
    input: val sra_id
    output: path "${sra_id}*.fastq", emit: fastq
    script:
    """
    fasterq-dump --split-files $sra_id --maxSpotId 10000
    """
}

process QC {
    publishDir "${params.outdir}/reports", mode: 'copy'
    container 'biocontainers/fastqc:v0.11.9_cv8'
    input: path reads
    output: path "*.html"
    script:
    """
    fastqc ${reads}
    """
}

process GENERATE_REPORT {
    publishDir "${params.outdir}/summary", mode: 'copy'
    // Usamos una imagen de Python pura
    container 'python:3.9-slim'

    input:
    val sra_id

    output:
    path "summary_report.json"

    script:
    """
    python ${baseDir}/bin/report_generator.py ${sra_id} .
    """
}
