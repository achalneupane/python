#!/usr/bin/env python
import sys
import os
import pathlib

myfasta = sys.argv[1]
fasta = open(myfasta)
# newfasta = sys.argv[2]
# newfasta = open(newfasta, 'w')

types = ['CDS', 'tRNA', 'rRNA', 'retrotransposons', 'mitochondria', 'IGR']
cwd = os.getcwd()



for type in range(len(types)):
    print('My type index is: ' + str(types[type]))
    # path = str(cwd+"/" + types[type])
    path = os.path.join(cwd, types[type])
    #print(path)
    # if type == 0:
    os.makedirs(path, exist_ok=True)
    newfile = ''.join([path, '/', myfasta, '_' , types[type], '.fasta'])
    newfasta = open(newfile, 'w')
    print(newfile)
    flag = False
    fasta = open(myfasta)
    for line in fasta:
        if line.startswith('>') and types[type] in line:
            flag = True
        elif line.startswith('>'):
          flag = False
        if flag:
            grabbed = line.strip()
            newfasta.writelines(grabbed + "\n")
            # print(grabbed)
    newfasta.close()

fasta.close


# import sys
# import os

# myfasta = sys.argv[1]
# with open(myfasta) as f:
#     lines = f.readlines()
# types = ['CDS', 'tRNA', 'rRNA']

# for type_index, type in enumerate(types):
#     print('My type index is:', type_index)
#     flag = False
#     for line in lines:
#         if line.startswith('>') and type in line:
#             flag = True
#         elif line.startswith('>'):
#             flag = False
#         if flag:
#             print(line.strip())           



##################
# from Bio import SeqIO; SeqIO.write((r for r in SeqIO.parse('in.fa', 'fasta') if 'CDS' in r.id), 'out.fa', 'fasta')


##################            

# #!/usr/bin/env python
# import sys
# import os
# myfasta = sys.argv[1]
# fasta = open(myfasta)
# #newfasta = sys.argv[2]
# #append_type = sys.argv[2]
# #newfasta = open(newfasta, 'w')
# #count = 0
# lines = fasta.readlines()
# for i, line in enumerate(lines):
#   if line.startswith('>') and 'CDS' in line:
#     print(line.strip())
#     print(lines[i+].strip())


##########################

# #!/usr/bin/env python
# import sys
# import os
# from collections import defaultdict

# myfasta = sys.argv[1]
# with open(myfasta) as fasta:
#     data = fasta.read().splitlines()

# pattern_data = defaultdict(list)
# index = 0
# while index < len(data):
#     if data[index].startswith('>'):
#         start = data[index].index('_') + 1
#         key = data[index][start:]
#         pattern_data[key].append(data[index + 1])
#     index += 2

## RUN as: python /home/owner/Dropbox/python/replace_fasta_header_with_number.py test_fasta.fasta new_fasta.fasta CDS