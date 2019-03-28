import re
# from pandas import DataFrame as df

# results = {}
# with open('/media/owner/newdrive/phasing/Domier_10RNAseq.2017104.tgz_transcriptome/Domier_10RNAseq.2017104/RNAseq/bbmap_trimmed/filtered_bbtrimmed/deseq2/esearch_output_for_deseq_genes.txt', 'r') as f_file:
#     data = f_file.readlines()
#     for line in data:
#         results.update(re.findall(
#             r'^>lcl.*\[locus_tag=(.*?)\].*\[location=(.*?)\]',
#             line
#         ))

# df_ = df(
#     list(results.items()),
#     index=range(1, len(results) + 1),
#     columns=['locus', 'location']
# )
# print(df_)
# df_.to_csv('locus_and_location.csv', sep='\t')

results = []
with open('/media/owner/newdrive/phasing/Domier_10RNAseq.2017104.tgz_transcriptome/Domier_10RNAseq.2017104/RNAseq/bbmap_trimmed/filtered_bbtrimmed/deseq2/esearch_output_for_deseq_genes.txt', 'r') as f_file:
    data = f_file.read()
    results = re.findall(r'>lcl.*\[locus_tag=(.*?)\].*\[location=(.*?)\]', data)
    #print(results)
for locus, location in results:
   print(locus, location, sep = '\t')

# #############
# #df.to_csv('locus_and_location.csv', sep='\t')


##Another variation using a dict as a result and by splitting lines:

#import re

#results = {}
#with open('fichier1', 'r') as f_file:
#    data = f_file.readlines()
#    for line in data:
#        results.update(re.findall(r'^>lcl.*\[locus_tag=(.*?)\].*\[location=(.*?)\]', line))
#
#for locus, location in results.items():
#    print(locus, location)
