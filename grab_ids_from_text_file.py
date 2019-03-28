#https://stackoverflow.com/questions/18865058/extract-values-between-two-strings-in-a-text-file-using-python
for line in open('/media/owner/c3c5fbb4-73f6-45dc-a475-988ad914056e/phasing/trna/all_trna_from_all_genes_final.txt', 'r'):
	if "locus_tag" in line:
		data = line.split("locus_tag=")[1].split("][db_xref")[0]
		print(data)


		#Also can be done with this loop
		# for line in input_data:
		# 	match = re.search(r'(?<=\[locus_tag=).*(?=\]\[db_xre)', line)
			# if match:
			# 	print(match.group())


