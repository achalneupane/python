pattern1 = re.compile(r'Degardome Category')
pattern2 = re.compile(r'Degradome p-value')
pattern3 = re.compile(r'Query')

l1 = []
l2 = []
l3 = []

with open('/home/mayankp/data.txt') as f:
    for i in f:
        if pattern1.search(i):
            a = re.sub('\n','',i)
            l1.append(a)
        elif pattern2.search(i):
            a = re.sub('\n','',i)
            l2.append(a)
        elif pattern3.search(i):
            a = re.sub('Query:','',i)
            b = re.sub('\n','',a)
            l3.append(b)

In [1244]: output = zip(l1,l2,l3)

In [1245]: output
Out[1245]: