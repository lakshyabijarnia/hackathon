# Use the file name mbox-short.txt as the file name
from itertools import count


fname = input("Enter file name: ")
counter=0
float_no=0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    # print(line)
    counter=counter+1
    pos=line.find(':')
    fstring=line[pos+1:]
    float_no=float_no+float(fstring)
avg_floats=float_no/counter

print("Average spam confidence:",avg_floats)
