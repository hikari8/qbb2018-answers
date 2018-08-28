#!/bin/bash

GENOME=../genomes/BDGP6
 =../genomes/BDGP6.Ensembl.81.gtf

for SAMPLE in SRR072893 SRR072903 SRR072905 SRR072915
do
    echo "working on sample $SAMPLE"
    mkdir $SAMPLE
    echo "running fastqc"
    fastqc ../rawdata/${SAMPLE}.fastq
    echo "running hisat"
    hisat2 -p 4 -x ../genomes/BDGP6 -U ~/data/rawdata/${SAMPLE}.fastq -S ${SAMPLE}/${SAMPLE}.sam
    echo "running samtools"
    samtools view -S -b ${SAMPLE}/${SAMPLE}.sam -o ${SAMPLE}/${SAMPLE}.bam
    samtools sort ${SAMPLE}/${SAMPLE}.bam -o ${SAMPLE}/${SAMPLE}.sorted.bam
    samtools index ${SAMPLE}/${SAMPLE}.sorted.bam
    echo "running stringtie"
    stringtie ${SAMPLE}/${SAMPLE}.sorted.bam -G ../genomes/BDGP6.Ensembl.81.gtf -p 8 -e -B -o ${SAMPLE}/${SAMPLE}.abund.gtf
done
