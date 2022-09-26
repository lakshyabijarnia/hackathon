fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    templist=line.split()
    for word in templist:
        if(word in lst):
            continue
        lst.append(word)
lst.sort()
print((lst))

