import sys
import os
from Bio import SeqIO
from collections import defaultdict
filename = sys.argv[1]
outfile = sys.argv[2]
dedup_records = defaultdict(list)
# #### can create the full path where you ant files to be written
#dir_name='/media/owner/7ef86942-96a5-48a7-a325-6c5e1aec7408/symarzano2018June.201875/2018June.201875.bz2_files/trimmed_files/bbmap_trimmed_slagem_name_swapped_with_WTDK3/SsGenome/fastq.out/fastq.out_zero_mismatch_allowed/assembly.txt/assembly.fasta/most_repeated_sequences'  #directory where you want output files to be printed
#base_filename = filename
#suffix = '.fasta'
#outfile = os.path.join(dir_name, base_filename + "_Output" + suffix)
print (outfile)
for record in SeqIO.parse(filename, "fasta"):
    # Use the sequence as the key and then have a list of id's as the value
    dedup_records[str(record.seq)].append(record.id)
with open(outfile, 'w') as output:
#   # to get the counts of duplicated ids (sorted order)
    for seq, ids in sorted(dedup_records.items(), key = lambda t: len(t[1]), reverse=True):
        output.write("{}	{}\n".format(seq,len(ids)))
        #output.write(seq + "\n")

#    # to get all the duplicated ids appended
#    for seq, ids in dedup_records.items():
#        # Join the ids and write them out as the fasta
#        output.write(">{}\n".format('|'.join(ids))) 
#        output.write(seq + "\n")


##test_fasta.fasta
#>XXKHH_1
#AAAAATTTCTGGGCCCC
#>YYYXXKHH_1
#TTAAAAATTTCTGGGCCCCGGGAAAAAA
#>TTDTT_11
#TTTGGGAATTAAACCCT
#>ID_2SS
#TTTGGGAATTAAACCCT
#>YKHH_1
#TTAAAAATTTCTGGGCCCCGGGAAAAAA
#>YKHSH_1S
#TTAAAAATTTCTGGGCCCCGGGAAAAAA
