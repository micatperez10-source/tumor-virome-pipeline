# MCF-7 Variant Calling Pipeline

Pipeline bioinformático para detección de variantes genómicas en la línea celular de cáncer de mama **MCF-7**, usando datos públicos de NCBI SRA.

## Pregunta biológica
¿Qué variantes genéticas presenta la línea celular MCF-7 en el cromosoma 22?

## Herramientas utilizadas
- **Nextflow** — orquestación del pipeline
- **FastQC** — control de calidad de reads
- **Trimmomatic** — filtrado y trimming de adaptadores
- **BWA** — alineamiento contra genoma humano GRCh38
- **Samtools** — procesamiento de alineamientos
- **BCFtools** — variant calling

## Resultados (SRR8476839, chr22)
| Métrica | Valor |
|---|---|
| Reads totales | 51,186,014 |
| Reads alineados | 6.35% (chr22) |
| SNPs detectados | 89,243 |
| INDELs detectados | 1,070 |
| Total variantes | 90,636 |

## Cómo correr el pipeline
```bash
git clone https://github.com/micatperez10-source/tumor-virome-pipeline
cd tumor-virome-pipeline
nextflow run main.nf
```

## Datos
- Organismo: *Homo sapiens*
- Línea celular: MCF-7 (adenocarcinoma de mama)
- Accession: SRR8476839
- Referencia: GRCh38 cromosoma 22
