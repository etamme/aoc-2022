import sys

total1=0
total2=0
for line in sys.stdin:
  line = line.strip()
  if(line):
    s1,s2 = line.split(',')
    l1= list(map(int,s1.split('-')))
    l2 = list(map(int,s2.split('-')))
    l1.sort();l2.sort()
    s1min=l1[0];s1max=l1[1]
    s2min=l2[0];s2max=l2[1]
    # part 1
    if(s1min<=s2min and s1max>=s2max or s2min<=s1min and s2max>=s1max):
      total1 +=1
    # part 2
    if(len(set(list(range(s1min,s1max+1))) & set(list(range(s2min,s2max+1))))>0):
      total2 +=1

# output
print("completely contained:"+str(total1))
print("partially contained:"+str(total2))
