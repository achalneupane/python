import sys
# import re

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")
import re
import pandas as pd
text = open("/media/owner/b54f3251-5380-4288-9ddf-fa3357ea8294/Domier_26_smallRNA.20171119/trimmed_files/fastq.out/differential_expression/sshadv1_vs_wt_DF/tRNA_read_counts_from_new_library-exactmatch_set2.txt",'r').read()
# print(text)
# print(type(text))
# results = re.findall(r'(trimmed.*.fastq)\nSeq_132582_1: ATCCGAATTAGTGTAGGGGTTAACATAACTCT: \n(\d)\nSeq_483974_49238: TCCGAATTAGTGTAGGGGTTAACATAACTC: \n(\d)\nSeq_483975_2034: TCCGAATTAGTGTAGGGGTTAACATAACTCG: \n(\d)\nSeq_483976_27121: TCCGAATTAGTGTAGGGGTTAACATAACTCGC: \n(\d)\nSeq_483977_41181: TCCGAATTAGTGTAGGGGTTAACATAACTCGCT: \n(\d)\nSeq_483978_1: TCCGAATTAGTGTAGGGGTTAACATAACTCGCTT: \n(\d)\nSeq_483979_10: TCCGAATTAGTGTAGGGGTTAACATAACTCGCTTT: \n(\d*)',text)
results = re.findall(r'Counting[*]+File:[ ]*([\w.]+)[ \n]*[ *\w]+:[ :\w]+[\n]*([\w.]+)[ \n]*[ *\w]+:[ :\w]+[\n]*([\w.]+)[ \n]*[ *\w]+:[ :\w]+[\n]*([\w.]+)[ \n]*[ *\w]+:[ :\w]+[\n]*([\w.]+)[ \n]*[ *\w]+:[ :\w]+[\n]*([\w.]+)[ \n]*[ *\w]+:[ :\w]+[\n]*(\w+)[\n]*[ *\w]+:[ :\w]+[\n]*(\w+)', text, re.MULTILINE)

print (results)
# print(pd.DataFrame(results))
df=pd.DataFrame(results)
df.columns=['FileName','Seq_132582_1','Seq_483974_49238','Seq_483975_2034','Seq_483976_27121','Seq_483977_41181','Seq_483978_1','Seq_483979_10'] #This doesn't work
print(df)
df.to_csv('/media/owner/b54f3251-5380-4288-9ddf-fa3357ea8294/Domier_26_smallRNA.20171119/trimmed_files/fastq.out/differential_expression/sshadv1_vs_wt_DF/Table_tRNA_read_counts_from_new_library-exactmatch_set2', sep='\t')
# pattern1 = 'Counting'
# pattern2 = 'Seq_132582_1'
# pattern3 = 'Seq_483974_49238'
# # pattern1 = re.compile(r'Counting')
# # pattern2 = re.compile(r'Seq_132582_1')
# # pattern3 = re.compile(r'Seq_483974_49238')

# l1 = []
# l2 = []
# l3 = []

# # l2 = []
# # l3 = []
# with open("text.txt", "r") as ifile:
#     for line in ifile:
#         if line.startswith(pattern1):
#             a =next(ifile, '').strip()
#             # print(a)
#             l1.append(a)
#         if line.startswith(pattern2):
#             a =next(ifile, '').strip()
#             # print(a)
#             l2.append(a)
#         if line.startswith(pattern3):
#             a =next(ifile, '').strip()
#             # print(a)
#             l3.append(a)

#         # if pattern1.search(line):
#         #     a = re.sub('\n','',line)
#         #     print(a)
#         #     l1.append(a)
#         # elif pattern2.search(line):
#         #     a = re.sub('\n','',line)
#         #     l2.append(a)
#         #     print(a)
#         # elif pattern3.search(line):
#         #     b = re.sub('\n','',line)
#         #     l3.append(b)
#         #     print(b)
# #In [1244]: output = zip(l1,l2,l3)
# #             # print(a)
# #             file_name=line
# #             # print(file_name)
# #             l1.append(file_name)
# #         elif line.startswith(pattern2):
# #             value1 =next(ifile, '').strip()
# #             # print(value)
# #             l2.append(value1)
# #         elif line.startswith(pattern3):
# #             value2 =next(ifile, '').strip()
# #             # print(value)
# #             l3.append(value2)

# output = zip(l1,l2,l3)
# # output = zip(file_name,value1,value2)
# print(output)