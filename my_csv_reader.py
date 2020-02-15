#reading files
f = open('housing.data', 'r')
#if f.read() == '1':
 #       print("I have a file to read")

data = []
for line in f.readlines():
    data_line = line.rstrip().split('\n')
    data.append(data_line)
    print (data)

#else:
#    print('Booooo')