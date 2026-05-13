## MCF-7 Variant Calling Pipeline

Bioinformatics pipeline for genomic variant detection in the **MCF-7** breast cancer cell line, using public data from NCBI SRA.

## Biological question
What genetic variants does the MCF-7 cell line present in chromosome 22?

## Tools used
- **Nextflow** — pipeline orchestration
- **FastQC** — read quality control
- **Trimmomatic** — adapter trimming and filtering
- **BWA** — alignment against human genome GRCh38
- **Samtools** — processing of alignments
- **BCFtools** — variant calling

## Results (SRR8476839, chr22)
| Metric | Value |
|---|---|
| Total reads | 51,186,014 |
| Aligned reads | 6.35% (chr22) |
| SNPs detected | 89,243 |
| INDELs detected | 1,070 |
| Total variants | 90,636 |

## How to run
```bash
git clone [https://github.com/micatperez10-source/mcf7-variant-calling-nf](https://github.com/micatperez10-source/mcf7-variant-calling-nf)
cd mcf7-variant-calling-nf
nextflow run main.nf
