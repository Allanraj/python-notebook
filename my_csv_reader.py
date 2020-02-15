#reading files
f = open('housing.data', 'r')
#if f.read() == '1':
 #       print("something")


data = []
for line in f:
    data_line = line.rstrip().split('\t')
    data.append(data_line)
print (data)

