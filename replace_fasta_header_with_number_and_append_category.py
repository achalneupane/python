#!/usr/bin/env python
import sys
import os
myfasta = sys.argv[1]
fasta = open(myfasta)
newfasta = sys.argv[2]
append_type = sys.argv[3]
newfasta = open(newfasta, 'w')
count = 0
for line in fasta:
    if line.startswith('>'):
        count +=1
        newname = '>' + str(count)+'_'+append_type+ '\n'
        newfasta.write(newname)
    else:
        newfasta.write(line)

fasta.close()
newfasta.close()



## RUN as: python /home/owner/Dropbox/python/replace_fasta_header_with_number.py test_fasta.fasta new_fasta.fasta CDS