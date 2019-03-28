#!/usr/bin/env python

fasta= open('/media/owner/newdrive/phasing/Domier_10RNAseq.2017104.tgz_transcriptome/Domier_10RNAseq.2017104/RNAseq/bbmap_trimmed/filtered_bbtrimmed/deseq2/esearch_output_for_deseq_genes.fasta')
newnames= open('/media/owner/newdrive/phasing/Domier_10RNAseq.2017104.tgz_transcriptome/Domier_10RNAseq.2017104/RNAseq/bbmap_trimmed/filtered_bbtrimmed/deseq2/locus_and_location_2.fasta')
newfasta= open('new_esearch.fasta', 'w')

for line in fasta:
    if line.startswith('>'):
        newname= newnames.readline()
        newfasta.write(newname)
    else:
        newfasta.write(line)

fasta.close()
newnames.close()
newfasta.close()
