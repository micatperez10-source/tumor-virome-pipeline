#!/usr/bin/env nextflow

params.sra_id = "SRR8476839"
params.outdir = "results"

workflow {
    sra_ch = channel.of(params.sra_id)
    DOWNLOAD_SRA(sra_ch)
    QC(DOWNLOAD_SRA.out.fastq)
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
